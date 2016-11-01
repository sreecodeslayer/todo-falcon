# CONSTANTS / DIRS / SETTINGS GOES HERE
import os

APP_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIR = os.path.join(APP_ROOT_DIR,'templates/')

# ALLOWED URLS RELATED TO Todo
TODO_URL_PATHS = ['/todo','/todo/add','/todo/remove','/todo/edit','/todo/done']
