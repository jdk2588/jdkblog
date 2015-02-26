from flask import request, Blueprint
from flask import render_template
from flask.views import MethodView

socialweb = Blueprint("socialweb", __name__)

#class RegexConverter(BaseConverter):
#    def __init__(self, url_map, *items):
#        super(RegexConverter, self).__init__(url_map)
#        self.regex = items[0]

class SocialWebView(MethodView):

    def get(self, number):
        if number==1:
        	return render_template('index1.html')
        elif number==2:
        	return render_template('index2.html')
	else:
        	return render_template('404.html')


socialweb.add_url_rule('/socialweb/page<int:number>', view_func=SocialWebView.as_view('socialweb'))
