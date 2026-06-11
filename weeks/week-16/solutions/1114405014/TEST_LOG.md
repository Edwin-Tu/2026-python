pytest
PS D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014> pytest
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014
plugins: anyio-4.13.0
collected 10 items                                                                                    

test_sorts.py uuu.uuuuuu.uuu.uuu.uuu.                                                           [ 50%]
test_timing.py uuu.uuuuuu.uuu.uuu.uuu.                                                          [100%]

============================================== FAILURES ==============================================
________ TestSortingAlgorithms.test_sort_does_not_modify_input_list (sort_func='bubble_sort') ________

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_does_not_modify_input_list>

    def test_sort_does_not_modify_input_list(self):
        original = [3, 1, 2]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
                data = original.copy()
                result = sort_func(data)
    
>               self.assertEqual(result, [1, 2, 3])
E               AssertionError: None != [1, 2, 3]

test_sorts.py:57: AssertionError
________ TestSortingAlgorithms.test_sort_does_not_modify_input_list (sort_func='quick_sort') _________

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_does_not_modify_input_list>

    def test_sort_does_not_modify_input_list(self):
        original = [3, 1, 2]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
                data = original.copy()
                result = sort_func(data)
    
>               self.assertEqual(result, [1, 2, 3])
E               AssertionError: None != [1, 2, 3]

test_sorts.py:57: AssertionError
________ TestSortingAlgorithms.test_sort_does_not_modify_input_list (sort_func='merge_sort') _________

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_does_not_modify_input_list>

    def test_sort_does_not_modify_input_list(self):
        original = [3, 1, 2]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
                data = original.copy()
                result = sort_func(data)
    
>               self.assertEqual(result, [1, 2, 3])
E               AssertionError: None != [1, 2, 3]

test_sorts.py:57: AssertionError
___ TestSortingAlgorithms.test_sort_empty_and_single_item_list (sort_func='bubble_sort', data=[]) ____

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_empty_and_single_item_list>

    def test_sort_empty_and_single_item_list(self):
        cases = [
            ([], []),
            ([7], [7]),
        ]
    
        for sort_func in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
>                   self.assertEqual(sort_func(data), expected)
E                   AssertionError: None != []

test_sorts.py:47: AssertionError
___ TestSortingAlgorithms.test_sort_empty_and_single_item_list (sort_func='bubble_sort', data=[7]) ___

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_empty_and_single_item_list>

    def test_sort_empty_and_single_item_list(self):
        cases = [
            ([], []),
            ([7], [7]),
        ]
    
        for sort_func in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
>                   self.assertEqual(sort_func(data), expected)
E                   AssertionError: None != [7]

test_sorts.py:47: AssertionError
____ TestSortingAlgorithms.test_sort_empty_and_single_item_list (sort_func='quick_sort', data=[]) ____

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_empty_and_single_item_list>

    def test_sort_empty_and_single_item_list(self):
        cases = [
            ([], []),
            ([7], [7]),
        ]
    
        for sort_func in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
>                   self.assertEqual(sort_func(data), expected)
E                   AssertionError: None != []

test_sorts.py:47: AssertionError
___ TestSortingAlgorithms.test_sort_empty_and_single_item_list (sort_func='quick_sort', data=[7]) ____

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_empty_and_single_item_list>

    def test_sort_empty_and_single_item_list(self):
        cases = [
            ([], []),
            ([7], [7]),
        ]
    
        for sort_func in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
>                   self.assertEqual(sort_func(data), expected)
E                   AssertionError: None != [7]

test_sorts.py:47: AssertionError
____ TestSortingAlgorithms.test_sort_empty_and_single_item_list (sort_func='merge_sort', data=[]) ____

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_empty_and_single_item_list>

    def test_sort_empty_and_single_item_list(self):
        cases = [
            ([], []),
            ([7], [7]),
        ]
    
        for sort_func in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
>                   self.assertEqual(sort_func(data), expected)
E                   AssertionError: None != []

test_sorts.py:47: AssertionError
___ TestSortingAlgorithms.test_sort_empty_and_single_item_list (sort_func='merge_sort', data=[7]) ____

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_empty_and_single_item_list>

    def test_sort_empty_and_single_item_list(self):
        cases = [
            ([], []),
            ([7], [7]),
        ]
    
        for sort_func in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
>                   self.assertEqual(sort_func(data), expected)
E                   AssertionError: None != [7]

