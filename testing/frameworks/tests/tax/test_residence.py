from tax.income import calculate_tax


def test_tax_calculator():
    assert calculate_tax(1000) == 150
    assert calculate_tax(100) == 15
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(2.34) == 0.35
    print("test unbugged tax calculator passed")

def test_negatie_income():
    try:
        calculate_tax(-100)
        print("test negative income falied")
    except ValueError as e:
        print("test negative income passed")

if __name__ == '__main__':
    test_tax_calculator()
    test_negatie_income()