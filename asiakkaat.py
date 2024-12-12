import globals
import common
import laitteet
import tkinter as tk
# -------------------------------------------------------------------
def luo_uusi_asiakas(asiakas_tiedot_lista):
    """Luo uudelle asiakkaalle ID:n ja ottaa vastaan asiakkaan tiedot"""

    tiedosto = "asiakastiedot.txt"
    # Lukee tiedostosta olemassa olevien asiakkaiden tiedot sanakirjaan
    asiakas_sanakirja = common.avaa_tiedosto(tiedosto)

    asiakas_lukumaara = common.laske_id_lukumaara(asiakas_sanakirja)
    id = common.luo_uusi_id("as-", asiakas_lukumaara)

    asiakas_avaimet = ["nimi", "osoite", "puh.numero", "email"]

    # Kirjataan asiakkaan tiedot sanakirjaan
    sanakirja = common.lisaa_tiedot_sanakirjaan(asiakas_tiedot_lista, asiakas_avaimet)

    print("uusi_asiakas sanakirja", sanakirja)
    asiakas_sanakirja[id] = sanakirja

    # Tallentaa asiakkaan tiedot tiedostoon
    common.tallenna_tiedostoon(asiakas_sanakirja, id, tiedosto)
    return id
# -------------------------------------------------------------------
def hae_vanha_asiakas(asiakas_muuttujat, asiakas_entryt, vanhat_laitteet_valikko):
    """Haetaan vanhan asiakkaan tiedot ID:llä ja sijoitetaan entry-muuttujiin näkymään terminaaliin"""

    asiakas_id = common.hae_id(asiakas_muuttujat, "asiakastiedot.txt", "nimi")

    # Tyhjä string, jos nimeä ei löytynyt
    if asiakas_id == "":
        return
    else:
        tiedot = common.hae_tiedot(asiakas_id, "", "asiakastiedot.txt", "id")
        globals.onko_uusi_asiakas = False

        lista = ["nimi", "osoite", "puh.numero", "email"]
        #print("vanha_asiakas here2")
        for i in range(0, 4):

            asiakas_entryt[i].delete(0, tk.END)
            # Sijoitetaan tiedot terminaaliin
            asiakas_entryt[i].insert(0, tiedot[lista[i]])

        laitteet.aseta_vanhat_laitteet_valikko(asiakas_muuttujat, vanhat_laitteet_valikko)
# -------------------------------------------------------------------