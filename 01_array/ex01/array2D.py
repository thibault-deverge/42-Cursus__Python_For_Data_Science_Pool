import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D array (family) between specified start and end indices."""
    try:
        is_valid_2D_list(family)
        is_integer(start)
        is_integer(end)
    except (ValueError, TypeError) as error:
        print(f"error: {error}")
        return []

    family_array = np.array(family)
    sliced_array = family_array[slice(start, end)]

    print(f"My shape is : {family_array.shape}")
    print(f"My new shape is : {sliced_array.shape}")
    return sliced_array.tolist()


def is_valid_2D_list(lst: any):
    """Validate that the input is a 2D list."""
    if not isinstance(lst, list) or np.array(lst).ndim != 2:
        raise TypeError("Invalid 2D array as first argument")


def is_integer(arg: any):
    """Validate that the input is an integer."""
    if not isinstance(arg, int):
        raise TypeError("start and end argument should be integer.")
