import pandas as pd
import win32com.client as win32

pr = pd.read_excel('Pracownicy.xlsx')
informacja = []
#plik = input('Podaj ścieżkę do pliku')
dane = pr['ID']
i = 0
for info in dane:
    tekst = (f"Witaj {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']} twój numer pesel to {pr.loc[i, 'PESEL']}. Twoje wynagrodzenie w miesiącu {pr.loc[i, 'Miesiąc_pensja']} wynosi {pr.loc[i, 'Pensja']} zł, otrzymana premia to {pr.loc[i, 'Premia']} zł, ilość dni przepracowanych to {pr.loc[i, 'Dni_pracy']} dni, pozostało {pr.loc[i, 'Dni_urlopu']} dni urlopu. Pozdrawiamy.")
    informacja.append(tekst)
    print(tekst)
    i += 1

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)

mail.To = 'pw27883@student.wsb.wroclaw.pl'
mail.Subject = 'Dzień dobry'
mail.Body = tekst
mail.CC = 'pw27883@student.wsb.wroclaw.pl'

mail.Send()