from chalice import Chalice
from pylti.chalice import lti

app = Chalice(app_name='lti-chalice-sample')
app.debug = True 

@app.route('/', methods=['POST'], content_types=['application/x-www-form-urlencoded'])
@lti(request='initial', app=app)
def index(lti=lti):
    return {'hello': 'world'}
