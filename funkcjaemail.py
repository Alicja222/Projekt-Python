import pandas as pd

# Sprawdzenie czy mail posiada @, nazwę użytkownika i domenę

def sprawdz_email(plik):
    print('Start funkcji sprawdz_email')
    pr = pd.read_excel(plik)
    lista_domeny = pd.read_excel(r'D:\pythonProjectWSB\Lista domen.xlsx')
    mail = pr["Email"]
    nazwa_domeny = lista_domeny["Lista domen"]
    i = 0
    for poczta in mail:
        if poczta.count("@") == 1:
            print("\nPracownik ", i + 1, " Email jest prawidłowy: ", poczta)
            pozycja_malpy = poczta.find("@")
            print(f'znak @ jest na pozycji {poczta.find("@") + 1}')
            nazwa_uzytkownika = poczta[:pozycja_malpy]
            print('nazwa uzytkownika to ', poczta[:pozycja_malpy])
            ostatnia_kropka = poczta.rindex('.')
            print('ostatnia kropka jest na pozycji ', poczta.rindex('.'))
            domena = poczta[pozycja_malpy + 1:ostatnia_kropka]
            print('nazwa domeny to ', poczta[pozycja_malpy + 1:ostatnia_kropka])
            if domena in str(nazwa_domeny):
                print('nazwa domeny jest prawidłowa')
            else:
                print(f"nieprawidłowa domena dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
                return False
        else:
            print(f"Nieprawidłowy email dla {pr.loc[i, 'ID']} {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']}")
            return False
        i += 1
    print('Koniec funkcji sprawdz_email')
    return True