test_sorts.py:47: AssertionError
_____________ TestSortingAlgorithms.test_sort_positive_numbers (sort_func='bubble_sort') _____________

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_positive_numbers>

    def test_sort_positive_numbers(self):
        data = [5, 3, 1, 4, 2]
        expected = [1, 2, 3, 4, 5]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [1, 2, 3, 4, 5]

test_sorts.py:20: AssertionError
_____________ TestSortingAlgorithms.test_sort_positive_numbers (sort_func='quick_sort') ______________

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_positive_numbers>

    def test_sort_positive_numbers(self):
        data = [5, 3, 1, 4, 2]
        expected = [1, 2, 3, 4, 5]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [1, 2, 3, 4, 5]

test_sorts.py:20: AssertionError
_____________ TestSortingAlgorithms.test_sort_positive_numbers (sort_func='merge_sort') ______________

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_positive_numbers>

    def test_sort_positive_numbers(self):
        data = [5, 3, 1, 4, 2]
        expected = [1, 2, 3, 4, 5]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [1, 2, 3, 4, 5]

test_sorts.py:20: AssertionError
_____________ TestSortingAlgorithms.test_sort_with_duplicates (sort_func='bubble_sort') ______________

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_with_duplicates>

    def test_sort_with_duplicates(self):
        data = [4, 2, 4, 1, 2]
        expected = [1, 2, 2, 4, 4]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [1, 2, 2, 4, 4]

test_sorts.py:28: AssertionError
______________ TestSortingAlgorithms.test_sort_with_duplicates (sort_func='quick_sort') ______________

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_with_duplicates>

    def test_sort_with_duplicates(self):
        data = [4, 2, 4, 1, 2]
        expected = [1, 2, 2, 4, 4]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [1, 2, 2, 4, 4]

test_sorts.py:28: AssertionError
______________ TestSortingAlgorithms.test_sort_with_duplicates (sort_func='merge_sort') ______________

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_with_duplicates>

    def test_sort_with_duplicates(self):
        data = [4, 2, 4, 1, 2]
        expected = [1, 2, 2, 4, 4]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [1, 2, 2, 4, 4]

test_sorts.py:28: AssertionError
__________ TestSortingAlgorithms.test_sort_with_negative_numbers (sort_func='bubble_sort') ___________

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_with_negative_numbers>

    def test_sort_with_negative_numbers(self):
        data = [3, -1, 0, -5, 2]
        expected = [-5, -1, 0, 2, 3]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [-5, -1, 0, 2, 3]

test_sorts.py:36: AssertionError
___________ TestSortingAlgorithms.test_sort_with_negative_numbers (sort_func='quick_sort') ___________

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_with_negative_numbers>

    def test_sort_with_negative_numbers(self):
        data = [3, -1, 0, -5, 2]
        expected = [-5, -1, 0, 2, 3]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [-5, -1, 0, 2, 3]

test_sorts.py:36: AssertionError
___________ TestSortingAlgorithms.test_sort_with_negative_numbers (sort_func='merge_sort') ___________

self = <test_sorts.TestSortingAlgorithms testMethod=test_sort_with_negative_numbers>

    def test_sort_with_negative_numbers(self):
        data = [3, -1, 0, -5, 2]
        expected = [-5, -1, 0, 2, 3]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [-5, -1, 0, 2, 3]

test_sorts.py:36: AssertionError
________ TestSortingAlgorithms.test_sort_does_not_modify_input_list (sort_func='bubble_sort') ________

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_does_not_modify_input_list>

    def test_sort_does_not_modify_input_list(self):
        original = [3, 1, 2]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
                data = original.copy()
                result = sort_func(data)
    
>               self.assertEqual(result, [1, 2, 3])
E               AssertionError: None != [1, 2, 3]

test_timing.py:57: AssertionError
________ TestSortingAlgorithms.test_sort_does_not_modify_input_list (sort_func='quick_sort') _________

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_does_not_modify_input_list>

    def test_sort_does_not_modify_input_list(self):
        original = [3, 1, 2]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
                data = original.copy()
                result = sort_func(data)
    
>               self.assertEqual(result, [1, 2, 3])
E               AssertionError: None != [1, 2, 3]

test_timing.py:57: AssertionError
________ TestSortingAlgorithms.test_sort_does_not_modify_input_list (sort_func='merge_sort') _________

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_does_not_modify_input_list>

    def test_sort_does_not_modify_input_list(self):
        original = [3, 1, 2]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
                data = original.copy()
                result = sort_func(data)
    
