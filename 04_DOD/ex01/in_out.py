def square(x: int | float) -> int | float:
    '''return square of a number'''
    return x * x


def pow(x: int | float) -> int | float:
    '''return pow of a number with itself'''
    return x ** x


def outer(x: int | float, function) -> object:
    '''closure function which act as wrapper'''
    count = 0

    def inner() -> float:
        '''execute a function on a range of numbers'''
        nonlocal count
        count += 1
        result = function(x)

        for iter in range(count - 1):
            result = function(result)
        return result

    return inner
