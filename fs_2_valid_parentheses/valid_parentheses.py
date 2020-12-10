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

    count = 0

    for x in parens:
        if x == '(':  # if value = (, add 1
            count += 1
        # if value = ), subtract 1 as it would not be a valid ()
        elif x == ')':
            count -= 1
        if count < 0:  # if any are left in there (since one didnt get removed)
            return False

    return count == 0
