import unittest


class TestCollatzCycleLength(unittest.TestCase):
    def test_cycle_length_of_1(self):
        self.assertEqual(cycle_length(1), 1)

    def test_cycle_length_of_2(self):
        self.assertEqual(cycle_length(2), 2)

    def test_cycle_length_of_3(self):
        self.assertEqual(cycle_length(3), 8)

    def test_cycle_length_of_22(self):
        self.assertEqual(cycle_length(22), 16)

    def test_cycle_length_of_9(self):
        self.assertEqual(cycle_length(9), 20)

    def test_max_cycle_length_single_number(self):
        self.assertEqual(max_cycle_length(1, 1), 1)
        self.assertEqual(max_cycle_length(2, 2), 2)
        self.assertEqual(max_cycle_length(22, 22), 16)

    def test_max_cycle_length_range_1_to_10(self):
        self.assertEqual(max_cycle_length(1, 10), 20)

    def test_max_cycle_length_range_100_to_200(self):
        result = max_cycle_length(100, 200)
        self.assertGreaterEqual(result, 20)

    def test_max_cycle_length_i_greater_than_j(self):
        self.assertEqual(max_cycle_length(10, 1), max_cycle_length(1, 10))

    def test_process_input_output(self):
        i, j = 1, 10
        max_len = max_cycle_length(i, j)
        expected_output = f"{i} {j} {max_len}"
        self.assertEqual(expected_output, "1 10 20")


def cycle_length(n):
    count = 1
    while n != 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        count += 1
    return count


def max_cycle_length(i, j):
    if i > j:
        i, j = j, i

    max_len = 0
    for num in range(i, j + 1):
        current_len = cycle_length(num)
        if current_len > max_len:
            max_len = current_len
    return max_len


if __name__ == '__main__':
    unittest.main()