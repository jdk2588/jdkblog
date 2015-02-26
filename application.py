import settings
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

#@singleton
class BaseApp(object):
    def __init__(self, *args, **kwargs):
        self.app = Flask(__name__)

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)
        self.db = MongoEngine(self.app)
