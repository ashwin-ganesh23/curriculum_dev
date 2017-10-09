import unittest
from my_math_module import add, multiply

class TestMM(unittest.TestCase):

	def setUp(self):
		pass

	def test_add(self):
		print(self.assertEqual(add(5, 6), 11))
		self.assertEqual(add(-5, 6), 1)
		self.assertEqual(add('a', 'b'), 'ab')
		self.assertEqual(add(16, 22), 38)

	def test_multiply(self):
		self.assertEqual(multiply(5, 6), 30)
		self.assertEqual(multiply(-5, 6), -30)
		self.assertEqual(multiply('a', 2), 'aa')
		self.assertEqual(multiply('b', 4), 'bbbb')
		self.assertEqual(multiply(100, 17), 1700)
		self.assertEqual(multiply(52, 4), 208)

if __name__ == '__main__':
	unittest.main()
