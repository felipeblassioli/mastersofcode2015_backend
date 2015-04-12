import unittest

from app import create_app

class ModCabritoTestCase(unittest.TestCase):
	def setUp(self):
		print 'setUp'
		self.app = create_app().test_client()

	def tearDown(self):
		print 'tearDown'

class NewClientFirstPayment(ModCabritoTestCase):
	def test_newclient_do_first_payment(self):
		rv = self.app.get('/tablet/')
		print rv.data

if __name__ == '__main__':
    unittest.main(verbosity=2)