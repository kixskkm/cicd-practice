from calc import add, subtract

def test_add():
    assert add(1, 2) == 999  # わざと間違えた！

def test_subtract():
    assert subtract(5, 3) == 2