import unittest

from sorts import bubble_sort, quick_sort, merge_sort


SORT_FUNCTIONS = [
    bubble_sort,
    quick_sort,
    merge_sort,
]


class TestSortingAlgorithms(unittest.TestCase):
    def test_sort_positive_numbers(self):
        data = [5, 3, 1, 4, 2]
        expected = [1, 2, 3, 4, 5]

        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
                self.assertEqual(sort_func(data), expected)

    def test_sort_with_duplicates(self):
        data = [4, 2, 4, 1, 2]
        expected = [1, 2, 2, 4, 4]

        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
                self.assertEqual(sort_func(data), expected)

    def test_sort_with_negative_numbers(self):
        data = [3, -1, 0, -5, 2]
        expected = [-5, -1, 0, 2, 3]

        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
                self.assertEqual(sort_func(data), expected)

    def test_sort_empty_and_single_item_list(self):
        cases = [
            ([], []),
            ([7], [7]),
        ]

        for sort_func in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
                    self.assertEqual(sort_func(data), expected)

    def test_sort_does_not_modify_input_list(self):
        original = [3, 1, 2]

        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
                data = original.copy()
                result = sort_func(data)

                self.assertEqual(result, [1, 2, 3])
                self.assertEqual(data, original)
                self.assertIsNot(result, data)


if __name__ == "__main__":
    unittest.main()