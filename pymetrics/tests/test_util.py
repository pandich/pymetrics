import unittest

from pymetrics.util import issubclass_recursive
from pymetrics.util import coalesce


#
# IS_SUBCLASS_RECURSIVE
#

# noinspection PyStatementEffect
class Parent:
    def __init__(self):
        None


# noinspection PyStatementEffect
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)


# noinspection PyStatementEffect
class Grandchild(Child):
    def __init__(self):
        Child.__init__(self)


# noinspection PyStatementEffect
class Stranger:
    def __init__(self):
        None


class TestIsSubClassRecursiveDescendant(unittest.TestCase):
    def test_immediate_descendant(self):
        self.assertIs(True, issubclass_recursive(Child(), Parent()))

    def test_transitive_descendant(self):
        self.assertIs(True, issubclass_recursive(Grandchild(), Parent()))

    def test_not_a_descendant(self):
        self.assertIs(False, issubclass_recursive(Stranger(), Parent()))

    def test_None_descendant(self):
        self.assertIs(False, issubclass_recursive(None, Parent()))

    def test_None_parent(self):
        self.assertIs(False, issubclass_recursive(Stranger(), None))


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
