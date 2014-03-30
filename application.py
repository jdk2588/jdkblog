import settings
from flask import Flask

#def singleton(cls):
#    instances = {}
#    def getinstance():
#        if cls not in instances:
#            instances[cls] = cls()
#        return instances[cls]
#    return getinstance
#
#@singleton
class BaseApp(object):
    def __init__(self, *args, **kwargs):
        self.app = Flask(__name__)

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)