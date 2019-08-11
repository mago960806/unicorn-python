import tornado.ioloop
import tornado.web

from api.handlers import *


def make_app():
    return tornado.web.Application(
        [
            (r"/api/v1/unicorns/", MainHandler),
        ],
        debug=True
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
