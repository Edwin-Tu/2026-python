"""Stage 1 — @timeit 裝飾器測試骨架

規格:timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫後更新 f.last_elapsed(float 秒)並 append 到 f.records
  4. 裝飾器內不准 print

待辦:
  1. 自己打提示詞跟 AI 討論,補齊下面三個測試(可再加)
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: stage1 timeit 裝飾器測試"
  4. 寫 timing.py,全綠後 commit: "feat: stage1 實作 timeit 裝飾器"
"""

import unittest
from unittest.mock import patch

from timing import timeit  # 完成 timing.py 後解除註解


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)

    def test_returns_none_result(self):
        @timeit
        def do_nothing():
            return None

        self.assertIsNone(do_nothing())

    def test_preserves_function_metadata(self):
        @timeit
        def sample_function():
            """Sample docstring."""
            return "done"

        self.assertEqual(sample_function.__name__, "sample_function")
        self.assertEqual(sample_function.__doc__, "Sample docstring.")

    def test_records_elapsed_time(self):
        @timeit
        def identity(value):
            return value

        self.assertEqual(identity.records, [])

        identity("first")
        self.assertIsInstance(identity.last_elapsed, float)
        self.assertGreaterEqual(identity.last_elapsed, 0)
        self.assertEqual(len(identity.records), 1)
        self.assertEqual(identity.records[-1], identity.last_elapsed)

        first_elapsed = identity.last_elapsed
        identity("second")
        self.assertIsInstance(identity.last_elapsed, float)
        self.assertEqual(len(identity.records), 2)
        self.assertEqual(identity.records[0], first_elapsed)
        self.assertEqual(identity.records[-1], identity.last_elapsed)

    def test_does_not_print(self):
        @timeit
        def greet(name):
            return f"Hello, {name}"

        with patch("builtins.print") as mock_print:
            self.assertEqual(greet("Ada"), "Hello, Ada")

        mock_print.assert_not_called()


if __name__ == "__main__":
    unittest.main()
