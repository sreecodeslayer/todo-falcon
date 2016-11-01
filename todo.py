import falcon
from settings import APP_ROOT_DIR, TEMPLATE_DIR
from pymongo import MongoClient

api = falcon.API

db = MongoClient(connect=False).todo
users = db.users


class Todo(object):
    def on_get(self, req, resp):
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_200
        resp.stream = open(TEMPLATE_DIR+'index.html','rb')
