def sum(a,b):
    return a+b

def devide(a,b):
    if b==0:
        raise ValueError("Denominator could not be zero")
    return a/b

def substruct(a, b):
    if isinstance(a, str) and isinstance(b, str):
        result = a.replace(b, "")
        return result
    return a - b

print("Hi")

