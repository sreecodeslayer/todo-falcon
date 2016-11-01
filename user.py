import falcon
import bcrypt
import os
import binascii  # for cookie random hex
from datetime import datetime
from pymongo import MongoClient
from settings import APP_ROOT_DIR, TEMPLATE_DIR

api = falcon.API()

db = MongoClient(connect=False).todo
users = db.users


class Login(object):

    def on_post(self, req, resp):
        user = {}
        data = req.stream.read()
        user['username'] = data.split('&')[0].split('=')[1]
        user['password'] = data.split('&')[1].split('=')[1]
        '''
        USE THIS FOR REST CLIENT TESTING, For HTML form, encoding is to be taken care as in above codes
         user = {'username': req.get_param(
            'username'), 'password': req.get_param('password')}
        '''
        # Check if there is a user
        if users.find({'username': user['username']}).count() > 0:
            # get the salt used for that user while signup
            salt = users.find_one({'username': user['username']})

            # match the hashed password
            if bcrypt.hashpw(user['password'], str(salt['password'])) == str(salt['password']):
                resp.body = "Successfully validated " + str(user)
                resp.status = falcon.HTTP_200
                # set cookie and store cookie in db for future (untill logout)
                the_cookie = str(binascii.b2a_hex(
                    os.urandom(15)) + str(datetime.now()))
                resp.set_cookie('the-magic-key', the_cookie)
            else:
                resp.status = falcon.HTTP_200
                # No need to show this to user in real application
                resp.body = 'Invalid login credentials, wrong password'
        else:
            resp.status = falcon.HTTP_200
            # No need to show this to user in real application
            resp.body = 'Invalid login credentials, user not found'


class Signup(object):

    def on_get(self, req, resp):
        print req.uri, req.relative_uri
        print "########## GET ###########"
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_200
        resp.stream = open(TEMPLATE_DIR + 'signup.html', 'rb')

    def on_post(self, req, resp):
        new_user = {}
        data = req.stream.read()
        new_user['name'] = data.split('&')[0].split('=')[1]
        new_user['username'] = data.split('&')[1].split('=')[1]
        new_user['email'] = data.split('&')[2].split('=')[1]
        new_user['password'] = data.split('&')[3].split('=')[1]
        '''
        USE THIS FOR REST CLIENT TESTING, For HTML form, encoding is to be taken care as in above codes
        new_user = {
            'name': req.get_param('name'),
            'username': req.get_param('username'),
            'password': req.get_param('password'),
            'email': req.get_param('email')
        }
        '''
        # Check db for existing username
        if users.find({'username': str(new_user['username'])}).count() > 0:
            resp.body = "User exists. Please use another username!"
        else:
            # if not Signup by inserting
            user_obj_id = users.insert_one({
                'username': new_user['username'],
                'password': bcrypt.hashpw(new_user['password'], bcrypt.gensalt()),
                'salt': bcrypt.gensalt(),
                'name': new_user['name'],
                'email': new_user['email']
            })
            resp.content_type = 'text/html'
            resp.status = falcon.HTTP_200
            resp.stream = open(TEMPLATE_DIR + 'index.html', 'rb')
            # redirection to login goes here
