
def calculate_ndfl(income):
    result = 0
    if income < 2_400_000:
        return income * 0.13
    else:
        result = (2_400_000 * 0.13) + (income - 2_400_000) * 0.15
    return result
