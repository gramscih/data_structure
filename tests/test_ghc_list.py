import unittest

from ghc_list import GHCList

class TestGHCList(unittest.TestCase):
    def test_is_empty(self):
        my_list = GHCList()
        self.assertTrue(my_list.is_empty())

    def test_is_not_empty(self):
        my_list = GHCList()
        my_list.add('some value')
        self.assertFalse(my_list.is_empty())

    def test_add_element(self):
        my_list = GHCList()
        my_list.add("first value")
        self.assertNotEqual(my_list[0], None)

    def test_add_more_than_one_item(self):
        my_list = GHCList()
        my_list.add(1)
        my_list.add(2)
        my_list.add(3)
        my_list.add(4)
        my_list.add("other type")
        self.assertEqual(my_list[1], 2)
        self.assertEqual(my_list[3], 4)
        self.assertEqual(my_list[2], 3)
        self.assertEqual(my_list[4], "other type")

    def test_set_item(self):
        my_list = GHCList()
        my_list.add("first")
        my_list.add("second")
        my_list.add("third")
        self.assertEqual(my_list[1], "second")
        self.assertEqual(my_list[0], "first")
        my_list[1] = 2
        self.assertEqual(my_list[1], 2)

    def test_get_firts_item(self):
        my_list = GHCList()
        my_list.add("first value")
        self.assertEqual(my_list[0], "first value")

    def test_find_item(self):
        my_list = GHCList()
        my_list.add("item")
        self.assertEqual(my_list.find("item"), 0)

    def test_find_middle_item(self):
        my_list = GHCList()
        my_list.add("item")
        my_list.add("item2")
        my_list.add("item3")
        self.assertEqual(my_list.find("item2"), 1)
        self.assertEqual(my_list.find("item3"), 2)

    def test_list_size(self):
        my_list = GHCList()
        my_list.add("item")
        my_list.add("item2")
        my_list.add("item3")
        self.assertEqual(my_list.size(), 3)

    def test_empty_list_size(self):
        my_list = GHCList()
        self.assertEqual(my_list.size(), 0)

    def test_list_to_str(self):
        my_list = GHCList()
        my_list.add("Hello")
        my_list.add("World")
        self.assertEqual(str(my_list), "Hello World ")
