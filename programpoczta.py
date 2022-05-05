import pandas as pd
import win32com.client as win32

pr = pd.read_excel('Pracownicy.xlsx')
informacja = []
#plik = input('Podaj ścieżkę do pliku')
daneid = pr['ID']
emaile = pr['Email']

i = 0
for info in daneid:
    tekst = (f"Witaj {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']} twój numer pesel to {pr.loc[i, 'PESEL']}. Twoje wynagrodzenie w miesiącu {pr.loc[i, 'Miesiąc_pensja']} wynosi {pr.loc[i, 'Pensja']} zł, otrzymana premia to {pr.loc[i, 'Premia']} zł, ilość dni przepracowanych to {pr.loc[i, 'Dni_pracy']} dni, pozostało {pr.loc[i, 'Dni_urlopu']} dni urlopu. Pozdrawiamy.")
    informacja.append(tekst)
    print(tekst)
    i += 1

outlook = win32.Dispatch('outlook.application')

for nr_id, email in zip(daneid, emaile):
    mail = outlook.CreateItem(0)
    mail.To = email
    mail.Subject = 'Dzień dobry'
    mail.Body = tekst
    mail.CC = 'pw27883@student.wsb.wroclaw.pl'
    mail.Send()
    print('Mail ',daneid, 'wysłany')