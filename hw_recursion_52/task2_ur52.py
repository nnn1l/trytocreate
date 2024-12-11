def is_palindrome(looking_str: str) -> bool:
    """
        Checks if input string is Palindrome
        >>> is_palindrome('mom')
        True

        >>> is_palindrome('sassas')
        True

        >>> is_palindrome('o')
        True
        """
    looking_str = looking_str.lower().replace(' ', '')
    if len(looking_str) == 1:
        return True

    elif len(looking_str) == 0:
        raise ValueError(f'The string is None.')

    return looking_str == looking_str[::-1]


assert is_palindrome('mom') is True
assert is_palindrome('sassas') is True
assert is_palindrome('o') is True