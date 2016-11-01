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
api = StaticMiddleware(api)
