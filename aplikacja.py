import funkcjapensjasuma
import funkcjasredniapensja
import funkcjapensjamiesiac
import funkcjapesel
import funkcjaemail
from funkcjaliczbykolumny import *
from funkcjainformacja import mailpracownik
plik = input('Podaj ścieżkę do pliku ')
nazwamiesiaca = input('Podaj nazwę miesiąca ')

i=0
#funkcjapensjamiesiac.sprawdz_miesiac(plik, nazwamiesiaca)
if funkcjapensjamiesiac.sprawdz_miesiac(plik, nazwamiesiaca) == True:
    i+=1
    print('Miesiąc jest poprawny')
else:
    print('Miesiąc jest niepoprawny')
#funkcjapesel.sprawdz_cyfrypesel(plik)
if funkcjapesel.sprawdz_cyfrypesel(plik) == True:
    i+=1
    print('Ilość cyfr w peselu jest poprawna')
else:
    print('Ilość cyfr w peselu jest niepoprawna')
#funkcjaemail.sprawdz_email()
if funkcjaemail.sprawdz_email(plik) == True:
    i+=1
    print('Email jest poprawny')
else:
    print('Email jest niepoprawny')
#sprawdz_id(plik)
if sprawdz_id(plik) == True:
    i+=1
    print('ID poprawne')
else:
    print('ID niepoprawne')
#sprawdz_pesel(plik)
if sprawdz_pesel(plik) == True:
    i+=1
    print('Pesel poprawny')
else:
    print('Pesel niepoprawny')
#sprawdz_pensja(plik)
if sprawdz_pensja(plik) == True:
    i+=1
    print('Pensja poprawna')
else:
    print('Pensja niepoprawna')
#sprawdz_premia(plik)
if sprawdz_premia(plik) == True:
    i+=1
    print('Premia poprawna')
else:
    print('Premia niepoprawna')
#sprawdz_dnipracy(plik)
if sprawdz_dnipracy(plik) == True:
    i+=1
    print('Dni pracy są poprawne')
else:
    print('Dni pracy są niepoprawne')
#sprawdz_dniurlopu(plik)
if sprawdz_dniurlopu(plik) == True:
    i+=1
    print('Dni urlopu są poprawne')
else:
    print('Dni urlopu są niepoprawne')
if i==9:
    print('Wszystko jest prawidłowe')
    funkcjapensjasuma.suma_wyplata(plik)
    funkcjasredniapensja.srednia_pensja(plik)
    x= mailpracownik(plik)
    print(x)
else:
    print('Nieprawidłowe')




