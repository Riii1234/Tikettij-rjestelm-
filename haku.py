import tkinter as tk
import common
# -------------------------------------------------------------------
def aseta_laite_valikko_tiedot(laite_valikko, valikko_avain):
    """Hakee ja täyttää laite-valikon tiedoilla"""

    tieto_lista = common.hae_tieto_lista(valikko_avain, "laitetiedot.txt", "erilaiset", [])
    common.aseta_valikko(laite_valikko, tieto_lista)
# -------------------------------------------------------------------
def aseta_valmiusaste_valikko_tiedot(valmiusaste_valikko):
    """Täyttää valmiusaste-valikon tiedoilla"""

    tieto_lista = ["Vastaanotettu", "Työnalla", "Valmis"]
    common.aseta_valikko(valmiusaste_valikko, tieto_lista)
# -------------------------------------------------------------------
def hae_asiakas_tiedot(asiakas_entryt, asiakas_tekstikentta):
    """Hakee asiakkaan nimen tai emailin valinnan ja luo tarvittavat tiedot"""

    asiakas_nimi_valinta = asiakas_entryt[0].get()
    asiakas_email_valinta = asiakas_entryt[1].get()

    asiakas_tekstit = ["Nimi:", "Osoite:", "Puh.numero:", "Email:"]
    asiakas_avaimet = ["nimi", "osoite", "puh.numero", "email"]
    valilyonti_maarat = [12, 9, 1, 11]

    if asiakas_nimi_valinta != "":
        hae_tiedot_ja_tayta_tekstikentta(asiakas_nimi_valinta, "nimi", "asiakastiedot.txt", asiakas_tekstikentta, asiakas_avaimet, asiakas_tekstit, valilyonti_maarat)

    elif asiakas_email_valinta != "":
        hae_tiedot_ja_tayta_tekstikentta(asiakas_email_valinta, "email", "asiakastiedot.txt", asiakas_tekstikentta, asiakas_avaimet, asiakas_tekstit, valilyonti_maarat)
# -------------------------------------------------------------------
def hae_laite_tiedot(laite_sarjanumero_entry, laite_tekstikentta):
    """Hakee laitteen sarjanumeron valinnan ja luo tarvittavat tiedot"""

    laite_sarjanumero_valinta = laite_sarjanumero_entry.get()

    laite_tekstit = ["Malli:", "Tyyppi:", "Sarjanumero:", "Tuotetunnus:", "Lisätiedot:"]
    laite_avaimet = ["malli", "tyyppi", "sarjanumero", "tuotetunnus", "lisa"]
    valilyonti_maarat = [13, 10, 1, 2, 6]

    if laite_sarjanumero_valinta != "":
        hae_tiedot_ja_tayta_tekstikentta(laite_sarjanumero_valinta, "sarjanumero", "laitetiedot.txt", laite_tekstikentta, laite_avaimet, laite_tekstit, valilyonti_maarat)
# -------------------------------------------------------------------
def hae_tiedot_ja_tayta_tekstikentta(valinta, avain, tiedosto, tekstikentta, avaimet, tekstit, valilyonti_maarat):
    """Hakee tiedot sanakirjaan ja täyttää ne tekstikenttään"""

    tiedot_sanakirja = common.hae_tiedot(valinta, avain, tiedosto, "tieto")
    if tiedot_sanakirja != "":
        
        tekstikentta.delete('1.0', tk.END)
        i = 0
        while i < len(tekstit):
            if i < len(tekstit) - 1:
                # Sijoitetaan tiedot terminaaliin
                tekstikentta.insert(tk.END, f"{tekstit[i]} {" " * valilyonti_maarat[i]} {tiedot_sanakirja[avaimet[i]]}\n")
            else:
                tekstikentta.insert(tk.END, f"{tekstit[i]} {" " * valilyonti_maarat[i]} {tiedot_sanakirja[avaimet[i]]}")
            i += 1
# -------------------------------------------------------------------
def luo_laite_valikko_event(event, laite_valikko, valikko_avain, laite_tekstikentta):
    """Täyttää tekstikentän, kun valikon valintaa vaihdetaan"""

    laite_valinta = laite_valikko.get()

    laite_idt_ja_tiedot_lista = common.hae_tietoja(laite_valinta, valikko_avain, "laitetiedot.txt")

    id_teksti = ""
    laite_tekstit = ["Malli:", "Tyyppi:", "Sarjanumero:", "Tuotetunnus:", "Lisätiedot:"]
    laite_avaimet = ["malli", "tyyppi", "sarjanumero", "tuotetunnus", "lisa"]
    valilyonti_maarat = [13, 10, 1, 2, 6]

    tayta_tekstikentta_useita_tietoja(laite_tekstikentta, laite_idt_ja_tiedot_lista, laite_avaimet, laite_tekstit, laite_valinta, valilyonti_maarat, id_teksti)
