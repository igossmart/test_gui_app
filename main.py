import tornado.ioloop
import tornado.web
import json

data_user = {'id': 23445, 'name': 'Петров Егор', 'skills': 'PHP, HTML/CSS/JS'}


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(data_user))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    print('Запуск сервера..')
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
