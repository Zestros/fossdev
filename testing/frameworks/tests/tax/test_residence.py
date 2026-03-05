from tax.income import calculate_tax


def test_tax_calculator():
    assert calculate_tax(1000) == 130
    assert calculate_tax(100) == 13
    assert calculate_tax(10) == 1.3
    assert calculate_tax(1) == 0.13
    print("test unbugged tax calculator passed")


if __name__ == '__main__':
    test_tax_calculator()