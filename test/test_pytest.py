from src.calculator import fun1, fun2, fun3, fun4, fun5

def test_fun1():
    assert fun1(2, 3) == 5

def test_fun2():
    assert fun2(5, 3) == 2

def test_fun3():
    assert fun3(2, 4) == 8

def test_fun4():
    assert fun4(2, 3) == (2+3) + (2-3) + (2*3)

def test_fun5():
    assert fun5(2, 3) == 8
