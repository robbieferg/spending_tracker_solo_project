import unittest
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

class TestTransaction(unittest.TestCase):

    def test_transaction_has_values(self):
        merchant_1 = Merchant("Tesco", "Supermarket")
        tag_1 = Tag("Groceries")
        transaction_1 = Transaction("03/12/2021", "15:31", 12.50, merchant_1, tag_1)
        self.assertEqual("03/12/2021", transaction_1.date)
        self.assertEqual("15:31", transaction_1.time)
        self.assertEqual(12.50, transaction_1.amount_spent)
        self.assertEqual("Tesco", transaction_1.merchant.name)
        self.assertEqual("Supermarket", transaction_1.merchant.description)
        self.assertEqual("Groceries", transaction_1.tag.name)
        self.assertEqual(None, transaction_1.id)
        