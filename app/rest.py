from flask import *
from .services import *
from . import app

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
		usr = User.get(User.id == user_id)
		return jsonify(usr.to_json())
	elif request.method == 'POST':
		params = request.get_json()
		print 'params', params
		try:
			usr = User.get(User.email == params['email'])
			for k,v in params.items():
				setattr(usr,k,v)
			usr.save()
		except User.DoesNotExist:
			usr = User.create(**params)
		print usr
		return jsonify(usr.to_json())

@rest.route('/user/payments/', methods=['GET','POST'])
def payments():
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		return "POST payments"

@rest.route('/user/<user_id>/invoice/', methods=['GET','POST'])
def invoices(user_id):
	user = User.get(User.id == user_id)
	if request.method == 'GET':
		invs = [ i.to_json() for i in user.invoices2 ]
		return jsonify(dict(invoices=invs))
	elif request.method == 'POST':
		listItems = request.get_json()['list_items']
		invoice = user.send_invoice(listItems)
		return jsonify(invoice.to_json())

from .services import Product
@rest.route('/user/<user_id>/transaction')
def transaction(user_id):
	products = [ p for p in Product.select() ]
	customer = User.get(User.id == user_id)
	current_user = dict(name='Test01', image='', categories=['food', 'restaurant'])
	return render_template('transaction.html', user=current_user, products=products, customer=customer)