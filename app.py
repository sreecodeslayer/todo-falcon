import falcon
import todo
import user
from static import StaticMiddleware

api = application = falcon.API()
todo = todo.Todo()
user_login = user.Login()
user_signup = user.Signup()

api.add_route('/', todo)
api.add_route('/login', user_login)
api.add_route('/signup', user_signup)
# todo crud operations

api.add_route('/todo', todo)
api.add_route('/todo/add', todo)
api.add_route('/todo/done', todo)
api.add_route('/todo/edit', todo)
api.add_route('/todo/done', todo)
api.add_route('/todo/remove', todo)
api = StaticMiddleware(api)
