# encoding: utf-8
from flask import Flask, Blueprint, render_template, request


from flask import current_app
def bla():
	print current_app.url_map

from flask.json import JSONEncoder
class CustomJSONEncoder(JSONEncoder):
	def default(self, obj):
		if hasattr(obj, 'to_json'):
			return obj.to_json()
		try:
			iterable = iter(obj)
		except TypeError:
			pass
		else:
			return list(iterable)
		return JSONEncoder.default(self, obj)

def create_app():
	app = Flask(__name__)
	app.json_encoder = CustomJSONEncoder
	from .tablet import tablet
	app.register_blueprint(tablet, url_prefix='/tablet')

	from .rest import rest
	app.register_blueprint(rest, url_prefix='/rest')
	app.before_first_request(bla)
	return app

