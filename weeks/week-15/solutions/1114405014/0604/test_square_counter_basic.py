from square_counter import count_square_numbers


def test_n_1_should_return_1():
    assert count_square_numbers(1) == 1


def test_n_4_should_return_2():
    assert count_square_numbers(4) == 2


def test_n_9_should_return_3():
    assert count_square_numbers(9) == 3


def test_n_16_should_return_4():
    assert count_square_numbers(16) == 4