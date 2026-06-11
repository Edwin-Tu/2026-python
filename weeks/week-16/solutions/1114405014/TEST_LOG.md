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
