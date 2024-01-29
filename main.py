from datetime import date
import csv

# Wprowadzanie danych faktury


def faktury_zapis():
    while True:
        lista_walut = ['Euro', 'Dolar', 'Zloty']
        kwota = int(input("Wprowadź kwotę faktury: "))
        print('Lista walut: ' + ' | '.join(lista_walut))
        waluta = str(input("Wprowadź walute w jakiej została wystawiona: "))
        print("Kiedy została wystawiona?")
        rok = int(input('Wprowadź rok: '))
        miesiac = int(input('Wprowadź miesiąc: '))
        dzien = int(input('Wprowadź dzień: '))
        data_wystawienia = date(rok, miesiac, dzien)
        print("Kwota: ", kwota)
        print("Twoja waluta to: ", waluta)
        print("Data: ", data_wystawienia)
        # Zapisanie faktur do pliku
        with open('faktury.csv', 'a', newline='') as faktury:
            spamwriter = csv.writer(faktury, delimiter=',')
            spamwriter.writerow({kwota, waluta, data_wystawienia})


faktury_zapis()
