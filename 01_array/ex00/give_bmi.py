import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]):
    """Calculate the BMI for given heights and weights."""
    try:
        parse_list(height)
        parse_list(weight)
        if len(height) != len(weight):
            raise ValueError("Both arguments should have of same size")
        height_array = np.array(height, dtype=float)
        weight_array = np.array(weight, dtype=float)
    except (ValueError, TypeError) as error:
        print(f"error: {error}")
        return []

    return (weight_array / (height_array ** 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check if each BMI value exceeds the specified limit."""
    try:
        parse_list(bmi)
        if not isinstance(limit, int):
            raise TypeError("Second argument should be an integer'")
    except (ValueError, TypeError) as error:
        print(f"error: {error}")
        return []

    return list(map(lambda x: x > limit, bmi))


def parse_list(lst: list):
    """Validate that the list contains only integers or floats."""
    if not isinstance(lst, list):
        raise TypeError("Arguments should be of type 'list'")

    for element in lst:
        if not isinstance(element, int) and not isinstance(element, float):
            raise ValueError("Elements of the list should be integer or float")
