from peewee import *

db = SqliteDatabase('people.db')


class BaseModel(Model):
	class Meta:
		database = db

class User(BaseModel):
	name = CharField()
	email = CharField()
	customer_id = CharField(null=True)

	def to_json(self):
		return self.__dict__['_data']

def before_request_handler():
	db.connect()

def after_request_handler(*args,**kwargs):
	print args, kwargs
	db.close()

def init_app(app):
	app.before_request(before_request_handler)
	#app.after_request(after_request_handler)
	app.teardown_request(after_request_handler)