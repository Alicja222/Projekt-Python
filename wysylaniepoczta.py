import pandas as pd
import win32com.client as win32
import time

pr = pd.read_excel('Pracownicy.xlsx')
nr_ids = pr['ID']
emaile = pr['Email']
imiona = pr['Imię']
nazwiska = pr['Nazwisko']
pesele = pr['PESEL']

outlook = win32.Dispatch('outlook.application')


for nr_id, email, imie, nazwisko, pesel in zip(nr_ids, emaile, imiona, nazwiska, pesele):
    mail = outlook.CreateItem(0)
    mail.To = mail
    mail.Subject = 'Dzień dobry'
    mail.Body = f"Witaj {imie} {nazwisko}, twój numer pesel to {pesel}"
    mail.CC = ''
    mail.Send()
    print('Mail ',nr_id ,'wyslany')
