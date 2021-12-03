import unittest
from models.merchant import Merchant

class TestMerchant(unittest.TestCase):

    def test_merchant_has_values(self):
        merchant_1 = Merchant("Asda", "Supermarket") 
        self.assertEqual(merchant_1.name, "Asda")
        self.assertEqual(merchant_1.description, "Supermarket")
        self.assertEqual(merchant_1.id, None)