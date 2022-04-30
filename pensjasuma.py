import pandas as pd

pr = pd.read_excel(r'D:\pythonProjectWSB\Pracownicy.xlsx')

# Suma wypłat wszystkich pracowników
pensja = pr['Pensja'].sum()
print('Pensja pracowników wynosi ',pensja)

# Suma premii wszystkich pracowników
premia = pr['Premia'].sum()
print('Premia pracowników wynosi ',premia)

# Suma wypłat wraz z premią wszystkich pracowników
pensjapremia = pr['Pensja'].sum() + pr['Premia'].sum()
print('Suma pensji i premii wynosi ',pensjapremia)