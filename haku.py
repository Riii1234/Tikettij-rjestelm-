import tkinter as tk
import common
# -------------------------------------------------------------------
def hae_asiakas_tiedot(asiakas_entryt, asiakas_tekstikentta):
    """Asiakkaan tietojen haku ID:n, nimen tai emailin perusteella"""

    asiakas_nimi = asiakas_entryt[0].get()
    asiakas_email = asiakas_entryt[1].get()

    asiakas_tekstit = ["Nimi:", "Osoite:", "Puh.numero:", "Email:"]
    asiakas_avaimet = ["nimi", "osoite", "puh.numero", "email"]
    valilyonti_maarat = [12, 9, 1, 11]

    if asiakas_nimi != "":

        tiedot = common.hae_tiedot(asiakas_nimi, "nimi", "asiakastiedot.txt")
        tietojen_taytto(asiakas_tekstikentta, tiedot, asiakas_avaimet, asiakas_tekstit, valilyonti_maarat)

    elif asiakas_email != "":

        tiedot = common.hae_tiedot(asiakas_email, "email", "asiakastiedot.txt")
        tietojen_taytto(asiakas_tekstikentta, tiedot, asiakas_avaimet, asiakas_tekstit, valilyonti_maarat)
# -------------------------------------------------------------------
def tietojen_taytto(tekstikentta, tiedot, avaimet, tekstit, valilyonti_maarat):

    tekstikentta.delete('1.0', tk.END)

    i = 0
    while i < len(tekstit):
        if i < len(tekstit) - 1:
            # Sijoitetaan tiedot terminaaliin
            tekstikentta.insert(tk.END, f"{tekstit[i]} {" " * valilyonti_maarat[i]} {tiedot[avaimet[i]]}\n")
        else:
            tekstikentta.insert(tk.END, f"{tekstit[i]} {" " * valilyonti_maarat[i]} {tiedot[avaimet[i]]}")
        i += 1
# -------------------------------------------------------------------
def hae_laite_tiedot(laite_sarjanumero_entry, laite_tekstikentta):
    """Laitteen tietojen haku ID:n tai sarjanumeron perusteella"""

    tiedosto = "laitetiedot.txt"

    laite_sarjanumero = laite_sarjanumero_entry.get()

    laitteen_tekstit = ["Malli:", "Tyyppi:", "Sarjanumero:", "Tuotetunnus:", "Lisätiedot:"]
    laitteen_avaimet = ["malli", "tyyppi", "sarjanumero", "tuotetunnus", "lisa"]
    montako_valia = [13, 10, 1, 2, 6]

    if laite_sarjanumero != "":

        tiedot = common.hae_tiedot(laite_sarjanumero, "sarjanumero", tiedosto)
        tietojen_taytto(laite_tekstikentta, tiedot, laitteen_avaimet, laitteen_tekstit, montako_valia)
# -------------------------------------------------------------------
def aseta_laite_valikko_tiedot(laite_valikko, valikko_avain):
    """Hakee ja täyttää laite-valikon tiedoilla"""

    tiedot = common.hae_tiedot_kaikkien_erit(valikko_avain, "laitetiedot.txt")
    common.aseta_valikko(laite_valikko, tiedot)
# -------------------------------------------------------------------
def luo_laite_valikko_event(event, laite_valikko, valikko_avain, laite_tekstikentta):
    """Täyttää tekstikentän, kun valikon valintaa vaihdetaan"""

    valinta = laite_valikko.get()

    tiedot_lista = common.hae_tietoja(valinta, valikko_avain, "laitetiedot.txt")

    laitteen_tekstit = ["Malli:", "Tyyppi:", "Sarjanumero:", "Tuotetunnus:", "Lisätiedot:"]
    laitteen_avaimet = ["malli", "tyyppi", "sarjanumero", "tuotetunnus", "lisa"]
    valilyonti_maarat = [13, 10, 1, 2, 6]

    tietojen_taytto_useat(laite_tekstikentta, tiedot_lista, laitteen_avaimet, laitteen_tekstit, valinta, valilyonti_maarat)
# -------------------------------------------------------------------
def tietojen_taytto_useat(tekstikentta, tiedot_lista, avaimet, tekstit, valinta, valilyonti_maarat):
    """Täyttää tiedot entryyn"""

    tekstikentta.delete('1.0', tk.END)

    laskuri = 0
    for tiedot in tiedot_lista:

        if laskuri % 2 == 0:
            laskuri += 1
        elif laskuri < len(tiedot_lista) - 1:
            tietojen_taytto_entryyn(tiedot, tekstikentta, avaimet, tekstit, valinta, "\n\n", valilyonti_maarat)
            laskuri += 1
        else:
            tietojen_taytto_entryyn(tiedot, tekstikentta, avaimet, tekstit, valinta, "", valilyonti_maarat)
