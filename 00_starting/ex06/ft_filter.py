
def ft_filter(function, iterable: object) -> iter:
    '''
    Return an iterator yielding those items of iterable for which
    function(item) is true.
    If function is None, return the items that are true.
    '''
    if function is None:
        function = bool

    return iter([element for element in iterable if function(element)])
