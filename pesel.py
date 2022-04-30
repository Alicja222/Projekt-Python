import pandas as pd

pr = pd.read_excel(r'D:\pythonProjectWSB\Pracownicy.xlsx')


# Pesel musi posiadać 11 cyfr
pesel = pr["PESEL"]

i = 0
for cyfry in pesel:
    if len(str(cyfry)) == 11 and isinstance(cyfry, int):
        print('Prawidłowy pesel')
    else:
        print(f"Nieprawidłowy pesel {cyfry}. Ma {len(str(cyfry))} cyfr, jest typu {type(cyfry)} dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
    i += 1
