import globals
import common
from laitteet import vanhat_laitteet_valikko
import tkinter as tk
# -------------------------------------------------------------------
"""Luo uudelle asiakkaalle ID:n ja ottaa vastaan asiakkaan tiedot"""
def uusi_asiakas(asiakas_tiedot_lista):

    tiedosto = "asiakastiedot.txt"
    # Lukee tiedostosta olemassa olevien asiakkaiden tiedot sanakirjaan
    asiakkaat_sanakirja = common.avaa_tiedosto(tiedosto)

    asiakkaat_lukumaara = common.id_lukumaara(asiakkaat_sanakirja)
    id = common.luo_uusi_id("as-", asiakkaat_lukumaara)

    asiakas_tieto_nimikkeet = ["nimi", "osoite", "puh.numero", "email"]

    # Kirjataan asiakkaan tiedot sanakirjaan
    sanakirja = common.lisaa_tiedot_sanakirjaan(asiakas_tiedot_lista, asiakas_tieto_nimikkeet)

    print("uusi_asiakas sanakirja", sanakirja)
    asiakkaat_sanakirja[id] = sanakirja

    # Tallentaa asiakkaan tiedot tiedostoon
    common.tallenna_tiedostoon(asiakkaat_sanakirja, id, tiedosto)
    return id
# -------------------------------------------------------------------
"""Haetaan vanhan asiakkaan tiedot ID:llä ja sijoitetaan entry-muuttujiin näkymään terminaaliin"""
def vanha_asiakas(asiakkaan_tiedot, asiakkaan_entryt, vanhat_laitteet_combobox):

    asiakas_id = common.hae_id(asiakkaan_tiedot, "asiakastiedot.txt", "nimi")

    # Tyhjä string, jos nimeä ei löytynyt
    if asiakas_id == "":
        return
    else:
        tiedot = common.hae_tiedot_id(asiakas_id, "asiakastiedot.txt")
        globals.onko_uusi_asiakas = False

        lista = ["nimi", "osoite", "puh.numero", "email"]
        #print("vanha_asiakas here2")
        for i in range(0, 4):

            asiakkaan_entryt[i].delete(0, tk.END)
            # Sijoitetaan tiedot terminaaliin
            asiakkaan_entryt[i].insert(0, tiedot[lista[i]])

        vanhat_laitteet_valikko(asiakkaan_tiedot, vanhat_laitteet_combobox)
# -------------------------------------------------------------------

if __name__ == "__main__":

    uusi_asiakas()
