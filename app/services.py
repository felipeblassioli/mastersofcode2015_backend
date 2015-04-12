from peewee import *

class User(object):
	def to_json(self):
		return dict(
			name='bla',
			email='x'
		)