"""
Plik z testami sortowania. Wykorzystany z własnego githuba (https://github.com/dkilian01/Testowanie_01/blob/main/test_sorting.py)
"""

import unittest

from sorting_algorithms import insert_sort, merge_sort, _merge


SORTING_FUNCTIONS = [
    insert_sort,
    merge_sort,
]


class TestSortingAlgorithms(unittest.TestCase):
    """
    Testy jednostkowe dla obu algorytmów sortowania.
    Te same przypadki są wykonywane dla insert_sort oraz merge_sort.
    """

    def test_empty_list(self):
        for sort_function in SORTING_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(sort_function([]), [])

    def test_single_element(self):
        for sort_function in SORTING_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(sort_function([5]), [5])

    def test_already_sorted_list(self):
        for sort_function in SORTING_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(sort_function([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        for sort_function in SORTING_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(sort_function([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        for sort_function in SORTING_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(sort_function([4, 2, 5, 1, 3]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        for sort_function in SORTING_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(sort_function([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_negative_numbers(self):
        for sort_function in SORTING_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(sort_function([-1, -5, 3, 0, 2]), [-5, -1, 0, 2, 3])

    def test_float_numbers(self):
        for sort_function in SORTING_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(sort_function([2.5, 1.1, 3.3, 1.0]), [1.0, 1.1, 2.5, 3.3])

    def test_tuple_input(self):
        for sort_function in SORTING_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                self.assertEqual(sort_function((3, 2, 1)), [1, 2, 3])

    def test_generator_input(self):
        for sort_function in SORTING_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                data = (number for number in [3, 1, 2])
                self.assertEqual(sort_function(data), [1, 2, 3])

    def test_original_list_is_not_modified(self):
        for sort_function in SORTING_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                data = [3, 1, 2]
                sorted_data = sort_function(data)

                self.assertEqual(sorted_data, [1, 2, 3])
                self.assertEqual(data, [3, 1, 2])

    def test_none_input_raises_type_error(self):
        for sort_function in SORTING_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                with self.assertRaises(TypeError):
                    sort_function(None)

    def test_string_input_raises_type_error(self):
        for sort_function in SORTING_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                with self.assertRaises(TypeError):
                    sort_function("321")

    def test_non_iterable_input_raises_type_error(self):
        for sort_function in SORTING_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                with self.assertRaises(TypeError):
                    sort_function(123)

    def test_mixed_uncomparable_types_raise_type_error(self):
        for sort_function in SORTING_FUNCTIONS:
            with self.subTest(sort_function=sort_function.__name__):
                with self.assertRaises(TypeError):
                    sort_function([1, "a", 3])


class TestMergeHelper(unittest.TestCase):
    """
    Testy funkcji pomocniczej _merge.
    """

    def test_merge_two_non_empty_lists(self):
        self.assertEqual(_merge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_merge_when_left_has_remaining_elements(self):
        self.assertEqual(_merge([1, 2, 10], [3]), [1, 2, 3, 10])

    def test_merge_when_right_has_remaining_elements(self):
        self.assertEqual(_merge([3], [1, 2, 10]), [1, 2, 3, 10])

    def test_merge_empty_left_list(self):
        self.assertEqual(_merge([], [1, 2, 3]), [1, 2, 3])

    def test_merge_empty_right_list(self):
        self.assertEqual(_merge([1, 2, 3], []), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
