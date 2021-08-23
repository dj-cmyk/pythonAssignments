def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    lowercase_str = phrase.lower()
    no_space_str = lowercase_str.replace(' ', '')
    listed_str = list(no_space_str)
    listed_str.reverse()
    joined_lst = "".join(listed_str)

    if joined_lst == no_space_str:
        return True
    else:
        return False
