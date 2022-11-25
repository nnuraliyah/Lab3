import bmi
print("Test_Bmi")

def test_bmi_normal_weight():
    result = []
    height = 1.73
    weight = 57
    test = 0

    result = bmi.calculate_bmi(weight, height)

    assert (result == test)

def test_bmi_over_weight():
    result = []
    height = 1
    weight = 140
    test = 1

    result = bmi.calculate_bmi(weight, height)

    assert (result == test)

def test_bmi_under_weight():
    result = []
    height = 1.73
    weight = 40
    test = -1

    result = bmi.calculate_bmi(weight, height)

    assert (result == test)