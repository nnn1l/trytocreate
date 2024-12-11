def mult(a: int, n: int) -> int:
    """
    This function works only with positive integers

    >>> mult(2, 4) == 8
    True

    >>> mult(2, 0) == 0
    True

    >>> mult(2, -4)
    ValueError("This function works only with positive integers")
    """
    if a < 0 or n < 0:
        raise ValueError("This function works only with positive integers")
    if n == 0 or a == 0:
        return 0
    if a == 1:
        return n
    if n == 1:
        return a
    return a + mult(a, n - 1)

assert mult(2, 4) == 8
assert mult(2, 0) == 0