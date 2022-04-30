import pandas as pd

# Suma wypłat wszystkich pracowników

def suma_pensja(plik):
    print('Start funkcji suma_pensja')
    pr = pd.read_excel(plik)
    pensja = pr['Pensja'].sum()
    print('Pensja pracowników wynosi', pensja)
    print('Koniec funkcji suma_pensja')


# Suma premii wszystkich pracowników

def suma_premia(plik):
    print('Start funkcji suma_premia')
    pr = pd.read_excel(plik)
    premia = pr['Premia'].sum()
    print('Premia pracowników wynosi', premia)
    print('Koniec funkcji suma_premia')


# Suma wypłat wraz z premią wszystkich pracowników

def suma_wyplata(plik):
    print('Start funkcji suma_wyplata')
    pr = pd.read_excel(plik)
    wyplata = pr['Pensja'].sum() + pr['Premia'].sum()
    print('Suma pensji i premii wynosi ',wyplata)
    print('Koniec funkcji suma_wyplata')

