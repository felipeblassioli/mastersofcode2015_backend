from flask import *
from .services import *

def create_rest_blueprint():
	rest = Blueprint('rest', __name__)
	return rest

rest = create_rest_blueprint()

@rest.route('/')
def index():
	return "Hello"

@rest.route('/user/<user_id>', methods=['GET'])
@rest.route('/user/', methods=['POST'])
def users_index(user_id=None):
	if request.method == 'GET':
		return User.get(User.id == user_id)
	elif request.method == 'POST':
		params = request.get_json()
		print 'params', params
		usr = User.create(**params)
		print usr
		return jsonify(usr.to_json())

@rest.route('/user/payments/', methods=['GET','POST'])
def payments():
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		return "POST payments"
