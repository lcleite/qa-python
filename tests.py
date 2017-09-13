import feature


def test_sum():
    assert feature.sum(1,2) == 3, "SUM IS WRONG"


def test_append():
    ls = [1]
    feature.append(ls, 1)
    assert ls == [1,1], "APPEND IS WRONG"


def test_in():
    ls = [1]
    assert feature.is_in(ls, 1), "IN IS WRONG"