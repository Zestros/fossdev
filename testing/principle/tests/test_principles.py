import sys
#sys.path.append("../src")
#TODO make it with 'pip install -e .'

#Ранее тестирование позволяет сэкономить,
# Тесты показывают наличие ошибок, а не отсутвие
# Тесты не должны дублировать логику тестируемого кода
# Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты должны покрывать "кластеры" входных параметров
# Тесты должны обнаруживать новые ошибки (pescicide paradox)
# Тесты покрывают как успешные так и ощибочные кейсы


from math_demo import add, add_with_bug
def test_addition():
    assert add(2,2) == 4
    assert add(0,0) == 0
    assert add(7,6) == 13
    print("test addition passed")

def test_addition_with_bug():
    # Тесты показывают наличие ошибок, а не отсутвие
    assert add_with_bug(2,2) == 4
    assert add_with_bug(0,0) == 0
    assert add_with_bug(6,7) == 13
    print("test bugger addition passed")

if __name__ == '__main__':
    test_addition()
