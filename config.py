import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"