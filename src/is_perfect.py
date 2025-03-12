def is_perfect(digit):
    if not isinstance(digit, int) or digit <= 0:
        return False
    if digit == 1:
        return False
    divisors_sum = 0
    sqrt_digit = int(digit ** 0.5)
    for i in range(1, sqrt_digit + 1):
        if digit % i == 0:
            if i != digit:
                divisors_sum += i
            counterpart = digit // i
            if counterpart != i and counterpart != digit:
                divisors_sum += counterpart
    return divisors_sum == digit