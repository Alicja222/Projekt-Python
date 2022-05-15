from funkcjapensjasuma import *
from funkcjasredniapensja import srednia_pensja
from programpoczta import wysłanie_emaili
from funkcjapesel import sprawdz_cyfrypesel
from funkcjaliczbykolumny import sprawdz_pesel
from funkcjaliczbykolumny import sprawdz_pensja
from funkcjapensjamiesiac import sprawdz_miesiac

def test_1():
    assert suma_pensja('Pracownicy.xlsx') == 41200


def test_2():
    assert suma_premia('Pracownicy.xlsx') == 13400

def test_3():
    assert suma_wyplata('Pracownicy.xlsx') == 54600

def test_4():
    assert srednia_pensja('Pracownicy.xlsx') == 4120.0

def test_5():
    assert sprawdz_cyfrypesel('Pracownicy.xlsx') == True

def test_6():
    assert sprawdz_pesel('Pracownicy.xlsx') == True

def test_7():
    assert sprawdz_pensja('Pracownicy.xlsx') == True

def test_8():
    assert wysłanie_emaili('Pracownicy.xlsx') == True