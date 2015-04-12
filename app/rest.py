from flask import *
from .services import *

def create_rest_blueprint():
	rest = Blueprint('rest', __name__)
	return rest

rest = create_rest_blueprint()

@rest.route('/')
def index():
	return "Hello"


@rest.route('/users/', methods=['GET','POST'])
def users_index():
	return jsonify(dict(bla=User()))

@rest.route('/users/payments/', methods=['GET','POST'])
def payments():
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		return "POST payments"
