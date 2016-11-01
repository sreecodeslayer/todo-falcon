import falcon
from pymongo import MongoClient

api = falcon.API

db = MongoClient(connect=False).todo
users = db.users


class Todo(object):
    def on_get(self, req, resp):
        resp.body = '{"message":"To-Do App"}'
        resp.status = falcon.HTTP_200
