def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    split_string_into_list = list(phrase)
    split_string_into_list.reverse()
    new_phrase = "".join(split_string_into_list)
    return new_phrase