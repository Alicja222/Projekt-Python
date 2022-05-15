import pandas as pd

# Średnia wypłat wszystkich pracowników
def srednia_pensja(plik):
    print('Start funkcji srednia_pensja')
    pr = pd.read_excel(plik)
    pensja = pr['Pensja'].sum()
    ilosc = int(len(pr['Pensja']))
    srednia = pensja / ilosc
    print('Średnia pensji wszystkich pracowników wynosi', round(srednia, 2))
    print('Koniec funkcji srednia_pensja')
    return round(srednia, 2)





