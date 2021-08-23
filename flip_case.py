def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    flipped_phrase = ''
    for letter in phrase:
        if(to_swap.isupper()):
            if(letter == to_swap):
                flipped_phrase += letter.lower()
            elif(letter.upper() == to_swap):
                flipped_phrase += letter.upper()
            else:
                flipped_phrase += letter
        else:
            if(letter == to_swap):
                flipped_phrase += letter.upper()
            elif(letter.lower() == to_swap):
                flipped_phrase += letter.lower()
            else:
                flipped_phrase += letter

    return flipped_phrase