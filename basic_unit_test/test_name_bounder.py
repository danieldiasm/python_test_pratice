import unittest
from name_bonder import bound_names_together

class NameBoundTest(unittest.TestCase):

    def test_simple_name_bound(self):
        full_name = bound_names_together('bob', 'marley')
        self.assertEqual(full_name, 'Bob Marley')

unittest.main()