from calculadora import somar, subtrair, multiplicar, dividir

def test_somar():
    assert somar(2, 3) == 5

def test_subtrair():
    assert subtrair(5, 2) == 3

def test_multiplicar():
    assert multiplicar(3, 3) == 9

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(5, 0) == "Erro: Você não pode dividir por zero!"