# -------------------------------------------------------------------
def luo_valmiusaste_valikko_event(event, valmiusaste_valikko, tiketti_tekstikentta):
    """Täyttää tekstikentän, kun valikon valintaa vaihdetaan"""

    valmiusaste_valinta = valmiusaste_valikko.get()

    tiketti_idt_ja_tiedot_lista = common.hae_tietoja(valmiusaste_valinta, "valmiusaste", "tikettitiedot.txt")

    idt_ja_tiedot_lista = lisaa_listan_sanakirjaan_tietoja(tiketti_idt_ja_tiedot_lista)

    tiketti_id_teksti = "Tiketin ID:"
    tiketti_tekstit = ["Asiakkaan nimi:", "Laitteen sarjanumero:", "Valmiusaste:", "Teknikon nimi:", "Laitteen vika:"]
    tiketti_avaimet = ["asiakas_nimi", "laite_sarjanumero", "valmiusaste", "teknikko_nimi", "vika"]
    valilyonti_maarat = [9, 1, 0, 11, 13]

    tayta_tekstikentta_useita_tietoja(tiketti_tekstikentta, idt_ja_tiedot_lista, tiketti_avaimet, tiketti_tekstit, valmiusaste_valinta, valilyonti_maarat, tiketti_id_teksti)
# -------------------------------------------------------------------
def tayta_tekstikentta_useita_tietoja(tekstikentta, idt_ja_tiedot_lista, avaimet, tekstit, valinta, valilyonti_maarat, id_teksti):
    """Täyttää tiedot tekstikenttään"""

    tekstikentta.delete('1.0', tk.END)

    laskuri = 0
    for tiedot in idt_ja_tiedot_lista:

        if laskuri % 2 == 0:
            if id_teksti != "":
                tekstikentta.insert(tk.END, f"{id_teksti} {" "*18} {tiedot}\n")
            laskuri += 1
        elif laskuri < len(idt_ja_tiedot_lista) - 1:
            tayta_tiedot_tekstikenttaan(tiedot, tekstikentta, avaimet, tekstit, valinta, "\n\n", valilyonti_maarat)
            laskuri += 1
        else:
            tayta_tiedot_tekstikenttaan(tiedot, tekstikentta, avaimet, tekstit, valinta, "", valilyonti_maarat)
# -------------------------------------------------------------------
def tayta_tiedot_tekstikenttaan(tiedot, tekstikentta, avaimet, tekstit, valinta, rivinvaihto, valilyonti_maarat):
    """Täyttää tiedot tekstikenttään"""

    i = 0
    while i < len(tekstit) - 1:
        if tiedot[avaimet[i]] != valinta:
            # Sijoitetaan tiedot terminaaliin
            tekstikentta.insert(tk.END, f"{tekstit[i]} {" " * valilyonti_maarat[i]} {tiedot[avaimet[i]]}\n")
        i += 1
    else:
        tekstikentta.insert(tk.END, f"{tekstit[i]} {" " * valilyonti_maarat[i]} {tiedot[avaimet[i]]}{rivinvaihto}")
# -------------------------------------------------------------------
def lisaa_listan_sanakirjaan_tietoja(idt_ja_tiedot_lista):
    """Lisää listassa olevaan tiedot-sanakirjaan tarvittavia tietoja"""

    laskuri = 0
    lista = []
    for tieto in idt_ja_tiedot_lista:

        if laskuri % 2 == 0:
            lista.append(tieto)
            laskuri += 1

        else:
            tieto["asiakas_nimi"] = common.hae_tieto_id(tieto["asiakas_id"], "nimi", "asiakastiedot.txt")
            tieto["laite_sarjanumero"] = common.hae_tieto_id(tieto["laite_id"], "sarjanumero", "laitetiedot.txt")
            tieto["teknikko_nimi"] = common.hae_tieto_id(tieto["teknikko_id"], "nimi", "teknikkotiedot.txt")
            laskuri += 1

    return idt_ja_tiedot_lista
# -------------------------------------------------------------------