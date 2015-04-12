from flask import *
from .services import *

def create_tablet_blueprint():
	tablet = Blueprint('tablet', __name__, template_folder='templates')
	return tablet

tablet = create_tablet_blueprint()

@tablet.route('/')
def index():
	current_user = dict(name='North Buy', image='', categories=['food', 'restaurant'])
	users = [ u for u in User.select() ]
	products = [ p for p in Product.select() ]
	return render_template('index.html', user=current_user, users=users, products=products)
