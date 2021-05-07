import calculator as calc


def test_add():
    assert calc.add(5, 10) == 15
    assert calc.add(15, 10) == 25


def test_sub():
    assert calc.sub(10, 5) == 5
    assert calc.sub(25, 5) == 20
