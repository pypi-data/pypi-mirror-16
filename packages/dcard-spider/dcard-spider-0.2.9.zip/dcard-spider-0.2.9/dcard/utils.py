# -*- coding: utf-8 -*-

import logging
import itertools
from multiprocessing.dummy import Pool
from six.moves import http_client as httplib

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import RetryError
from requests_futures.sessions import FuturesSession

logger = logging.getLogger('dcard')


class _Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(_Singleton('SingletonMeta', (object,), {})):
    pass


class Client(Singleton):

    def __init__(self, workers=8):
        self.fut_session = FuturesSession(max_workers=workers)
            # gevent is much better !!!!!
            '''
            import grequests
            session = grequests.AsyncRequest(session=session)
            '''
        self.req_session = requests.Session()
        self.thread_pool = Pool(processes=workers) # how to recycle?
        self.retries = Retry(
            total=5,
            backoff_factor=0.1,
            status_forcelist=[500, 502, 503, 504])
        self.req_session.mount('https://', HTTPAdapter(max_retries=self.retries))

    def get(self, url, **kwargs):
        try:
            response = self.req_session.get(url, **kwargs)
            data = response.json()
            if isinstance(data, dict) and data.get('error'):
                raise ServerResponsedError
            return data
        except ValueError:
            man_retry = kwargs.get('man_retry', 1)
            if man_retry > 5:
                return {}
            logger.error('when get {}, error {}; and retry#{}...'.format(url, e, man_retry))
            return self.get(url, man_retry=man_retry + 1, **kwargs)
        except ServerResponsedError:
            logger.error('when get {}, error {}; status_code {}'.format(
                url, data, response.status_code))
            return {}
        except httplib.IncompleteRead as e:
            logger.error('when get {}, error {}; partial: {}'.format(url, e, e.partial))
            return {}  # or should we return `e.partial` ?
        except RetryError as e:
            logger.error('when get {}, error {}'.format(url, e))

    def get_stream(self, url, **kwargs):
        return self.req_session.get(url, stream=True, **kwargs)

    def fut_get(self, url, **kwargs):
        return self.fut_session.get(url, **kwargs)

    def parallel_tasks(self, function, tasks):
        return self.thread_pool.map_async(function, tasks)


def flatten_lists(meta_lists):
    return list(itertools.chain.from_iterable(meta_lists))


def chunks(elements, chunck_size=30):
    for i in range(0, len(elements), chunck_size):
        yield elements[i:i+chunck_size]


class ServerResponsedError(Exception):
    pass
