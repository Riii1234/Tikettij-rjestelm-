import globals
import tkinter as tk
import common
from asiakkaat import uusi_asiakas
from laitteet import uusi_laite
from common_tkinter import tee_label_teksti
# -------------------------------------------------------------------
def uusi_tiketti():
    """Luo uudelle tiketille ID:n ja ottaa vastaan tiketin tiedot"""

    tiedosto = "tikettitiedot.txt"
    # Lukee tiedostosta olemassa olevien tikettien tiedot sanakirjaan
    tiketit_sanakirja = common.avaa_tiedosto(tiedosto)

    # Laskee montako tikettiä on jo olemassa ID:n luomista varten
    lukumaara = common.id_lukumaara(tiketit_sanakirja)

    # Luo uudelle tiketille ID-tunnuksen
    id = common.luo_uusi_id("ti-", lukumaara)

    return id
# -------------------------------------------------------------------
def tietojen_tallennus(tiketti_frame, tiketti_id, asiakkaan_tiedot, laitteen_tiedot, vikakuvaus_entry):
    """Tallentaa tiketin tiedot tiedostoon"""
    tiedosto = "tikettitiedot.txt"

    asiakas_tiedot_lista = common.lue_tiedot(asiakkaan_tiedot)
    laitteen_tiedot_lista = common.lue_tiedot(laitteen_tiedot)
    tiketin_tiedot_lista = []

    # Luetaan vikakuvaus entrystä
    vikakuvaus = vikakuvaus_entry.get("1.0" , tk.END)
    vikakuvaus = vikakuvaus[:-1]

    # Jos tarvittavia tietoja puuttuu
    if "" in asiakas_tiedot_lista or "" in laitteen_tiedot_lista[:-1] or vikakuvaus == "":
        tee_label_teksti(tiketti_frame, "Täytä puuttuvat tiedot!", 345, 550)

    else:
        tiketin_tiedot_lista = luo_tai_hae_id(globals.onko_uusi_asiakas, uusi_asiakas, asiakas_tiedot_lista, asiakkaan_tiedot, tiketin_tiedot_lista, "asiakastiedot.txt", "nimi")

        tiketin_tiedot_lista = luo_tai_hae_id(globals.onko_uusi_laite, uusi_laite, laitteen_tiedot_lista, laitteen_tiedot, tiketin_tiedot_lista, "laitetiedot.txt", "malli")

        tiketin_tiedot_lista.append("Vastaanotettu")
        # Tikettiä työstävä teknikko on tikettiä luotaessa tyhjä
        tiketin_tiedot_lista.append("")
        tiketin_tiedot_lista.append(vikakuvaus)

        tiketin_tiedot_nimikkeet = ["asiakas_id", "laite_id", "valmiusaste", "teknikko_id", "vika"]
        # Kirjataan asiakkaan tiedot sanakirjaan
        sanakirja = common.lisaa_tiedot_sanakirjaan(tiketin_tiedot_lista, tiketin_tiedot_nimikkeet)

        tiketit_sanakirja = common.avaa_tiedosto(tiedosto)

        tiketit_sanakirja[tiketti_id] = sanakirja
    
        # Tallentaa tiketin tiedot tiedostoon
        common.tallenna_tiedostoon(tiketit_sanakirja, tiketti_id, tiedosto)
        tee_label_teksti(tiketti_frame, "Tiedot tallennettu!", 345, 550)
        print("tietojen_tallennus onnistui")
# -------------------------------------------------------------------
def luo_tai_hae_id(onko_uusi, uusi_funtio, tiedot_lista, tiedot, tiketin_tiedot_lista, tiedosto, nimike):
    """Luodaan tai haetaan asiakas_id tai laite_id"""
    # Jos asiakas/laite on uusi, luodaan uusi asiakas_id/laite_id ja tallennetaan asiakkaan/laitteen tiedot tiedostoon
    if onko_uusi == True:
        id = uusi_funtio(tiedot_lista)
        tiketin_tiedot_lista.append(id)
    else:
        id = common.hae_id(tiedot, tiedosto, nimike)
        tiketin_tiedot_lista.append(id)

    return tiketin_tiedot_lista
# -------------------------------------------------------------------