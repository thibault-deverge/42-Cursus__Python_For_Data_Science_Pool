import pytest
from ex01.array2D import slice_me


@pytest.fixture
def valid_family():
    return [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]


def test_slice_me_valid_input(capfd, valid_family):
    result = slice_me(valid_family, 0, 2)
    stdout = capfd.readouterr().out
    assert stdout == "My shape is : (4, 2)\nMy new shape is : (2, 2)\n"
    assert result == [[1.8, 78.4], [2.15, 102.7]]

    result = slice_me(valid_family, 1, -2)
    stdout = capfd.readouterr().out
    assert stdout == "My shape is : (4, 2)\nMy new shape is : (1, 2)\n"
    assert result == [[2.15, 102.7]]


def test_slice_me_out_of_bounds(capfd, valid_family):
    result = slice_me(valid_family, 0, 10)
    stdout = capfd.readouterr().out
    assert stdout == "My shape is : (4, 2)\nMy new shape is : (4, 2)\n"
    assert result == valid_family


def test_slice_me_out_of_bounds_negative(capfd, valid_family):
    result = slice_me(valid_family, -10, -6)
    stdout = capfd.readouterr().out
    assert stdout == "My shape is : (4, 2)\nMy new shape is : (0, 2)\n"
    assert result == []


def test_slice_me_invalid_family_list1(capfd):
    return_value = slice_me("invalid input", 0, 2)
    stdout = capfd.readouterr().out
    assert 'error' in stdout
    assert return_value == []


def test_slice_me_invalid_family_list2(capfd):
    return_value = slice_me([[1, 2], [3]], 0, 2)
    stdout = capfd.readouterr().out
    assert 'error' in stdout
    assert return_value == []


def test_slice_me_invalid_start_type(capfd, valid_family):
    return_value = slice_me(valid_family, "start", 2)
    stdout = capfd.readouterr().out
    assert 'error' in stdout
    assert return_value == []


def test_slice_me_invalid_end_type(capfd, valid_family):
    return_value = slice_me(valid_family, 0, "end")
    stdout = capfd.readouterr().out
    assert 'error' in stdout
    assert return_value == []
