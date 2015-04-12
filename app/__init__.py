# encoding: utf-8
from flask import Flask, Blueprint, render_template, request


from flask import current_app
def bla():
	pass
	#print current_app.url_map

def create_app():
	app = Flask(__name__)
	from .tablet import tablet
	app.register_blueprint(tablet, url_prefix='/tablet')

	from .rest import rest
	app.register_blueprint(rest, url_prefix='/rest')
	app.before_first_request(bla)

	from .services import init_app
	init_app(app)

	import logging
	logger = logging.getLogger('peewee')
	logger.setLevel(logging.DEBUG)
	logger.addHandler(logging.StreamHandler())
	return app

