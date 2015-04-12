from peewee import *

from flask import current_app
from . import db
#db = SqliteDatabase('people.db')
#db = MySQLDatabase("hackathon", user="root", passwd="algebra2")
class BaseModel(db.Model):
	def to_json(self):
		return self.__dict__['_data']

	def __str__(self):
		return 'Model:'+str(self.to_json())

	def __repr__(self):
		return str(self)

	# class Meta:
	# 	database = db

import simplify
simplify.public_key = "sbpb_MjM2NWQ2MmUtZWVmZC00Nzk1LTg2ZDctMzUzMDE0ZjE5YzEz"
simplify.private_key = "3bKNdnkpjOFnTDqZFAz7+ot+SMI5D8TPiIsNda20ySt5YFFQL0ODSXAOkNtXTToq"

from json import dumps,loads

class User(BaseModel):
	name = CharField()
	email = CharField(unique=True)
	customer_id = CharField(null=True)

	@classmethod
	def create(self,*args,**kwargs):
		ret = super(User,self).create(*args,**kwargs)
		customer = simplify.Customer.create({
			"email" : ret.email,
			"name" : ret.name,
			"reference" : ret.id
		})
		ret.customer_id = customer['id']
		ret.save()
		return ret

	def send_invoice(self, itemsList):
		data = dict(
			items=itemsList,
			customer=self.customer_id
		)
		invoice = simplify.Invoice.create(data)
		ret = Invoice.create(
			invoice_id=invoice['id'],
			user=self,
			body=str(invoice)
		)
		return ret

class Invoice(BaseModel):
	invoice_id = CharField()
	user = ForeignKeyField(User, related_name='invoices2')
	body = TextField()

	def to_json(self):
		return loads(self.body)

# invoice = simplify.Invoice.create({
#     "memo" : "This is a memo",
#     "items" : [
#         {
#             "amount" : "5504",
#             #"tax" : "[TAX ID]",
#             "quantity" : "1"
#         }
#     ],
#     "email" : "felipeblassioli@gmail.com",
#     "name" : "Felipe Blassioli",
#     "suppliedDate" : "2394839384000",
#     "note" : "This is a note",
#     "reference" : "Ref2",
#     "currency" : "USD"
# })

def before_request_handler():
	db.connect()

def after_request_handler(*args,**kwargs):
	print args, kwargs
	if db is not None:
		db.close()

def setup_db():
	for m in [User, Invoice]:
		m.create_table(True)

#app.before_first_request(setup_db)
def init_app(app):

	app.before_request(before_request_handler)
	#app.after_request(after_request_handler)
	app.teardown_request(after_request_handler)