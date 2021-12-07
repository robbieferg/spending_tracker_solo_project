import unittest
from models.budget import Budget

class TestBudget(unittest.TestCase):

    def test_budget_has_values(self):
        budget_1 = Budget("Daily", 45.55)
        self.assertEqual("Daily", budget_1.budget_type)
        self.assertEqual(45.55, budget_1.budget_amount)