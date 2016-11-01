import falcon
import bcrypt
import os
import binascii  # for cookie random hex
from datetime import datetime
from pymongo import MongoClient

api = falcon.API

db = MongoClient(connect=False).todo
users = db.users


class Login(object):

    def on_post(self, req, resp):
        user = {'username': req.get_param(
            'username'), 'password': req.get_param('password')}
        # Check if there is a user
        if users.find({'username': user['username']}).count() > 0:
            # get the salt used for that user while signup
            salt = users.find_one({'username': user['username']})

            # match the hashed password
            if bcrypt.hashpw(user['password'], str(salt['password'])) == str(salt['password']):
                resp.body = "Successfully validated" + str(user)
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

    def on_post(self, req, resp):
        new_user = {
            'name': req.get_param('name'),
            'username': req.get_param('username'),
            'password': req.get_param('password')
        }

        # Check db for existing username
        if users.find({'username': str(new_user['username'])}).count() > 0:
            resp.body = "User exists. Please use another username!"
        else:
            # if not Signup by inserting
            user_obj_id = users.insert_one({
                'username': new_user['username'],
                'password': bcrypt.hashpw(new_user['password'], bcrypt.gensalt()),
                'salt': bcrypt.gensalt(),
                'name': new_user['name']
            })
            resp.body = str({'ObjectID', user_obj_id})
            resp.status = falcon.HTTP_200
            # redirection to login goes here
