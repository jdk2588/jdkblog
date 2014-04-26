from application import BaseApp
from admin import admin
from about import about

class Urls(BaseApp):
    def attach_urls(self):
        self.app.register_blueprint(about)
        self.app.register_blueprint(admin)
