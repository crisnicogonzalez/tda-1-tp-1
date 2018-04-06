import unittest
from src.sort.merge_sort import sort
from src.utils.sort_validator import check_order


class TestInsertionSort(unittest.TestCase):
    def test_empty_list(self):
        empty_list = []
        self.assertEqual(empty_list, sort(empty_list))

    def test_a_element(self):
        self.assertEqual([1], sort([1]))

    def test_few_elements(self):
        list_with_few_elements = [6, 5, 4, 3, 2, 1]
        self.assertFalse(check_order(list_with_few_elements))
        self.assertTrue(check_order(sort(list_with_few_elements)))

    def test_many_elements(self):
        a_list = [1, 3, 2, 3, 4, 43, 4, 54, 6, 5, 5, 6, 65, 65]
        self.assertFalse(check_order(a_list))
        sort(a_list)
        self.assertTrue(check_order(a_list))
