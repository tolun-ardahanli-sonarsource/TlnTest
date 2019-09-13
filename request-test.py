import ssl

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

class Tls12Adapter(HTTPAdapter):
    """"Transport adapter that forces TLSv1.2"""

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        self.poolmanager = PoolManager(
            *pool_args,
            ssl_version=ssl.PROTOCOL_TLSv1_2,
            **pool_kwargs)

class Ssl3Adapter(HTTPAdapter):
    """"Transport adapter that forces SSLv3"""

    def init_poolmanager(self, *pool_args, **pool_kwargs):

        self.poolmanager = PoolManager(
            *pool_args,
            ssl_version=ssl.PROTOCOL_SSLv3,
            **pool_kwargs)