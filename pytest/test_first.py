def multiply(a, b):
    # if a == 3 and b == 3:
    #     return 10
    return a * b


def test_multiply():
    result = multiply(1, 1)
    assert result == 1

    result1 = multiply(2, 2)

    assert result1 == 4
    result2 = multiply(3, 3)
    assert result2 == 9
    result3 = multiply(4,4)
    assert result3 == 16
