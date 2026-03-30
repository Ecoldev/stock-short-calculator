def oblicz_short(cena_wejscia, cena_wyjscia, ilosc, prowizja, podatek=0.19):
    przychod = cena_wejscia * ilosc
    koszt = cena_wyjscia * ilosc

    zysk_brutto = przychod - koszt - prowizja

    if zysk_brutto > 0:
        podatek_kwota = zysk_brutto * podatek
    else:
        podatek_kwota = 0

    zysk_netto = zysk_brutto - podatek_kwota

    return {
        "zysk_brutto": round(zysk_brutto, 2),
        "podatek": round(podatek_kwota, 2),
        "zysk_netto": round(zysk_netto, 2),
    }
