# encoding: utf-8
from flask import Flask, Blueprint, render_template, request


from flask import current_app
def bla():
	#print current_app.url_map
	pass

def create_app():
	app = Flask(__name__)
	app.config["SECRET_KEY"] = 'development key'
	from .tablet import tablet
	app.register_blueprint(tablet, url_prefix='/tablet')

	from .rest import rest
	app.register_blueprint(rest, url_prefix='/rest')
	app.before_first_request(bla)

	from .services import init_app, User, Invoice, Product
	init_app(app)

	import logging
	logger = logging.getLogger('peewee')
	logger.setLevel(logging.DEBUG)
	logger.addHandler(logging.StreamHandler())

	from flask.ext.admin import Admin
	from flask.ext.admin.contrib.peewee import ModelView
	admin = Admin(app, name="Bla")

	for m in [User,Invoice,Product]:
		admin.add_view(ModelView(m))
	return app

