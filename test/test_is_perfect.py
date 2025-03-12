from src.is_perfect import is_perfect

def test_perfect_number_6():
    # Arrange
    number = 6
    # Act
    result = is_perfect(number)
    # Assert
    assert result is True, "tak"

def test_perfect_number_28():
    # Arrange
    number = 28
    # Act
    result = is_perfect(number)
    # Assert
    assert result is True

def test_non_perfect_number_5():
    # Arrange
    number = 5
    # Act
    result = is_perfect(number)
    # Assert
    assert result is False

def test_zero():
    # Arrange
    number = 0
    # Act
    result = is_perfect(number)
    # Assert
    assert result is False

def test_negative_number():
    # Arrange
    number = -6
    # Act
    result = is_perfect(number)
    # Assert
    assert result is False

def test_float_input():
    # Arrange
    number = 6.0
    # Act
    result = is_perfect(number)
    # Assert
    assert result is False

def test_string_input():
    # Arrange
    number = '6'
    # Act
    result = is_perfect(number)
    # Assert
    assert result is False

def test_large_perfect_number():
    # Arrange
    number = 8128
    # Act
    result = is_perfect(number)
    # Assert
    assert result is True

if __name__ == "__main__":
    tests = [
        test_perfect_number_6,
        test_perfect_number_28,
        test_non_perfect_number_5,
        test_zero,
        test_negative_number,
        test_float_input
    ]

    for test in tests:
        try:
            test()
            print(f"Test {test.__name__}: PASSED")
        except AssertionError:
            print(f"Test {test.__name__}: FAILED")