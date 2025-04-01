import pytest
from calculadora2 import adicao, subtracao, multiplicacao, divisao

def teste_adicao():
    assert adicao(5, 4) == 9
    assert adicao(10,5) == 15
    assert adicao(20,11) == 31

def teste_subtracao():
    assert subtracao(10,5) == 5
    assert subtracao(9,4) == 5
    assert subtracao(20,13) == 7

def teste_multiplicacao():
    assert multiplicacao(1, 0) == 0
    assert multiplicacao(1, 300) == 300
    assert multiplicacao(20, 5) == 100

def teste_divisao():
    assert divisao(10,2) == 5
    assert divisao(30,2) == 15
    assert divisao(33, 3) == 11