>               self.assertEqual(result, [1, 2, 3])
E               AssertionError: None != [1, 2, 3]

test_timing.py:57: AssertionError
___ TestSortingAlgorithms.test_sort_empty_and_single_item_list (sort_func='bubble_sort', data=[]) ____

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_empty_and_single_item_list>

    def test_sort_empty_and_single_item_list(self):
        cases = [
            ([], []),
            ([7], [7]),
        ]
    
        for sort_func in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
>                   self.assertEqual(sort_func(data), expected)
E                   AssertionError: None != []

test_timing.py:47: AssertionError
___ TestSortingAlgorithms.test_sort_empty_and_single_item_list (sort_func='bubble_sort', data=[7]) ___

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_empty_and_single_item_list>

    def test_sort_empty_and_single_item_list(self):
        cases = [
            ([], []),
            ([7], [7]),
        ]
    
        for sort_func in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
>                   self.assertEqual(sort_func(data), expected)
E                   AssertionError: None != [7]

test_timing.py:47: AssertionError
____ TestSortingAlgorithms.test_sort_empty_and_single_item_list (sort_func='quick_sort', data=[]) ____

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_empty_and_single_item_list>

    def test_sort_empty_and_single_item_list(self):
        cases = [
            ([], []),
            ([7], [7]),
        ]
    
        for sort_func in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
>                   self.assertEqual(sort_func(data), expected)
E                   AssertionError: None != []

test_timing.py:47: AssertionError
___ TestSortingAlgorithms.test_sort_empty_and_single_item_list (sort_func='quick_sort', data=[7]) ____

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_empty_and_single_item_list>

    def test_sort_empty_and_single_item_list(self):
        cases = [
            ([], []),
            ([7], [7]),
        ]
    
        for sort_func in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
>                   self.assertEqual(sort_func(data), expected)
E                   AssertionError: None != [7]

test_timing.py:47: AssertionError
____ TestSortingAlgorithms.test_sort_empty_and_single_item_list (sort_func='merge_sort', data=[]) ____

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_empty_and_single_item_list>

    def test_sort_empty_and_single_item_list(self):
        cases = [
            ([], []),
            ([7], [7]),
        ]
    
        for sort_func in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
>                   self.assertEqual(sort_func(data), expected)
E                   AssertionError: None != []

test_timing.py:47: AssertionError
___ TestSortingAlgorithms.test_sort_empty_and_single_item_list (sort_func='merge_sort', data=[7]) ____

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_empty_and_single_item_list>

    def test_sort_empty_and_single_item_list(self):
        cases = [
            ([], []),
            ([7], [7]),
        ]
    
        for sort_func in SORT_FUNCTIONS:
            for data, expected in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
>                   self.assertEqual(sort_func(data), expected)
E                   AssertionError: None != [7]

test_timing.py:47: AssertionError
_____________ TestSortingAlgorithms.test_sort_positive_numbers (sort_func='bubble_sort') _____________

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_positive_numbers>

    def test_sort_positive_numbers(self):
        data = [5, 3, 1, 4, 2]
        expected = [1, 2, 3, 4, 5]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [1, 2, 3, 4, 5]

test_timing.py:20: AssertionError
_____________ TestSortingAlgorithms.test_sort_positive_numbers (sort_func='quick_sort') ______________

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_positive_numbers>

    def test_sort_positive_numbers(self):
        data = [5, 3, 1, 4, 2]
        expected = [1, 2, 3, 4, 5]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [1, 2, 3, 4, 5]

test_timing.py:20: AssertionError
_____________ TestSortingAlgorithms.test_sort_positive_numbers (sort_func='merge_sort') ______________

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_positive_numbers>

    def test_sort_positive_numbers(self):
        data = [5, 3, 1, 4, 2]
        expected = [1, 2, 3, 4, 5]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [1, 2, 3, 4, 5]

test_timing.py:20: AssertionError
_____________ TestSortingAlgorithms.test_sort_with_duplicates (sort_func='bubble_sort') ______________

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_with_duplicates>

    def test_sort_with_duplicates(self):
        data = [4, 2, 4, 1, 2]
        expected = [1, 2, 2, 4, 4]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [1, 2, 2, 4, 4]

