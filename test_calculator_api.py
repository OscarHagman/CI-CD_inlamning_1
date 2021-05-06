import calculator_api as capi


def test_add():
    assert capi.add(7, 10) == 17
