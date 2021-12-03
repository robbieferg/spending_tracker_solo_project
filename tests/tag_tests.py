import unittest
from models.tag import Tag

class TestTag(unittest.TestCase):

    def test_tag_has_values(self):
        tag_1 = Tag("Groceries")
        self.assertEqual("Groceries", tag_1.name)
        self.assertEqual(None, tag_1.id)