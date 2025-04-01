import pytest
from calculadora2 import adicao, subtracao, multiplicacao, divisao

@pytest.fixture
def numeros():
    return 10, 5

def teste_adicao(numeros):
    a, b = numeros
    assert adicao(a, b) == 15
    assert adicao(-10 , -5) == -15
    assert adicao(20,11) == 31

def teste_subtracao(numeros):
    a, b = numeros
    assert subtracao(a, b) == 5
    assert subtracao(-10, -5) == -5
    assert subtracao(20,13) == 7

def teste_multiplicacao(numeros):
    a, b = numeros
    assert multiplicacao(a, 0) == 0
    assert multiplicacao(1, 300) == 300
    assert multiplicacao(20, b) == 100

def teste_divisao(numeros):
    a, b = numeros
    assert divisao(a, b) == 2
    assert divisao(30,2) == 15
    assert divisao(33, 3) == 11
    with pytest.raises(ZeroDivisionError):
        divisao(10, 0)

def divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b