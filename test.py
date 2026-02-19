from script import sum, devide, substruct

def test_sum():
    a=1
    b=2
    res = 3
    assert sum(a,b) == res
def test_devide():
    a=2
    b=1
    res=2
    assert devide(a,b) == res
def test_devide_zero():
    a=2
    b=0
    try:
        devide(a,b)
        raise False
    except:
        print("passed")
def test_substruct():
    a = 5
    b = 3
    result = 2
    assert substruct(a,b) == result
    print("Test substruct passed")

if __name__ == "__main__":
    test_devide()
    test_sum()
    test_substruct()