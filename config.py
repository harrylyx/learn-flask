import os
basedir = 'mysql+pymysql://root:lyx15lyx@localhost:3306/blog'

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or basedir
    SQLALCHEMY_TRACK_MODIFICATIONS = False
