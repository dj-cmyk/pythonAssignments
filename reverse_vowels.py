def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    # turn string into list
    # check if each letter is a vowel
    # if not a vowel, go to next index
    # if it is a vowel, check from the end of the list for the last vowel, 
    # swap the 2 vowels

    vowels = set('aeiou')

    string_lst = list(s)
    i = 0
    j = len(s) - 1    #last index

    while i < j:
        if string_lst[i].lower() not in vowels:
            i += 1
        elif string_lst[j].lower() not in vowels:
            j -= 1
        else: 
            string_lst[i], string_lst[j] = string_lst[j], string_lst[i]   #flip flopping values
            i += 1
            j -= 1
    
    return ''.join(string_lst)

        