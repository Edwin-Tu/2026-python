import unittest


class TestTrainSwapping(unittest.TestCase):
    def test_already_sorted(self):
        self.assertEqual(count_swaps([1, 2, 3]), 0)
        self.assertEqual(count_swaps([1]), 0)

    def test_reverse_sorted(self):
        self.assertEqual(count_swaps([3, 2, 1]), 3)
        self.assertEqual(count_swaps([4, 3, 2, 1]), 6)

    def test_single_swap_needed(self):
        self.assertEqual(count_swaps([1, 3, 2]), 1)
        self.assertEqual(count_swaps([2, 1, 3]), 1)

    def test_multiple_swaps_needed(self):
        self.assertEqual(count_swaps([2, 3, 1]), 2)
        self.assertEqual(count_swaps([3, 1, 2]), 2)

    def test_complex_case(self):
        self.assertEqual(count_swaps([4, 2, 3, 1]), 5)

    def test_empty_train(self):
        self.assertEqual(count_swaps([]), 0)

    def test_two_cars(self):
        self.assertEqual(count_swaps([1, 2]), 0)
        self.assertEqual(count_swaps([2, 1]), 1)

    def test_sample_input(self):
        self.assertEqual(count_swaps([1, 3, 2]), 1)
        self.assertEqual(count_swaps([3, 2, 1]), 3)

    def test_max_length(self):
        reverse_50 = list(range(50, 0, -1))
        self.assertEqual(count_swaps(reverse_50), 1225)


def count_swaps(train):
    if not train:
        return 0

    cars = train[:]
    swaps = 0

    n = len(cars)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cars[j] > cars[j + 1]:
                cars[j], cars[j + 1] = cars[j + 1], cars[j]
                swaps += 1

    return swaps


if __name__ == '__main__':
    unittest.main()