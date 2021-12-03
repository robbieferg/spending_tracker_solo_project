import unittest
from models.merchant import Merchant

class TestMerchant(unittest.TestCase):

    def test_merchant_has_values(self):
        merchant_1 = Merchant("Asda", "Supermarket") 
        self.assertEqual("Asda", merchant_1.name)
        self.assertEqual("Supermarket", merchant_1.description)
        self.assertEqual(None, merchant_1.id)