import pandas as pd

# Kolumny posiadające tylko cyfry

def sprawdz_id(plik):
    print('Start funkcji sprawdz_id')
    pr = pd.read_excel(plik)
    numer_id = pr['ID']
    i = 0
    for cyfry in numer_id:
        if type(cyfry) != int:
            print(f"Nieprawidłowe dane dla kolumny ID dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
            return False
        i += 1
    print('Koniec funkcji sprawdz_id')
    return True


def sprawdz_pesel(plik):
    print('Start funkcji sprawdz_pesel')
    pr = pd.read_excel(plik)
    numer_pesel = pr['PESEL']
    i = 0
    for cyfry in numer_pesel:
        if type(cyfry) != int:
            print(f"Nieprawidłowe dane dla kolumny Pesel dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
            return False
        i += 1
    print('Koniec funkcji sprawdz_pesel')
    return True

def sprawdz_pensja(plik):
    print('Start funkcji sprawdz_pensja')
    pr = pd.read_excel(plik)
    pensja = pr['Pensja']
    i = 0
    for cyfry in pensja:
        if type(cyfry) != int:
            print(f"Nieprawidłowe dane dla kolumny Pensja dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
            return False
        i += 1
    print('Koniec funkcji sprawdz_pensja')
    return True

def sprawdz_premia(plik):
    print('Start funkcji sprawdz_premia')
    pr = pd.read_excel(plik)
    premia = pr['Premia']
    i = 0
    for cyfry in premia:
        if type(cyfry) != int:
            print(f"Nieprawidłowe dane dla kolumny Premia dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
            return False
        i += 1
    print('Koniec funkcji sprawdz_premia')
    return True

def sprawdz_dnipracy(plik):
    print('Start funkcji sprawdz_dnipracy')
    pr = pd.read_excel(plik)
    dni_pracy = pr['Dni_pracy']
    i = 0
    for cyfry in dni_pracy:
        if type(cyfry) != int:
            print(f"Nieprawidłowe dane dla kolumny Dni_pracy dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
            return False
        i += 1
    print('Koniec funkcji sprawdz_dnipracy')
    return True

def sprawdz_dniurlopu(plik):
    print('Start funkcji sprawdz_dniurlopu')
    pr = pd.read_excel(plik)
    dni_urlopu = pr['Dni_urlopu']
    i = 0
    for cyfry in dni_urlopu:
        if type(cyfry) != int:
            print(f"Nieprawidłowe dane dla kolumny Dni_urlopu dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
            return False
        i += 1
    print('Koniec funkcji sprawdz_dniurlopu')
    return True



