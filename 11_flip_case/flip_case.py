def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    to_swap = to_swap.lower()  # make to_swap ltr lowercase
    new_phrase = ""  # new phrase string to add chars to

    for char in phrase:  # loop over chars in phrase
        if char.lower() == to_swap:  # if lowercase char = letter to swap
            char = char.swapcase()  # swap the char
        new_phrase += char  # add the new char to the new_phrase

    return new_phrase
