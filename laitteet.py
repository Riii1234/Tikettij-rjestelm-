import globals
import common
import tkinter as tk
# -------------------------------------------------------------------
def luo_uusi_laite(laite_tiedot_lista):
    """Luo uudelle laitteelle ID:n ja ottaa vastaan laitteen tiedot"""

    tiedosto = "laitetiedot.txt"
    # Lukee tiedostosta olemassa olevien laitteiden tiedot sanakirjaan
    laite_sanakirja = common.avaa_tiedosto(tiedosto)

    # Laskee montako laitetta on jo olemassa ID:n luomista varten
    montako = common.laske_id_lukumaara(laite_sanakirja)

    # Luo uudelle laitteelle ID-tunnuksen
    id = common.luo_uusi_id("la-", montako)

    laite_avaimet = ["malli", "tyyppi", "sarjanumero", "tuotetunnus", "lisa"]
    # Kirjataan laitteen tiedot sanakirjaan
    sanakirja = common.lisaa_tiedot_sanakirjaan(laite_tiedot_lista, laite_avaimet)

    laite_sanakirja[id] = sanakirja

    # Tallentaa laitteen tiedot tiedostoon
    common.tallenna_tiedostoon(laite_sanakirja, id, tiedosto)
    return id
# -------------------------------------------------------------------
def hae_laite_tiedot_mallilla(laite_entryt, asiakas_muuttujat, laite_malli):
    """Hakee vanhan laitteen tiedot mallin avullaja täyttää sen perusteella tiedot entryihin"""

    haettavat_laitteet = hae_vanhat_laitteet(asiakas_muuttujat)

    laite_sanakirja = common.avaa_tiedosto("laitetiedot.txt")
    
    lista = ["malli", "tyyppi", "sarjanumero", "tuotetunnus", "lisa"]
    # Tiedot sisältävät laite_id, malli, tyyppi, sarjanumero, tuotetunnus ja lisätiedot
    for id, tiedot in laite_sanakirja.items():
        if id in haettavat_laitteet:

            if laite_malli == tiedot["malli"]:
                globals.onko_uusi_laite = False

                for i in range(0, 5):
                    # Sijoitetaan tiedot terminaaliin
                    laite_entryt[i].delete(0, tk.END)
                    laite_entryt[i].insert(0, tiedot[lista[i]])
# -------------------------------------------------------------------
def hae_laite_tiedot(laite_malli_muuttuja, laite_entryt, asiakas_muuttujat):
    """Hakee laitteen mallin entry-widgetistä"""

    laite_malli = laite_malli_muuttuja.get()

    hae_laite_tiedot_mallilla(laite_entryt, asiakas_muuttujat, laite_malli)
# -------------------------------------------------------------------
def tayta_vanha_laite_tiedot(event, laite_entryt, asiakas_muuttujat, vanhat_laitteet_valikko):
    """Antaa tällä hetkellä valitun laitteen valikosta"""

    laite_malli = vanhat_laitteet_valikko.get()

    hae_laite_tiedot_mallilla(laite_entryt, asiakas_muuttujat, laite_malli)
# -------------------------------------------------------------------
def hae_vanhat_laitteet(asiakas_muuttujat):
    """Hakee vanhat laitteet asiakkaan ID:llä"""

    #print("vanhat_laitteet asiakkaan_tiedot", asiakkaan_tiedot)

    asiakas_id = common.hae_id(asiakas_muuttujat, "asiakastiedot.txt", "nimi")
  
    tiketti_sanakirja = common.avaa_tiedosto("tikettitiedot.txt")
    # Haetaan kaikki asiakkaan laitteet tiketeistä
    haettavat_laitteet = []
    for tiketti, tiedot in tiketti_sanakirja.items():
        if asiakas_id == tiedot["asiakas_id"]:
            haettavat_laitteet.append(tiedot["laite_id"])

    return haettavat_laitteet
# -------------------------------------------------------------------
def aseta_vanhat_laitteet_valikko(asiakas_muuttujat, vanhat_laitteet_valikko):
    """Asettaa asiakkaan vanhat laitteet valikkoon"""

    laitteet_lista = hae_vanhat_laite_mallit(asiakas_muuttujat)

    common.aseta_valikko(vanhat_laitteet_valikko, laitteet_lista)
# -------------------------------------------------------------------
def hae_vanhat_laite_mallit(asiakas_muuttujat):
    """Hakee laitteiden mallit"""

    haettavat_laitteet = hae_vanhat_laitteet(asiakas_muuttujat)

    laite_sanakirja = common.avaa_tiedosto("laitetiedot.txt")
    laite_mallit = []

    for id, tiedot in laite_sanakirja.items():
        if id in haettavat_laitteet:
            laite_mallit.append(tiedot["malli"])

    return laite_mallit
# -------------------------------------------------------------------