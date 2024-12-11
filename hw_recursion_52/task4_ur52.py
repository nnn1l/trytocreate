def reverse(input_str: str) -> str:
    """
    Function returns reversed input string
    >>> reverse("hello") == "olleh"
    True
    >>> reverse("o") == "o"
    True
    """
    if len(input_str) == 0:
        raise ValueError("Input string is empty")

    if len(input_str) == 1:
        return input_str

    return reverse(input_str[1:]) + input_str[0]
