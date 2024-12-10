import globals
import common
import tkinter as tk
# -------------------------------------------------------------------
"""Luo uudelle laitteelle ID:n ja ottaa vastaan laitteen tiedot"""
def uusi_laite(laitteen_tiedot_lista):

    tiedosto = "laitetiedot.txt"
    # Lukee tiedostosta olemassa olevien laitteiden tiedot sanakirjaan
    laitteet_sanakirja = common.avaa_tiedosto(tiedosto)

    # Laskee montako laitetta on jo olemassa ID:n luomista varten
    montako = common.id_lukumaara(laitteet_sanakirja)

    # Luo uudelle laitteelle ID-tunnuksen
    id = common.luo_uusi_id("la-", montako)

    laitteen_tiedot_nimikkeet = ["malli", "tyyppi", "sarjanumero", "tuotetunnus", "lisa"]
    # Kirjataan laitteen tiedot sanakirjaan
    sanakirja = common.lisaa_tiedot_sanakirjaan(laitteen_tiedot_lista, laitteen_tiedot_nimikkeet)

    print("uusi_laite sanakirja", sanakirja)
    laitteet_sanakirja[id] = sanakirja

    # Tallentaa laitteen tiedot tiedostoon
    common.tallenna_tiedostoon(laitteet_sanakirja, id, tiedosto)
    return id
# -------------------------------------------------------------------
"""Hakee vanhan laitteen tiedot mallin avulla"""
def vanha_laite(laitteen_entryt, asiakkaan_tiedot, laite_malli):

    haettavat_laitteet = vanhat_laitteet(asiakkaan_tiedot)

    laitteet_sanakirja = common.avaa_tiedosto("laitetiedot.txt")
    
    print("vanha_laite laite_malli", laite_malli)
    lista = ["malli", "tyyppi", "sarjanumero", "tuotetunnus", "lisa"]
    # Tiedot sisältävät laite_id, malli, tyyppi, sarjanumero, tuotetunnus ja lisätiedot
    for id, tiedot in laitteet_sanakirja.items():
        if id in haettavat_laitteet:

            if laite_malli == tiedot["malli"]:
                globals.onko_uusi_laite = False

                for i in range(0, 5):
                    # Sijoitetaan tiedot terminaaliin
                    laitteen_entryt[i].delete(0, tk.END)
                    laitteen_entryt[i].insert(0, tiedot[lista[i]])

# -------------------------------------------------------------------
"""Hakee laitteen mallin entry-widgetistä"""
def vanhat_laitteet_nappi(laitteen_malli, laitteen_entryt, asiakkaan_tiedot):

    laite_malli = laitteen_malli.get()
    print("vanhat_laitteet_nappi - laite_malli", laite_malli)

    vanha_laite(laitteen_entryt, asiakkaan_tiedot, laite_malli)
# -------------------------------------------------------------------
"""Antaa tällä hetkellä valitun laitteen valikosta"""
def vanha_laite_valikko(event, laitteen_entryt, asiakkaan_tiedot, vanhat_laitteet_combobox):

    laite_malli = vanhat_laitteet_combobox.get()

    vanha_laite(laitteen_entryt, asiakkaan_tiedot, laite_malli)
# -------------------------------------------------------------------
"""Hakee vanhat laitteet asiakkaan ID:llä"""
def vanhat_laitteet(asiakkaan_tiedot):

    #print("vanhat_laitteet asiakkaan_tiedot", asiakkaan_tiedot)

    asiakas_id = common.hae_id(asiakkaan_tiedot, "asiakastiedot.txt", "nimi")
    print("vanhat_laitteet asiakas_id", asiakas_id)
  
    tiketit_sanakirja = common.avaa_tiedosto("tikettitiedot.txt")
    # Haetaan kaikki asiakkaan laitteet tiketeistä
    haettavat_laitteet = []
    for tiketti, tiedot in tiketit_sanakirja.items():
        if asiakas_id == tiedot["asiakas_id"]:
            haettavat_laitteet.append(tiedot["laite_id"])

    return haettavat_laitteet
# -------------------------------------------------------------------
"""Asettaa asiakkaan vanhat laitteet valikkoon"""
def vanhat_laitteet_valikko(asiakkaan_tiedot, vanhat_laitteet_combobox):

    laitteet_lista = vanhat_laite_mallit(asiakkaan_tiedot)
    
    vanhat_laitteet_combobox.configure(values = laitteet_lista)
    vanhat_laitteet_combobox.set(laitteet_lista[0])
# -------------------------------------------------------------------
"""Hakee laitteiden mallit"""
def vanhat_laite_mallit(asiakkaan_tiedot):

    haettavat_laitteet = vanhat_laitteet(asiakkaan_tiedot)

    laitteet_sanakirja = common.avaa_tiedosto("laitetiedot.txt")
    laite_mallit = []

    for id, tiedot in laitteet_sanakirja.items():
        if id in haettavat_laitteet:
            laite_mallit.append(tiedot["malli"])

    return laite_mallit
# -------------------------------------------------------------------

if __name__ == "__main__":

    uusi_laite()
