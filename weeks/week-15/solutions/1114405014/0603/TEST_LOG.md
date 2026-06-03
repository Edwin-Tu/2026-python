# Red (Fail)
======================================================================
FAIL: test_n_2_should_return_1 (test_gcd_basic.TestGCDBasic.test_n_2_should_return_1)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Edwin\program\program-python\2026-python\weeks\week-15\solutions\1114405014\0603\test_gcd_basic.py", line 8, in test_n_2_should_return_1
    self.assertEqual(sum_of_gcd(2), 1)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
AssertionError: None != 1

======================================================================
FAIL: test_n_1_should_return_0 (test_gcd_edge.TestGCDEdgeCase.test_n_1_should_return_0)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Edwin\program\program-python\2026-python\weeks\week-15\solutions\1114405014\0603\test_gcd_edge.py", line 8, in test_n_1_should_return_0
    self.assertEqual(sum_of_gcd(1), 0)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
AssertionError: None != 0

# Green (Success)
----------------------------------------------------------------------
Ran 2 tests in 0.002s

FAILED (failures=2)


..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
