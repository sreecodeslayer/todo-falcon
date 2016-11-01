import falcon
from settings import APP_ROOT_DIR, TEMPLATE_DIR, TODO_URL_PATHS
from pymongo import MongoClient

api = falcon.API

db = MongoClient(connect=False).todo
users = db.users

class Todo(object):
    def on_get(self, req, resp):
        if req.path == '/todo':
            resp.content_type = 'text/html'
            resp.status = falcon.HTTP_200
            resp.stream = open(TEMPLATE_DIR+'todo.html','rb')
        elif req.path == '/todo/add':
            resp.status = falcon.HTTP_200
            resp.body = "'message':'add todo'"
        elif req.path == '/todo/done':
            resp.status = falcon.HTTP_200
            resp.body = "'message':'completed todo'"
        elif req.path == '/todo/edit':
            resp.status = falcon.HTTP_200
            resp.body = "'message':'edit todo'"
        elif req.path == '/todo/remove':
            resp.status = falcon.HTTP_200
            resp.body = "'message':'remove'"
        elif req.path not in TODO_URL_PATHS:
            resp.status = falcon.HTTP_404
            resp.body = "'message':'Sorry, 404'"
