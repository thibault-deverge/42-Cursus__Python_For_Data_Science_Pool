import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """
    Open a .jpg or .jpeg image, print its shape and return
    the image as an array.
    Print an error if it failed an return an empty array
    """
    try:
        if not path.endswith(('.jpg', '.jpeg')):
            raise TypeError("File shoud be .jpg or .jpeg")
        img = Image.open(path)
        img_array = np.array(img)
    except (TypeError) as error:
        print(f"TypeError: {error}")
        return np.array([])
    except (OSError) as error:
        print(f"OSError: {error}")
        return np.array([])

    return img_array
