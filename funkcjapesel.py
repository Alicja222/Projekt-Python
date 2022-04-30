import pandas as pd

# Pesel musi posiadać 11 cyfr

def sprawdz_cyfrypesel(plik):
    print('Start funkcji sprawdz_cyfrypesel')
    pr = pd.read_excel(plik)
    pesel = pr["PESEL"]
    i = 0
    for cyfry in pesel:
        if len(str(cyfry)) != 11 and isinstance(cyfry, int):
            print(f"Nieprawidłowy pesel {cyfry}. Ma {len(str(cyfry))} cyfr, jest typu {type(cyfry)} dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
            return False
        i += 1
    print('Koniec funkcji sprawdz_cyfrypesel')
    return True

