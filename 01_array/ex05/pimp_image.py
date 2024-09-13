from numpy import array
from PIL import Image, ImageOps


def ft_invert(array) -> array:
    """ Receive image array as argument and invert colors """
    image = Image.fromarray(array)
    image_inversed = ImageOps.invert(image)
    image_inversed.show()


def ft_red(array) -> array:
    """
        Receive image array as argument and apply a red filter
        by reducing green and blue channels of each pixels
    """
    image = Image.fromarray(array)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            red = image.getpixel((x, y))[0]
            image.putpixel((x, y), (red, 0, 0))
    image.show()


def ft_green(array) -> array:
    """
        Receive image array as argument and apply a green filter
        by reducing red and blue channels of each pixels
    """
    image = Image.fromarray(array)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            green = image.getpixel((x, y))[1]
            image.putpixel((x, y), (0, green, 0))
    image.show()


def ft_blue(array) -> array:
    """
        Receive image array as argument and apply a blue filter
        by reducing red and green channels of each pixels
    """
    image = Image.fromarray(array)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            blue = image.getpixel((x, y))[2]
            image.putpixel((x, y), (0, 0, blue))
    image.show()


def ft_grey(array) -> array:
    """ Receive image array as argument and apply a grey filter """
    image = Image.fromarray(array)
    image_grey = ImageOps.grayscale(image)
    image_grey.show()
    pass
