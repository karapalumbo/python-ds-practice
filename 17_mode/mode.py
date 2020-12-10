def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    val_counter = {}

    for val in nums:
        if val in val_counter:
            val_counter[val] += 1
        else:
            val_counter[val] = 1

    popular_vals = sorted(val_counter, key=val_counter.get, reverse=True)

    top = popular_vals[:1]

    return top.pop()
