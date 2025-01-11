from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0


def test_bound_basic2():
    assert bound_to_180(200) == -160.0


def test_bound_basic3():
    assert bound_to_180(135) == 135.0


def test_bound_basic4():
    assert bound_to_180(-200) == 160.0


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)


def test_between_basic2():
    assert is_angle_between(0, 45, 90)


def test_between_basic3():
    assert is_angle_between(45, 90, 270)


def test_between_basic4():
    assert not is_angle_between(45, 0, 270)
