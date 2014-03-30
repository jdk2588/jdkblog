from application import BaseApp
from handlers import Handlers

class Urls(BaseApp):
    def attach_urls(self):
        self.app.add_url_rule("/", view_func=Handlers.root)
        self.app.add_url_rule("/about", view_func=Handlers.about)
