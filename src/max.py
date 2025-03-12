def max(digits):
    if digits is None:
        return None
    if not isinstance(digits, list):
        return None
    if len(digits) == 0:
        return None
    current_max = digits[0]
    for num in digits[1:]:
        if num > current_max:
            current_max = num
    return current_max