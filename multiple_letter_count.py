def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    return_dict = {}

    for char in phrase:
        char_count = phrase.count(char)
        return_dict[char] = char_count

    return return_dict
        