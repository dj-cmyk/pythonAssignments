def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    # iterate over the list to get new list of only even numbers
    # muliply those numbers together
    evens_list = []
    for n in nums:
        if (n % 2 == 0):
            evens_list.append(n)

    product = 1

    for item in evens_list:
        product *= item
    
    return product