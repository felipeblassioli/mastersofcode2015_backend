from peewee import *

db = SqliteDatabase('people.db')


class BaseModel(Model):
	def to_json(self):
		return self.__dict__['_data']

	def __str__(self):
		return 'Model:'+str(self.to_json())

	def __repr__(self):
		return str(self)

	class Meta:
		database = db

class User(BaseModel):
	name = CharField()
	email = CharField()
	customer_id = CharField(null=True)

	
def before_request_handler():
	db.connect()

def after_request_handler(*args,**kwargs):
	print args, kwargs
	db.close()

def setup_db():
	for m in [User]:
		m.create_table(True)

def init_app(app):
	app.before_first_request(setup_db)
	app.before_request(before_request_handler)
	#app.after_request(after_request_handler)
	app.teardown_request(after_request_handler)