import unittest

import stox.stox


class TestCompany(unittest.TestCase):

  def test_get_stock_price(self):
      self.assertEqual(stox.stox.Company('goog').get_stock_price(), 9.99)


if __name__ == '__main__':
    unittest.main()