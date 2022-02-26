import unittest

from ghc_binary_tree import GHCBinaryTree

class TestGHCBinaryTree(unittest.TestCase):
    def test_is_tree_empty(self):
        my_tree = GHCBinaryTree()
        self.assertTrue(my_tree.is_empty())

    def test_is_tree_not_empty(self):
        my_tree = GHCBinaryTree()
        my_tree.add(1)
        self.assertFalse(my_tree.is_empty())
