import unittest

from app import create_app
from json import dumps, loads
class ModCabritoTestCase(unittest.TestCase):
	def setUp(self):
		print 'setUp'
		self.app = create_app().test_client()

	def tearDown(self):
		print 'tearDown'

	def post_json(self, url_suffix, data):
		rv = self.app.post(
			'/rest'+url_suffix,
			content_type='application/json',
			data=dumps(data), 
		)
		return rv

	def test_user_register(self):
		data = dict(
			name='Felipe Blassioli',
			email='felipeblassioli@gmail.com'
		)
		rv = self.post_json('/user/',data)
		user = loads(rv.data)

		rv = self.app.get('/rest/user/'+str(user['id']))
		print rv.data

	def test_newclient_do_first_payment(self):
		rv = self.app.get('/tablet/')
		#print rv.data

if __name__ == '__main__':
    unittest.main(verbosity=2)