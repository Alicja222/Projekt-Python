import pandas as pd

# Wynagrodzenie za dany miesiąc

def sprawdz_miesiac(plik, nazwamiesiaca):
    print('Start funkcji sprawdz_miesiac')
    pr = pd.read_excel(plik)
    miesiac = pr['Miesiąc_pensja']
    i = 0
    for mies in miesiac:
        if mies != nazwamiesiaca:
            print(f"Nieprawidłowy miesiąc {mies} wynagrodzenia dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
            return False
        i += 1
    print('Koniec funkcji sprawdz_miesiac')
    return True

