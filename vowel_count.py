def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel_set = set('aeiou')
    case_insensitive_phrase = phrase.lower()
    vowel_count_dict = {}

    for letter in case_insensitive_phrase:
        if (letter in vowel_set):
            count = case_insensitive_phrase.count(letter)
            if(count > 0):
                vowel_count_dict[letter] = count
    return vowel_count_dict