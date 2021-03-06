import calculator as calc


def test_add():
    assert calc.add(5, 10) == 15
    assert calc.add(15, 10) == 25


def test_sub():
    assert calc.sub(10, 5) == 5
    assert calc.sub(25, 5) == 20


def test_mul():
    assert calc.mul(6, 6) == 36
    assert calc.mul(7, 8) == 56


def test_div():
    assert calc.div(10, 5) == 2
    assert calc.div(10, 0) == "ERROR: Can't divide by zero"
