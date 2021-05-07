import calculator as calc


def test_add():
    assert calc.add(5, 10) == 15


def test_sub():
    assert calc.sub(10, 5) == 5
