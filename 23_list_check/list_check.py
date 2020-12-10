def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    for item in lst:
        if not isinstance(item, list):
            return False

    return True

    # why couldn't it have been written the other way around?
    # if isinstance(item, list) return true, else false
