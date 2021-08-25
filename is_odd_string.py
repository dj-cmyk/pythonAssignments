def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here

    alphabet_keys = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_values = list(range(1,27))
    case_insensitive_word = word.lower()
    alphabet_dict = dict(zip(alphabet_keys, alphabet_values))

    if len(word) == 1:
        if alphabet_dict[case_insensitive_word] % 2 == 0:
            return False
        else:
            return True
    elif len(word) > 1:
        counter = 0
        for char in case_insensitive_word:
            counter += alphabet_dict[char]
        if counter % 2 == 0:
            return False
        else:
            return True

