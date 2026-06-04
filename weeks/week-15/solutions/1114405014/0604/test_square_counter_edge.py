from square_counter import count_square_numbers


def test_n_0_should_return_0():
    assert count_square_numbers(0) == 0


def test_negative_number_should_return_0():
    assert count_square_numbers(-1) == 0


def test_n_2_should_return_1():
    assert count_square_numbers(2) == 1


def test_n_3_should_return_1():
    assert count_square_numbers(3) == 1


def test_n_8_should_return_2():
    assert count_square_numbers(8) == 2