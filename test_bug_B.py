from bug3_logic import find_max


def test_finds_max_when_values_increase():
    assert find_max([10, 20, 30]) == 30


def test_finds_max_in_middle():
    assert find_max([3, 9, 4]) == 9


def test_finds_max_at_start():
    assert find_max([9, 4, 3]) == 9


def test_single_value():
    assert find_max([7]) == 7