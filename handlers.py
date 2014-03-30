from flask import render_template

class Handlers(object):

    @classmethod
    def root(self):
        raise NotImplementedError

    @classmethod
    def about(self):
        return render_template('about.html')
