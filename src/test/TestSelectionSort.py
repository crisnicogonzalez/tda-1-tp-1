import unittest
from src.sort.selection_sort import sort
from src.sort.sort_validator import check_order

class TestSelectionSort(unittest.TestCase):
    def test_empty_list(self):
        empty_list = []
        sort(empty_list)
        self.assertTrue(check_order(empty_list))

    def test_a_element(self):
        a_element = [1]
        sort(a_element)
        self.assertTrue(check_order(a_element))


    def test_many_elements(self):
        a_list = [1, 3, 2, 3, 4, 43, 4, 54, 6, 5, 5, 6, 65, 65]
        self.assertFalse(check_order(a_list))
        sort(a_list)
        self.assertTrue(check_order(a_list))
        