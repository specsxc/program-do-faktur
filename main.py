from datetime import date
import csv

# Wprowadzanie danych faktury


def faktury_zapis():
    id_counter = 0
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
        # Zapisanie faktur do pliku
        id_counter += 1
        naglowek = ['id', 'Kwota', 'Waluta', 'Data wystawienia']
        with open('faktury.csv', mode='a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=naglowek)
            csv_file.seek(0, 2)  # Przesuń kursor na koniec pliku
            rozmiar = csv_file.tell()
            if rozmiar == 0:  # Dodaj nagłówki tylko jeśli plik jest pusty
                writer.writeheader()
            writer.writerow({'id': id_counter,
                             'Kwota': kwota,
                             'Waluta': waluta,
                             'Data wystawienia': data_wystawienia})
        print("Kwota faktury: ", kwota)
        print("Waluta faktury: ", waluta)
        print("Data: ", data_wystawienia)


# Wprowadzanie danych płatnośći


def platnosci_zapis():

    id_counter = 0

    while True:
        lista_walut = ['Euro', 'Dolar', 'Zloty']
        kwota = int(input("Wprowadź kwotę płatności: "))
        print('Lista walut: ' + ' | '.join(lista_walut))
        waluta = str(input("Wprowadź walute w jakiej została opłacona: "))
        print("Kiedy została opłacona?")
        rok = int(input('Wprowadź rok: '))
        miesiac = int(input('Wprowadź miesiąc: '))
        dzien = int(input('Wprowadź dzień: '))
        data_platnosci = date(rok, miesiac, dzien)
        # Zapisanie płatności do pliku
        id_counter += 1
        naglowek = ['id', 'Kwota', 'Waluta', 'Data płatności']
        with open('platnosci.csv', mode='a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=naglowek)
            csv_file.seek(0, 2)  # Przesuń kursor na koniec pliku
            rozmiar = csv_file.tell()
            if rozmiar == 0:  # Dodaj nagłówki tylko jeśli plik jest pusty
                writer.writeheader()
            writer.writerow({'id': id_counter,
                             'Kwota': kwota,
                             'Waluta': waluta,
                             'Data płatności': data_platnosci})
        print("Kwota płatnośći: ", kwota)
        print("Waluta płatnośći: ", waluta)
        print("Data płatności: ", data_platnosci)


platnosci_zapis()
faktury_zapis()
