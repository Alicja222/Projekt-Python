import pandas as pd

pr = pd.read_excel(r'D:\pythonProjectWSB\Pracownicy.xlsx')

# Kolumny posiadające tylko cyfry
numer_id = pr['ID']
numer_pesel = pr['PESEL']
pensja = pr['Pensja']
premia = pr['Premia']
dni_pracy = pr['Dni_pracy']
dni_urlopu = pr['Dni_urlopu']

i = 0
for cyfry in numer_id:
    if type(cyfry) == int:
        print('W kolumnie ID są tylko liczby')
    else:
        print(f"Nieprawidłowe dane dla kolumny ID dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
for cyfry in numer_pesel:
    if type(cyfry) == int:
        print('W kolumnie PESEL są tylko liczby')
    else:
        print(f"Nieprawidłowe dane dla kolumny PESEL dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
for cyfry in pensja:
    if type(cyfry) == int:
        print('W kolumnie Pensja są tylko liczby')
    else:
        print(f"Nieprawidłowe dane dla kolumny dla Pensja {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
for cyfry in premia:
    if type(cyfry) == int:
        print('W kolumnie Premia są tylko liczby')
    else:
        print(f"Nieprawidłowe dane dla kolumny Premia dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
for cyfry in dni_pracy:
    if type(cyfry) == int:
        print('W kolumnie Dni_pracy są tylko liczby')
    else:
        print(f"Nieprawidłowe dane dla kolumny PESEL dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
for cyfry in dni_urlopu:
    if type(cyfry) == int:
        print('W kolumnie Dni_urlopu są tylko liczby')
    else:
        print(f"Nieprawidłowe dane dla kolumny PESEL dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")

    i += 1



#wszystkie_kolumny = pr.columns.tolist()
#print(wszystkie_kolumny)
#wybrane_kolumny = ['ID']
#print(wybrane_kolumny)