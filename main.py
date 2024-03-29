from datetime import date
import csv
import requests

# Wprowadzanie danych faktury


def witaj():
    print("Witaj!")
    decyzja = input("Czy chcesz dodać fakture? (Tak/Nie): ").lower()
    if decyzja == "tak":
        faktury_zapis()
    else:
        decyzja2 = input("Czy chcesz dodać płatność? (Tak/Nie): ").lower()
        if decyzja2 == "tak":
            platnosci_zapis()
        else:
            exit()


def faktury_zapis():
    id_counter = 0
    while True:
        lista_walut = ["Euro", "Dolar", "Zloty"]
        kwota = int(input("Wprowadź kwotę faktury: "))
        print("Lista walut: " + " | ".join(lista_walut))
        waluta = str(input("Wprowadź walute na fakturze: ").lower())
        print("Kiedy została wystawiona?")
        rok = int(input("Wprowadź rok: "))
        miesiac = int(input("Wprowadź miesiąc: "))
        dzien = int(input("Wprowadź dzień: "))
        data_wystawienia = date(rok, miesiac, dzien)
        # Zapisanie faktur do pliku
        id_counter += 1
        naglowek = ["id", "kwota", "waluta", "data_wystawienia"]
        with open("faktury.csv", mode="a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=naglowek)
            csv_file.seek(0, 2)  # Przesuń kursor na koniec pliku
            rozmiar = csv_file.tell()
            if rozmiar == 0:  # Dodaj nagłówki tylko jeśli plik jest pusty
                writer.writeheader()
            writer.writerow(
                {
                    "id": id_counter,
                    "kwota": kwota,
                    "waluta": waluta,
                    "data_wystawienia": data_wystawienia,
                }
            )
        print("Kwota faktury: ", kwota)
        print("Waluta faktury: ", waluta)
        print("Data: ", data_wystawienia)
        decyzja = input("Czy chcesz dodać więcej faktur? (Tak/Nie): ").lower()
        if decyzja != "tak":
            platnosci_zapis()
        else:
            faktury_zapis()


# Wprowadzanie danych płatnośći


def platnosci_zapis():
    id_counter = 0

    while True:
        lista_walut = ["Euro", "Dolar", "Zloty"]
        kwota = int(input("Wprowadź kwotę płatności: "))
        print("Lista walut: " + " | ".join(lista_walut))
        waluta = str(input("Wprowadź walute płatności: ").lower())
        print("Kiedy została opłacona?")
        rok = int(input("Wprowadź rok: "))
        miesiac = int(input("Wprowadź miesiąc: "))
        dzien = int(input("Wprowadź dzień: "))
        data_platnosci = date(rok, miesiac, dzien)
        # Zapisanie płatności do pliku
        id_counter += 1
        naglowek = ["id", "kwota", "waluta", "data_platnosci"]
        with open("platnosci.csv", mode="a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=naglowek)
            csv_file.seek(0, 2)  # Przesuń kursor na koniec pliku
            rozmiar = csv_file.tell()
            if rozmiar == 0:  # Dodaj nagłówki tylko jeśli plik jest pusty
                writer.writeheader()
            writer.writerow(
                {
                    "id": id_counter,
                    "kwota": kwota,
                    "waluta": waluta,
                    "data_platnosci": data_platnosci,
                }
            )
        print("Kwota płatnośći: ", kwota)
        print("Waluta płatnośći: ", waluta)
        print("Data płatności: ", data_platnosci)
        pytanie = "Czy chcesz dodać więcej płatności? (Tak/Nie): "
        decyzja = input(pytanie).lower()
        if decyzja != "tak":
            break
        else:
            platnosci_zapis()


def czyt_platnosc():
    data_platnosci = "2016-3-30"
    url = f"http://api.nbp.pl/api/exchangerates/rates/a/usd/{data_platnosci}/"
    request = requests.get(url)
    print(request.text)


czyt_platnosc()
witaj()
