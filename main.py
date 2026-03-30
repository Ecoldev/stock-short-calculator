from calculator import oblicz_short

print("=== KALKULATOR SHORT ===")

while True:
    try:
        print("\nPodaj dane:")

        cena_wejscia = float(input("Cena wejścia (short): "))
        cena_wyjscia = float(input("Cena wyjścia (TP): "))
        ilosc = float(input("Ilość akcji: "))
        prowizja = float(input("Prowizja (całość): "))

        wynik = oblicz_short(
            cena_wejscia,
            cena_wyjscia,
            ilosc,
            prowizja
        )

        print("\n=== WYNIK ===")
        print(f"Zysk brutto: {wynik['zysk_brutto']} PLN")
        print(f"Podatek: {wynik['podatek']} PLN")
        print(f"Zysk netto: {wynik['zysk_netto']} PLN")

        if wynik["zysk_netto"] > 0:
            print("🟢 OPŁACA SIĘ")
        elif wynik["zysk_netto"] == 0:
            print("🟡 NA ZERO")
        else:
            print("🔴 STRATA")

    except:
        print("Błąd danych")

    if input("\nJeszcze raz? (t/n): ").lower() != "t":
        break