test_timing.py:28: AssertionError
______________ TestSortingAlgorithms.test_sort_with_duplicates (sort_func='quick_sort') ______________

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_with_duplicates>

    def test_sort_with_duplicates(self):
        data = [4, 2, 4, 1, 2]
        expected = [1, 2, 2, 4, 4]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [1, 2, 2, 4, 4]

test_timing.py:28: AssertionError
______________ TestSortingAlgorithms.test_sort_with_duplicates (sort_func='merge_sort') ______________

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_with_duplicates>

    def test_sort_with_duplicates(self):
        data = [4, 2, 4, 1, 2]
        expected = [1, 2, 2, 4, 4]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [1, 2, 2, 4, 4]

test_timing.py:28: AssertionError
__________ TestSortingAlgorithms.test_sort_with_negative_numbers (sort_func='bubble_sort') ___________

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_with_negative_numbers>

    def test_sort_with_negative_numbers(self):
        data = [3, -1, 0, -5, 2]
        expected = [-5, -1, 0, 2, 3]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [-5, -1, 0, 2, 3]

test_timing.py:36: AssertionError
___________ TestSortingAlgorithms.test_sort_with_negative_numbers (sort_func='quick_sort') ___________

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_with_negative_numbers>

    def test_sort_with_negative_numbers(self):
        data = [3, -1, 0, -5, 2]
        expected = [-5, -1, 0, 2, 3]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [-5, -1, 0, 2, 3]

test_timing.py:36: AssertionError
___________ TestSortingAlgorithms.test_sort_with_negative_numbers (sort_func='merge_sort') ___________

self = <test_timing.TestSortingAlgorithms testMethod=test_sort_with_negative_numbers>

    def test_sort_with_negative_numbers(self):
        data = [3, -1, 0, -5, 2]
        expected = [-5, -1, 0, 2, 3]
    
        for sort_func in SORT_FUNCTIONS:
            with self.subTest(sort_func=sort_func.__name__):
>               self.assertEqual(sort_func(data), expected)
E               AssertionError: None != [-5, -1, 0, 2, 3]

