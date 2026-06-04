from square_counter import count_square_numbers


def test_n_10_should_return_3():
    assert count_square_numbers(10) == 3


def test_n_25_should_return_5():
    assert count_square_numbers(25) == 5


def test_n_26_should_return_5():
    assert count_square_numbers(26) == 5


def test_n_100_should_return_10():
    assert count_square_numbers(100) == 10


def test_n_101_should_return_10():
    assert count_square_numbers(101) == 10