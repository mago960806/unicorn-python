# import motor
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from api.handlers import *
from spider.task import TechCrunchSpider

define(name='port', default=8888, type=int, help='监听端口')


def make_app():
    # db = motor.motor_tornado.MotorClient('mongodb://localhost:27017').techcrunch
    return tornado.web.Application(
        [
            (r"/api/v1/unicorns/", UnicornHandler),
        ],
        # db=db,
        debug=True
    )


if __name__ == "__main__":
    # 初始化爬虫
    spider = TechCrunchSpider()

    tornado.options.parse_command_line()
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.PeriodicCallback(spider.save_unicorns, 1000 * 60 * 1).start()
    tornado.ioloop.IOLoop.current().start()
