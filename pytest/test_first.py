def multiply(a, b):
    return a*b


def test_multiply():
    result = multiply(1, 1)
    assert result == 1

    result1 = multiply(2, 2)

    assert result1 == 4
