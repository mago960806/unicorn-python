import tornado.web

from spider.db import MongoDB

__all__ = ['MainHandler']


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        with MongoDB(host='127.0.0.1', port=27017, db_name='techcrunch', collection_name='unicorns') as db:
            self.finish({'results': [item for item in db.find({}, {'_id': 0})]})
