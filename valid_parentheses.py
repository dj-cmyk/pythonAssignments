def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    open_parens = []
    closed_parens = []
    
    if parens[0] == ')':
        return False
    
    for char in parens:
        if char == '(':
            open_parens.append(char)
        elif char == ')':
            closed_parens.append(char)
    if len(open_parens) == len(closed_parens):
        return True
    else:
        return False
    