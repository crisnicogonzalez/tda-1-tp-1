import unittest
from src.algorithm.insertion_sort import sort
from src.utils.sort_validator import check_order


class TestInsertionSort(unittest.TestCase):
    def test_empty_list(self):
        empty_list = []
        self.assertTrue(check_order(sort(empty_list)))

    def test_a_element(self):
        a_element = [1]
        self.assertTrue(check_order(sort(a_element)))

    def test_few_elements(self):
        list_with_few_elements = [6, 5, 4, 3, 2, 1]
        self.assertFalse(check_order(list_with_few_elements))
        self.assertTrue(check_order(sort(list_with_few_elements)))

    def test_few_elements_again(self):
        list_with_few_elements = [6, 5, 3, 1, 8, 7, 2, 4]
        self.assertFalse(check_order(list_with_few_elements))
        self.assertTrue(check_order(sort(list_with_few_elements)))

    def test_many_elements(self):
        a_list = [1, 3, 2, 3, 4, 43, 4, 54, 6, 5, 5, 6, 65, 65]
        self.assertFalse(check_order(a_list))
        self.assertTrue(check_order(sort(a_list)))
