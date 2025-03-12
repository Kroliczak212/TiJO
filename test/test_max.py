from src.max import max


def test_max_with_none():
    # Arrange
    input_digits = None
    # Act
    result = max(input_digits)
    # Assert
    assert result is None


def test_max_with_empty_list():
    # Arrange
    input_digits = []
    # Act
    result = max(input_digits)
    # Assert
    assert result is None


def test_max_single_element():
    # Arrange
    input_digits = [5]
    # Act
    result = max(input_digits)
    # Assert
    assert result == 5


def test_max_multiple_elements():
    # Arrange
    input_digits = [3, 1, 4, 2]
    # Act
    result = max(input_digits)
    # Assert
    assert result == 4


if __name__ == "__main__":
    tests = [
        test_max_with_none,
        test_max_with_empty_list,
        test_max_single_element,
        test_max_multiple_elements
    ]

    for test in tests:
        try:
            test()
            print(f"Test {test.__name__}: PASSED")
        except AssertionError:
            print(f"Test {test.__name__}: FAILED")