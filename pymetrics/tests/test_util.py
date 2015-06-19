import unittest

from pymetrics.util import coalesce

#
# COALESCE
#

class TestCoalesce(unittest.TestCase):
    def test_empty(self):
        self.assertIs(None, coalesce())

    def test_None(self):
        self.assertIs(None, coalesce(None))

    def test_all_None(self):
        self.assertIs(None, coalesce(None, None))

    def test_first_not_None(self):
        self.assertIs('first', coalesce('first', None))

    def test_nth_not_None(self):
        self.assertIs('second', coalesce(None, 'second'))

###

if __name__ == '__main__':
    unittest.main()
