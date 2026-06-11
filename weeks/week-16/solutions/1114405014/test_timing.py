import io
import time
import unittest
from contextlib import redirect_stdout

from timing import timeit


class TestTimeitDecorator(unittest.TestCase):
    def test_timeit_preserves_return_value(self):
        @timeit
        def add(a, b):
            return a + b

        result = add(2, 3)

        self.assertEqual(result, 5)

    def test_timeit_records_last_elapsed_and_records(self):
        @timeit
        def tiny_work():
            time.sleep(0.001)
            return "done"

        tiny_work()
        tiny_work()

        self.assertTrue(hasattr(tiny_work, "last_elapsed"))
        self.assertTrue(hasattr(tiny_work, "records"))
        self.assertIsInstance(tiny_work.last_elapsed, float)
        self.assertIsInstance(tiny_work.records, list)
        self.assertEqual(len(tiny_work.records), 2)
        self.assertEqual(tiny_work.last_elapsed, tiny_work.records[-1])
        self.assertGreaterEqual(tiny_work.last_elapsed, 0)

    def test_timeit_preserves_function_metadata(self):
        @timeit
        def sample_function():
            """sample docstring"""
            return "ok"

        self.assertEqual(sample_function.__name__, "sample_function")
        self.assertEqual(sample_function.__doc__, "sample docstring")

    def test_timeit_does_not_print(self):
        @timeit
        def quiet_function():
            return "quiet"

        output = io.StringIO()

        with redirect_stdout(output):
            result = quiet_function()

        self.assertEqual(result, "quiet")
        self.assertEqual(output.getvalue(), "")


if __name__ == "__main__":
    unittest.main()