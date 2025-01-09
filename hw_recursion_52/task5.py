def sum_of_digits(digit_string: str) -> int:
    """
    >>> sum_of_digits('26') == 8
    True
    >>> sum_of_digits('123') == 6
    True
    """
    if not digit_string.isdigit():
        raise ValueError("input string must be digit string")

    if len(digit_string) == 1:
        return int(digit_string)  # single digit

    return int(digit_string[0]) + sum_of_digits(digit_string[1:])
