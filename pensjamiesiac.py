import pandas as pd

pr = pd.read_excel(r'D:\pythonProjectWSB\Pracownicy.xlsx')

# Wynagrodzenie za dany miesiąc
miesiac = pr['Miesiąc_pensja']

i = 0
for mies in miesiac:
    if mies == 'marzec':
        print(f'Wynagrodzenie za miesiąc {mies}')
    else:
        print(f"Nieprawidłowy miesiąc {mies} wynagrodzenia dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")

    i += 1