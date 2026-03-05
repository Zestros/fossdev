def add(a,b):
    return a+b

def add_with_bug(a,b):
    return a*b

def calculate_tax_buggged(income):
    return income * 0.15 

def calculate_tax(income):
    if income < 0:
        reise ValueError(
            "Could not hav negative income"
        )
    return int(income * 0.15 * 100) / 100