# -------------------------------------------------------------------
def tietojen_taytto_entryyn(tiedot, tekstikentta, avaimet, tekstit, valinta, rivinvaihto, valilyonti_maarat):

    i = 0
    while i < len(tekstit) - 1:
        if tiedot[avaimet[i]] != valinta:
            # Sijoitetaan tiedot terminaaliin
            tekstikentta.insert(tk.END, f"{tekstit[i]} {" " * valilyonti_maarat[i]} {tiedot[avaimet[i]]}\n")
        i += 1
    else:
        tekstikentta.insert(tk.END, f"{tekstit[i]} {" " * valilyonti_maarat[i]} {tiedot[avaimet[i]]}{rivinvaihto}")
# -------------------------------------------------------------------
def tietojen_taytto_useat_id(tekstikentta, tiedot_lista, avaimet, tekstit, valinta, tiketin_id_teksti, valilyonti_maarat):
    """Täyttää tiedot entryyn + tiketin ID"""

    tekstikentta.delete('1.0', tk.END)

    laskuri = 0
    for tiedot in tiedot_lista:
        
        if laskuri % 2 == 0:
            tekstikentta.insert(tk.END, f"{tiketin_id_teksti} {" "*18} {tiedot}\n")
            laskuri += 1

        elif laskuri < len(tiedot_lista) - 1:
            tietojen_taytto_entryyn(tiedot, tekstikentta, avaimet, tekstit, valinta, "\n\n", valilyonti_maarat)
            laskuri += 1
        else:
            tietojen_taytto_entryyn(tiedot, tekstikentta, avaimet, tekstit, valinta, "", valilyonti_maarat)
# -------------------------------------------------------------------
def tiketit_haku_valmiusaste(valmiusaste_valikko):
    """Valmiusasteiden asetus valikkoon"""

    tiedot = ["Vastaanotettu", "Työnalla", "Valmis"]

    valmiusaste_valikko.configure(values = tiedot)
    valmiusaste_valikko.set(tiedot[0])
# -------------------------------------------------------------------
def valmiusaste_valikko_event(event, valmiusaste_valikko, tiketti_tekstikentta):
    """Tikettien tietojen haku valmiusasteen perusteella"""

    tiedosto = "tikettitiedot.txt"

    valittu_valmiusaste = valmiusaste_valikko.get()

    tiketin_id_teksti = "Tiketin ID:"
    tiketin_tekstit = ["Asiakkaan nimi:", "Laitteen sarjanumero:", "Valmiusaste:", "Teknikon nimi:", "Laitteen vika:"]
    tiketin_avaimet = ["asiakas_nimi", "laite_sarjanumero", "valmiusaste", "teknikko_nimi", "vika"]
    valilyonti_maarat = [9, 1, 0, 11, 13]

    tiketin_tiedot_lista = common.hae_tietoja(valittu_valmiusaste, "valmiusaste", tiedosto)

    tiedot_lista = asiakas_nimet_ja_laite_sarjanumerot(tiketin_tiedot_lista)

    tietojen_taytto_useat_id(tiketti_tekstikentta, tiedot_lista, tiketin_avaimet, tiketin_tekstit, valittu_valmiusaste, tiketin_id_teksti, valilyonti_maarat)
# -------------------------------------------------------------------
def asiakas_nimet_ja_laite_sarjanumerot(tiketin_tiedot_lista):

    laskuri = 0
    lista = []
    for tieto in tiketin_tiedot_lista:

        if laskuri % 2 == 0:
            lista.append(tieto)
            laskuri += 1

        else:
            tieto["asiakas_nimi"] = common.hae_tieto_id(tieto["asiakas_id"], "nimi", "asiakastiedot.txt")
            tieto["laite_sarjanumero"] = common.hae_tieto_id(tieto["laite_id"], "sarjanumero", "laitetiedot.txt")
            tieto["teknikko_nimi"] = common.hae_tieto_id(tieto["teknikko_id"], "nimi", "teknikkotiedot.txt")
            laskuri += 1

    print("asiakas_nimet_ja_laite_sarjanumerot - tiketin_tiedot_lista", tiketin_tiedot_lista)
    return tiketin_tiedot_lista
