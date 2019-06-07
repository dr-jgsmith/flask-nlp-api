# -*- coding: utf-8 -*-

#Server Configuration
HOST = '0.0.0.0'
PORT = 9001
DEBUG = True
USE_RELOADER = True
SECRET_KEY = 'supersecretkey'

#DB Configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///nlp/data/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DB_CREATED = False

# IPFS Configuration
IPFS_HOST = '127.0.0.1'
IPFS_PORT = 5001

# Redirect Configuration
SHORT_REDIRECT_DOMAIN = "http://{0}:{1}".format(HOST, PORT)
REDIRECT_BASE_URL = "http://ipfs.io/ipfs/"

# Upload Configuration
UPLOAD_FOLDER = '/Users/justinsmith/PycharmProjects/modernai/nlp/data/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'dict', 'mm'])

# Firebase Integration
FIREBASE_CONFIG = {
    "apiKey": "AIzaSyC8L8yaFtSWEFpvngLG_fKhHX-8oCt3VSg",
    "authDomain": "stellar-flask.firebaseapp.com",
    "databaseURL": "https://stellar-flask.firebaseio.com",
    "projectId": "stellar-flask",
    "storageBucket": "stellar-flask.appspot.com",
    "messagingSenderId": "373373108982"
}

REDIS_URL = 'redis://localhost:6379/0'