test_timing.py:36: AssertionError
====================================== short test summary info =======================================
SUBFAILED(sort_func='bubble_sort') test_sorts.py::TestSortingAlgorithms::test_sort_does_not_modify_input_list - AssertionError: None != [1, 2, 3]
SUBFAILED(sort_func='quick_sort') test_sorts.py::TestSortingAlgorithms::test_sort_does_not_modify_input_list - AssertionError: None != [1, 2, 3]
SUBFAILED(sort_func='merge_sort') test_sorts.py::TestSortingAlgorithms::test_sort_does_not_modify_input_list - AssertionError: None != [1, 2, 3]
SUBFAILED(sort_func='bubble_sort', data=[]) test_sorts.py::TestSortingAlgorithms::test_sort_empty_and_single_item_list - AssertionError: None != []
SUBFAILED(sort_func='bubble_sort', data=[7]) test_sorts.py::TestSortingAlgorithms::test_sort_empty_and_single_item_list - AssertionError: None != [7]
SUBFAILED(sort_func='quick_sort', data=[]) test_sorts.py::TestSortingAlgorithms::test_sort_empty_and_single_item_list - AssertionError: None != []
SUBFAILED(sort_func='quick_sort', data=[7]) test_sorts.py::TestSortingAlgorithms::test_sort_empty_and_single_item_list - AssertionError: None != [7]
SUBFAILED(sort_func='merge_sort', data=[]) test_sorts.py::TestSortingAlgorithms::test_sort_empty_and_single_item_list - AssertionError: None != []
SUBFAILED(sort_func='merge_sort', data=[7]) test_sorts.py::TestSortingAlgorithms::test_sort_empty_and_single_item_list - AssertionError: None != [7]
SUBFAILED(sort_func='bubble_sort') test_sorts.py::TestSortingAlgorithms::test_sort_positive_numbers - AssertionError: None != [1, 2, 3, 4, 5]
SUBFAILED(sort_func='quick_sort') test_sorts.py::TestSortingAlgorithms::test_sort_positive_numbers - AssertionError: None != [1, 2, 3, 4, 5]
SUBFAILED(sort_func='merge_sort') test_sorts.py::TestSortingAlgorithms::test_sort_positive_numbers - AssertionError: None != [1, 2, 3, 4, 5]
SUBFAILED(sort_func='bubble_sort') test_sorts.py::TestSortingAlgorithms::test_sort_with_duplicates - AssertionError: None != [1, 2, 2, 4, 4]
SUBFAILED(sort_func='quick_sort') test_sorts.py::TestSortingAlgorithms::test_sort_with_duplicates - AssertionError: None != [1, 2, 2, 4, 4]
SUBFAILED(sort_func='merge_sort') test_sorts.py::TestSortingAlgorithms::test_sort_with_duplicates - AssertionError: None != [1, 2, 2, 4, 4]
SUBFAILED(sort_func='bubble_sort') test_sorts.py::TestSortingAlgorithms::test_sort_with_negative_numbers - AssertionError: None != [-5, -1, 0, 2, 3]
SUBFAILED(sort_func='quick_sort') test_sorts.py::TestSortingAlgorithms::test_sort_with_negative_numbers - AssertionError: None != [-5, -1, 0, 2, 3]
SUBFAILED(sort_func='merge_sort') test_sorts.py::TestSortingAlgorithms::test_sort_with_negative_numbers - AssertionError: None != [-5, -1, 0, 2, 3]
SUBFAILED(sort_func='bubble_sort') test_timing.py::TestSortingAlgorithms::test_sort_does_not_modify_input_list - AssertionError: None != [1, 2, 3]
SUBFAILED(sort_func='quick_sort') test_timing.py::TestSortingAlgorithms::test_sort_does_not_modify_input_list - AssertionError: None != [1, 2, 3]
SUBFAILED(sort_func='merge_sort') test_timing.py::TestSortingAlgorithms::test_sort_does_not_modify_input_list - AssertionError: None != [1, 2, 3]
SUBFAILED(sort_func='bubble_sort', data=[]) test_timing.py::TestSortingAlgorithms::test_sort_empty_and_single_item_list - AssertionError: None != []
SUBFAILED(sort_func='bubble_sort', data=[7]) test_timing.py::TestSortingAlgorithms::test_sort_empty_and_single_item_list - AssertionError: None != [7]
SUBFAILED(sort_func='quick_sort', data=[]) test_timing.py::TestSortingAlgorithms::test_sort_empty_and_single_item_list - AssertionError: None != []
SUBFAILED(sort_func='quick_sort', data=[7]) test_timing.py::TestSortingAlgorithms::test_sort_empty_and_single_item_list - AssertionError: None != [7]
SUBFAILED(sort_func='merge_sort', data=[]) test_timing.py::TestSortingAlgorithms::test_sort_empty_and_single_item_list - AssertionError: None != []
SUBFAILED(sort_func='merge_sort', data=[7]) test_timing.py::TestSortingAlgorithms::test_sort_empty_and_single_item_list - AssertionError: None != [7]
SUBFAILED(sort_func='bubble_sort') test_timing.py::TestSortingAlgorithms::test_sort_positive_numbers - AssertionError: None != [1, 2, 3, 4, 5]
SUBFAILED(sort_func='quick_sort') test_timing.py::TestSortingAlgorithms::test_sort_positive_numbers - AssertionError: None != [1, 2, 3, 4, 5]
SUBFAILED(sort_func='merge_sort') test_timing.py::TestSortingAlgorithms::test_sort_positive_numbers - AssertionError: None != [1, 2, 3, 4, 5]
SUBFAILED(sort_func='bubble_sort') test_timing.py::TestSortingAlgorithms::test_sort_with_duplicates - AssertionError: None != [1, 2, 2, 4, 4]
SUBFAILED(sort_func='quick_sort') test_timing.py::TestSortingAlgorithms::test_sort_with_duplicates - AssertionError: None != [1, 2, 2, 4, 4]
SUBFAILED(sort_func='merge_sort') test_timing.py::TestSortingAlgorithms::test_sort_with_duplicates - AssertionError: None != [1, 2, 2, 4, 4]
SUBFAILED(sort_func='bubble_sort') test_timing.py::TestSortingAlgorithms::test_sort_with_negative_numbers - AssertionError: None != [-5, -1, 0, 2, 3]
SUBFAILED(sort_func='quick_sort') test_timing.py::TestSortingAlgorithms::test_sort_with_negative_numbers - AssertionError: None != [-5, -1, 0, 2, 3]
SUBFAILED(sort_func='merge_sort') test_timing.py::TestSortingAlgorithms::test_sort_with_negative_numbers - AssertionError: None != [-5, -1, 0, 2, 3]
=================================== 36 failed, 10 passed in 0.83s ====================================
pytest
PS D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014> pytest
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014
plugins: anyio-4.13.0
collected 10 items                                                                                    

