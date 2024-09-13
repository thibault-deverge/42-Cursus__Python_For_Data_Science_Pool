import pytest
from ex00.give_bmi import give_bmi, apply_limit


def test_give_bmi_valid_input():
    height = [1.75, 1.80, 1.65]
    weight = [70, 80, 60]
    expected_bmi = [22.85714, 24.69135, 22.03856]
    assert give_bmi(height, weight) == pytest.approx(expected_bmi)


def test_give_bmi_invalid_size_lists(capfd):
    height = [1.75, 1.80]
    weight = [70, 80, 60]
    return_value = give_bmi(height, weight)
    stdout = capfd.readouterr().out
    assert 'error' in stdout
    assert return_value == []


def test_give_bmi_invalid_height_type(capfd):
    height = [1.75, "1.80", 1.65]
    weight = [70, 80, 60]
    return_value = give_bmi(height, weight)
    stdout = capfd.readouterr().out
    assert 'error' in stdout
    assert return_value == []


def test_give_bmi_invalid_weight_type(capfd):
    height = [1.75, 1.80, 1.65]
    weight = [70, "80", 60]
    return_value = give_bmi(height, weight)
    stdout = capfd.readouterr().out
    assert 'error' in stdout
    assert return_value == []


def test_apply_limit_valid_input():
    bmi = [22.8, 24.7, 30.0]
    limit = 25
    expected_output = [False, False, True]
    assert apply_limit(bmi, limit) == expected_output


def test_apply_limit_invalid_bmi_type(capfd):
    bmi = [22.8, "24.7", 30.0]
    limit = 25
    return_value = apply_limit(bmi, limit)
    stdout = capfd.readouterr().out
    assert 'error' in stdout
    assert return_value == []


def test_apply_limit_invalid_limit_type(capfd):
    bmi = [22.8, 24.7, 30.0]
    limit = "25"
    return_value = apply_limit(bmi, limit)
    stdout = capfd.readouterr().out
    assert 'error' in stdout
    assert return_value == []


def test_apply_limit_non_list_input(capfd):
    bmi = "22.8, 24.7, 30.0"
    limit = 25
    return_value = apply_limit(bmi, limit)
    stdout = capfd.readouterr().out
    assert 'error' in stdout
    assert return_value == []
