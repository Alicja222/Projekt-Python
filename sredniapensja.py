import pandas as pd

pr = pd.read_excel(r'D:\pythonProjectWSB\Pracownicy.xlsx')

# Suma wypłat wszystkich pracowników
pensja = pr['Pensja'].sum()
print('Pensja pracowników wynosi',pensja)

# Średnia wypłat wszystkich pracowników
ilość = int(len(pr['Pensja']))
srednia = pensja / ilość

print('Średnia pensji wynosi ', str(round(srednia,2)))