test_sorts.py .....                                                                             [ 50%]
test_timing.py .....                                                                            [100%]

========================================= 10 passed in 0.09s =========================================

pytest
PS D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014> pytest
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014
plugins: anyio-4.13.0
collected 10 items / 1 error                                                                          

=============================================== ERRORS ===============================================
_________________________________ ERROR collecting test_banchmark.py _________________________________
ImportError while importing test module 'D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014\test_banchmark.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\hc105\AppData\Local\Python\pythoncore-3.14-64\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
test_banchmark.py:6: in <module>
    from benchmark import make_data, run_benchmark, save_results
E   ModuleNotFoundError: No module named 'benchmark'
====================================== short test summary info =======================================
ERROR test_banchmark.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
========================================== 1 error in 0.24s ==========================================

pytest
PS D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014> pytest
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014
plugins: anyio-4.13.0
collected 15 items                                                                                    

test_banchmark.py .....                                                                         [ 33%]
test_sorts.py .....                                                                             [ 66%]
test_timing.py .....                                                                            [100%]

========================================= 15 passed in 0.15s =========================================
pytest
PS D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014> pytest
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014
plugins: anyio-4.13.0
collected 15 items / 1 error                                                                          

=============================================== ERRORS ===============================================
___________________________________ ERROR collecting test_plot.py ____________________________________
ImportError while importing test module 'D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014\test_plot.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\hc105\AppData\Local\Python\pythoncore-3.14-64\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
test_plot.py:9: in <module>
    from plot import load_results, plot_results, main
E   ModuleNotFoundError: No module named 'plot'
====================================== short test summary info =======================================
ERROR test_plot.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
========================================== 1 error in 2.94s ==========================================
pytest
PS D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014> pytest
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014
plugins: anyio-4.13.0
collected 21 items                                                                                    

test_banchmark.py .....                                                                         [ 23%]
test_plot.py ......                                                                             [ 52%]
test_sorts.py .....                                                                             [ 76%]
test_timing.py .....                                                                            [100%]

========================================= 21 passed in 2.78s =========================================
python -m pytest test_security.py
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014
plugins: anyio-4.13.0
collected 7 items                                                                                     

test_security.py ...FF..                                                                        [100%]

============================================== FAILURES ==============================================
____________ TestSecurityValidation.test_plot_results_rejects_results_without_data_points ____________

self = <test_security.TestSecurityValidation testMethod=test_plot_results_rejects_results_without_data_points>

    def test_plot_results_rejects_results_without_data_points(self):
        results = {
            "quick_sort": {},
            "merge_sort": {},
        }
    
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "assets" / "benchmark.png"
    
>           with self.assertRaises(ValueError):
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E           AssertionError: ValueError not raised

test_security.py:38: AssertionError
___________ TestSecurityValidation.test_plot_results_rejects_zero_or_negative_elapsed_time ___________

self = <test_security.TestSecurityValidation testMethod=test_plot_results_rejects_zero_or_negative_elapsed_time>

    def test_plot_results_rejects_zero_or_negative_elapsed_time(self):
        results = {
            "quick_sort": {
                "10": 0.0,
                "100": -0.001,
            }
        }
    
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "assets" / "benchmark.png"
    
>           with self.assertRaises(ValueError):
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E           AssertionError: ValueError not raised

test_security.py:52: AssertionError
========================================== warnings summary ==========================================
test_security.py::TestSecurityValidation::test_plot_results_rejects_results_without_data_points
  D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014\plot.py:50: UserWarning: No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
    plt.legend()

test_security.py::TestSecurityValidation::test_plot_results_rejects_zero_or_negative_elapsed_time
  D:\Edwin\program\program-python\2026-python\weeks\week-16\solutions\1114405014\plot.py:49: UserWarning: Data has no positive values, and therefore cannot be log-scaled.
    plt.yscale("log")

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
====================================== short test summary info =======================================
FAILED test_security.py::TestSecurityValidation::test_plot_results_rejects_results_without_data_points - AssertionError: ValueError not raised
FAILED test_security.py::TestSecurityValidation::test_plot_results_rejects_zero_or_negative_elapsed_time - AssertionError: ValueError not raised
============================== 2 failed, 5 passed, 2 warnings in 1.57s ===============================
