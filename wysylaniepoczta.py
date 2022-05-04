import pandas as pd
import win32com.client as win32

pr = pd.read_excel('Pracownicy.xlsx')
dane = pr['ID']
poczta = pr['Email']
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
for index, row in pr:
    mail.To = row["Email"]
    mail.Subject = 'Dzień dobry'
    mail.Body = (f"Witaj {pr.loc[i, 'Imię']} {pr.loc[i, 'Nazwisko']} twój numer pesel to {pr.loc[i, 'PESEL']}. Twoje wynagrodzenie w miesiącu {pr.loc[i, 'Miesiąc_pensja']} wynosi {pr.loc[i, 'Pensja']} zł, otrzymana premia to {pr.loc[i, 'Premia']} zł, ilość dni przepracowanych to {pr.loc[i, 'Dni_pracy']} dni, pozostało {pr.loc[i, 'Dni_urlopu']} dni urlopu. Pozdrawiamy.")
    mail.CC = 'pw27883@student.wsb.wroclaw.pl'

    mail.Send()