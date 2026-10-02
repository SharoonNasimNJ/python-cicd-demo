# test_app.py - Tests for our calculator

from app import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(5, 6) == 30

def test_divide():
    assert divide(20, 4) == 5.0

def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        assert True

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_divide_by_zero()
    print("✅ All tests passed!")
