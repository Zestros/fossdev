def calculate_tax(income):
    if income < 0:
        raise ValueError(
            "Could not hav negative income"
        )
    return int(income * 0.15 * 100) / 100