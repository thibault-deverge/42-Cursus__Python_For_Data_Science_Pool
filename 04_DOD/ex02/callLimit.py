def callLimit(limit: int):
    """Limits the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwargs: any):
            """Act as a wrapper for the function."""
            nonlocal count
            count += 1
            if count <= limit:
                function()
            else:
                print(f"Error: {function} call too many times")
        return limit_function

    return callLimiter
