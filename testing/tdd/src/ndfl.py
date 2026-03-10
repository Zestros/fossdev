
def calculate_ndfl(income):
    result = 0
    tiers = [
        (0,0,0.13),
        (2_400_000,312_000,0.15),
        (5_000_000,702_000,0.18),
        (20_000_000,3_402_000,0.20),
        (50_000_000,9_402_000,0.22)
    ]
    for start, addition, taxrate in tiers[::-1]:
        if income > start:
            result = (income - start) * taxrate + addition
            return result
    raise RuntimeError("Idi nahui suka")


    """
    if income < 2_400_000:
        result = income * 0.13
    elif 2_400_000 <= income < 5_000_000:
        result = (2_400_000 * 0.13) + (income - 2_400_000) * 0.15
    elif 5_000_000 <= income < 20_000_000:
        result = (2_400_000 * 0.13) + (2_600_000 * 0.15) + (income - 5_000_000) * 0.18
    elif 20_000_000 <= income < 50_000_000:
        result = (2_400_000 * 0.13) + (2_600_000 * 0.15) + (15_000_000 * 0.18) + (income - 20_000_000) * 0.20
    elif 50_000_000 <= income:
        result = (2_400_000 * 0.13) + (2_600_000 * 0.15) + (15_000_000 * 0.18) + (30_000_000 * 0.20) + (income - 50_000_000) * 0.22
    return result
    """
