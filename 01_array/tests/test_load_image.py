import numpy as np
from ex02.load_image import ft_load


def test_ft_load_valid_jpeg(capfd):
    result = ft_load('../images/animal.jpeg')
    stdout = capfd.readouterr().out
    assert "The shape of image is: (768, 1024, 3)" in stdout
    assert isinstance(result, np.ndarray)


def test_ft_load_valid_jpg(capfd):
    result = ft_load('../images/landscape.jpg')
    stdout = capfd.readouterr().out
    assert "The shape of image is: (257, 450, 3)" in stdout
    assert isinstance(result, np.ndarray)


def test_ft_load_invalid_extension(capfd):
    return_value = ft_load('../images/invalid.txt')
    stdout = capfd.readouterr().out
    assert 'TypeError:' in stdout
    assert isinstance(return_value, np.ndarray)
    assert return_value.size == 0


def test_ft_load_not_found_file(capfd):
    return_value = ft_load('../images/not_found.jpg')
    stdout = capfd.readouterr().out
    assert 'OSError:' in stdout
    assert isinstance(return_value, np.ndarray)
    assert return_value.size == 0


def test_ft_load_empty_jpg(capfd):
    return_value = ft_load("../images/empty.jpg")
    stdout = capfd.readouterr().out
    assert 'OSError:' in stdout
    assert isinstance(return_value, np.ndarray)
    assert return_value.size == 0
