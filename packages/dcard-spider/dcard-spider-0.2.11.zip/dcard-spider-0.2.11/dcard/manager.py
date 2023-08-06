from __future__ import absolute_import, unicode_literals

import os
import re
import logging
import contextlib
from multiprocessing.dummy import Pool

from dcard.utils import Client

logger = logging.getLogger(__name__)


reg_images = \
    re.compile('http[s]?://\S+\.(?:jpg|png|gif)')
reg_imgur = \
    re.compile('http[s]?://imgur.com/(\w+)')
reg_imgur_file = \
    re.compile('http[s]?://i.imgur.com/\w+\.(?:jpg|png|gif)')

pattern_imgur_file = 'http://i.imgur.com/{img_hash}.jpg'

client = Client()


def download(task):
    filepath, src = task
    if os.path.exists(filepath):
        return True, src
    response = client.get_stream(src)
    if response.ok:
        with open(filepath, 'wb') as stream:
            for chunk in response.iter_content(chunk_size=1024):
                stream.write(chunk)
    return (response.ok, src)


class Downloader:

    def __init__(
            self, download_folder=None, subfolder_pattern=None, flatten=False):
        self.resources_folder = download_folder or './downloads'
        self.subfolder_pattern = subfolder_pattern or '({id}) {folder_name}'
        self.done_resources = 0
        self.flatten = flatten

    def set_bundles(self, resource_bundles):
        self.resource_bundles = resource_bundles

    def download(self):
        logger.info('[Downloader] takes hand')
        Downloader.mkdir(self.resources_folder)
        tasks = []
        for bundle in self.resource_bundles:
            meta, urls = bundle
            if len(urls) == 0:
                continue
            self.done_resources += len(urls)
            tasks += [(self._gen_filepath(meta, url), url) for url in urls]

        with contextlib.closing(Pool(8)) as pool:
            async_results = pool.map_async(download, tasks)
            results = async_results.get()

        status = [ok for ok, _ in results]
        fails = [src for ok, src in results if not ok]
        logger.info('[Downloader] finish %d items!', len(status))
        return status, fails

    def _gen_filepath(self, meta, url):
        folder = self._gen_full_folder(meta)
        base_name = os.path.basename(url)
        filepath = '{folder_name}{separator}{file_name}'.format(
            folder_name=folder,
            file_name=base_name,
            separator='-' if self.flatten else '/'
        )
        Downloader.mkdir(folder) if not self.flatten else None
        return filepath

    def _gen_full_folder(self, meta):

        # clean garbage text in title !
        safe_title = re.sub('[\?\\\\/><:"|\*\.]', '', meta['title']).strip()
        safe_title = ''.join([c for c in safe_title if ord(c) > 0x1f])

        meta['folder_name'] = safe_title
        folder = self.subfolder_pattern.format(**meta)
        return self.resources_folder + '/' + folder

    @staticmethod
    def mkdir(path):
        if not os.path.exists(path):
            os.makedirs(path)


class ContentParser:

    def __init__(self, results):
        self.results = results

    def parse(self):

        def parse(post):
            article = post.get('content') or ''
            comments = post.get('comments') or []
            imgur_files = ContentParser._parse_images(article)
            for comment in comments:
                imgur_files += ContentParser._parse_images(comment.get('content', ''))
            del post['content']
            return (post, imgur_files)

        logger.info('[ContentParser] takes hand')
        resoures = [parse(post) for post in self.results]
        logger.info('[ContentParser] collects %d resources', len(resoures))
        return resoures

    @staticmethod
    def _parse_images(raw_data):
        imgurs = reg_imgur.findall(raw_data)
        imgur_files = reg_imgur_file.findall(raw_data)
        imgur_files += [pattern_imgur_file.format(img_hash=r) for r in imgurs]
        return imgur_files
