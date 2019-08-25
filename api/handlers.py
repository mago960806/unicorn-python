import json

import tornado.web

from spider.db import MongoDB

__all__ = ['MainHandler', 'UnicornHandler']


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        pass


class UnicornHandler(tornado.web.RequestHandler):
    def get(self):
        page = int(self.get_argument('page', '1'))
        page_size = int(self.get_argument('page_size', '10'))
        # country = (self.get_argument('country', None))
        # name = (self.get_argument('name', None))
        # category = (self.get_argument('category', None))

        with MongoDB(host='127.0.0.1', port=27017, db_name='techcrunch', collection_name='unicorns') as db:
            self.finish(db.find_one({}, {'_id': 0, 'entities': {'$slice': [(page - 1) * page_size, page_size]}}))

# class DataSourceHandler(tornado.web.RequestHandler):
#     async def get(self):
#         url = 'https://techcrunch.com/wp-json/tc/v1/crunchbase/unicorns?cachePrevention=0'
#         headers = {
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
#         }
#         http_client = AsyncHTTPClient(force_instance=True, defaults=headers)
#         while True:
#             try:
#                 response = await http_client.fetch(url, validate_cert=False, connect_timeout=10)
#             except Exception as e:
#                 print(f'接口请求异常: {e}')
#             else:
#                 print(f'接口请求成功: [{response.code} {response.reason}] {int(response.request_time * 1000)}ms')
#                 print(json.loads(response.body))
