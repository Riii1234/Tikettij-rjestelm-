import globals
import tkinter as tk
import common
import common_tkinter
import asiakkaat
import laitteet
# -------------------------------------------------------------------
def luo_uusi_tiketti():
    """Luo uudelle tiketille ID:n"""

    # Lukee tiedostosta olemassa olevien tikettien tiedot sanakirjaan
    tiketti_sanakirja = common.avaa_tiedosto("tikettitiedot.txt")

    # Laskee montako tikettiä on jo olemassa ID:n luomista varten
    lukumaara = common.laske_id_lukumaara(tiketti_sanakirja)

    # Luo uudelle tiketille ID-tunnuksen
    id = common.luo_uusi_id("ti-", lukumaara)

    return id
# -------------------------------------------------------------------
def tallenna_tiedot(tiketti_frame, tiketti_id, asiakas_muuttujat, laite_muuttujat, vikakuvaus_entry):
    """Tallentaa tiketin tiedot tiedostoon"""
    tiedosto = "tikettitiedot.txt"

    asiakas_tiedot_lista = common.lue_tiedot(asiakas_muuttujat)
    laite_tiedot_lista = common.lue_tiedot(laite_muuttujat)
    tiketti_tiedot_lista = []

    # Luetaan vikakuvaus entrystä
    vikakuvaus_teksti = vikakuvaus_entry.get("1.0" , tk.END)
    vikakuvaus_teksti = vikakuvaus_teksti[:-1]

    # Jos tarvittavia tietoja puuttuu
    if "" in asiakas_tiedot_lista or "" in laite_tiedot_lista[:-1] or vikakuvaus_teksti == "":
        #tee_label_teksti(tiketti_frame, "Täytä puuttuvat tiedot!", 345, 550)
        pass

    else:
        tiketti_tiedot_lista = luo_tai_hae_id(globals.onko_uusi_asiakas, asiakkaat.luo_uusi_asiakas, asiakas_tiedot_lista, asiakas_muuttujat, tiketti_tiedot_lista, "asiakastiedot.txt", "nimi")

        tiketti_tiedot_lista = luo_tai_hae_id(globals.onko_uusi_laite, laitteet.luo_uusi_laite, laite_tiedot_lista, laite_muuttujat, tiketti_tiedot_lista, "laitetiedot.txt", "malli")

        tiketti_tiedot_lista.append("Vastaanotettu")
        # Tikettiä työstävä teknikko on tikettiä luotaessa tyhjä
        tiketti_tiedot_lista.append("")
        tiketti_tiedot_lista.append(vikakuvaus_teksti)

        tiketti_avaimet = ["asiakas_id", "laite_id", "valmiusaste", "teknikko_id", "vika"]
        # Kirjataan asiakkaan tiedot sanakirjaan
        sanakirja = common.lisaa_tiedot_sanakirjaan(tiketti_tiedot_lista, tiketti_avaimet)

        tiketti_sanakirja = common.avaa_tiedosto(tiedosto)

        tiketti_sanakirja[tiketti_id] = sanakirja
    
        # Tallentaa tiketin tiedot tiedostoon
        common.tallenna_tiedostoon(tiketti_sanakirja, tiketti_id, tiedosto)
        common_tkinter.luo_label(tiketti_frame, "Tiedot tallennettu!", "white.TLabel", 10, 24, 10, 10, 10, 10)
        print("tietojen_tallennus onnistui")
# -------------------------------------------------------------------
def luo_tai_hae_id(onko_uusi, uusi_funtio, tiedot_lista, muuttujat, tiketti_tiedot_lista, tiedosto, avain):
    """Luodaan tai haetaan asiakas_id tai laite_id"""
    # Jos asiakas/laite on uusi, luodaan uusi asiakas_id/laite_id ja tallennetaan asiakkaan/laitteen tiedot tiedostoon
    if onko_uusi == True:
        id = uusi_funtio(tiedot_lista)
        tiketti_tiedot_lista.append(id)
    else:
        id = common.hae_id(muuttujat, tiedosto, avain)
        tiketti_tiedot_lista.append(id)

    return tiketti_tiedot_lista
# -------------------------------------------------------------------