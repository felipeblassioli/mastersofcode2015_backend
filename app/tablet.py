from flask import *


def create_tablet_blueprint():
	tablet = Blueprint('tablet', __name__, template_folder='templates')
	return tablet

tablet = create_tablet_blueprint()

@tablet.route('/')
def index():
	return render_template('index.html')
