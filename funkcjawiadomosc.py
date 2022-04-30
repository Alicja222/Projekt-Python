import pandas as pd
informacja = []

# Wiadomość do pracownika

def wiadomosc(plik):
        pr = pd.read_excel(plik)
        dane = pr['ID']
        i = 0
        for info in dane:
                tekst = (f"Witaj {pr.loc[i,'Imię']} {pr.loc[i,'Nazwisko']} twój numer pesel to {pr.loc[i,'PESEL']}. Twoje wynagrodzenie w miesiącu {pr.loc[i,'Miesiąc_pensja']} wynosi {pr.loc[i,'Pensja']} zł, otrzymana premia to {pr.loc[i,'Premia']} zł, ilość dni przepracowanych to {pr.loc[i,'Dni_pracy']} dni, pozostało {pr.loc[i,'Dni_urlopu']} dni urlopu. Pozdrawiamy.")
                informacja.append(tekst)
                print(tekst)
                i += 1

wiadomosc()