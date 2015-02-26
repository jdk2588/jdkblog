from application import BaseApp
from admin import admin
from about import about
from socialweb import socialweb

class Urls(BaseApp):
    def attach_urls(self):
        self.app.register_blueprint(about)
        self.app.register_blueprint(admin)
        self.app.register_blueprint(socialweb)
