import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '.py_ML_ai_MIT'