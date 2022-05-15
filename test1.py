from funkcja1 import *
from funkcjapensjasuma import *
from programpoczta import wysłanie_emaili

def test_1():
    assert add(5,3) == 8
    assert add(5,3) == 9
def test_2():
    assert no_of_letters('kotek') == 5

def test_3():
    assert suma_pensja('Pracownicy.xlsx') == 41200

def test_4():
    assert suma_premia('Pracownicy.xlsx') == 13400

def test_5():


def test_():
    assert wysłanie_emaili('Pracownicy.xlsx') == True

