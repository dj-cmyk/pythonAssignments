def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
 
    word_lst = []
    split_phrase = phrase.split(' ')
    for word in split_phrase:
        word_lst.append(word.capitalize())
    title_phrase = ' '.join(word_lst)
    return title_phrase