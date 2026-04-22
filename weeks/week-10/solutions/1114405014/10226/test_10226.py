import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from main_annotated import solve, generate_permutations, output_diff

class TestUVA10226(unittest.TestCase):
    def test_basic_permutation(self):
        """測試基本排列生成"""
        result = generate_permutations(2, {0: [], 1: []})
        expected = ['AB', 'BA']
        self.assertEqual(result, expected)

    def test_with_forbidden_positions(self):
        """測試帶有禁止位置的排列"""
        result = generate_permutations(2, {0: [0], 1: [1]})
        expected = ['BA']
        self.assertEqual(result, expected)

    def test_three_elements(self):
        """測試三個元素的所有排列"""
        result = generate_permutations(3, {0: [], 1: [], 2: []})
        expected = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
        self.assertEqual(result, expected)

    def test_output_diff(self):
        """測試輸出差異部分"""
        prev = "ABC"
        curr = "ABD"
        result = output_diff(prev, curr)
        self.assertEqual(result, "D")

        prev = "ABC"
        curr = "ADC"
        result = output_diff(prev, curr)
        self.assertEqual(result, "D")

        prev = "ABC"
        curr = "ABC"
        result = output_diff(prev, curr)
        self.assertEqual(result, "")

    def test_no_valid_permutations(self):
        """測試無有效排列的情況"""
        result = generate_permutations(2, {0: [0, 1], 1: [0, 1]})
        expected = []
        self.assertEqual(result, expected)

    def test_solve_simple(self):
        """測試簡單輸入的solve函數"""
        input_data = "1\n2\n0\n0\n"
        import io
        import sys
        sys.stdin = io.StringIO(input_data)
        result = solve()
        expected = "AB\nB\n"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
