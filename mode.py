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
    num_set = set(nums)
    max_count = 0
    max_item = None
    for item in num_set:
        counter = nums.count(item)
        if(counter > max_count):
            max_count = counter
            max_item = item


    return max_item
    
