import common
import common_tkinter
# -------------------------------------------------------------------
def uusi_teknikko(teknikko_frame, teknikko_muuttujat):
    """Luo uudelle teknikolle ID:n ja ottaa vastaan teknikon tiedot"""

    tiedosto = "teknikkotiedot.txt"
    # Lukee tiedostosta olemassa olevien teknikoiden tiedot sanakirjaan
    teknikot_sanakirja = common.avaa_tiedosto(tiedosto)

    # Laskee montako teknikkoa on jo olemassa ID:n luomista varten
    montako = common.id_lukumaara(teknikot_sanakirja)

    # Luo uudelle teknikolle ID-tunnuksen
    teknikko_id = common.luo_uusi_id("te-", montako)

    teknikko_avaimet = ["nimi", "puh.numero", "email"]

    teknikko_tiedot_lista = common.lue_tiedot(teknikko_muuttujat)

    # Kirjataan asiakkaan tiedot sanakirjaan
    sanakirja = common.lisaa_tiedot_sanakirjaan(teknikko_tiedot_lista, teknikko_avaimet)

    teknikot_sanakirja[teknikko_id] = sanakirja

    # Tallentaa teknikon tiedot tiedostoon
    common.tallenna_tiedostoon(teknikot_sanakirja, teknikko_id, tiedosto)
    common_tkinter.luo_label(teknikko_frame, "Teknikko tallennettu!", "white.TLabel", 0, 19, 100, 10, 10, 10)
# -------------------------------------------------------------------
def asiakkaat_valikko_nimet(asiakas_valikko):
    """Täytetään asiakkaiden nimet valikkoon"""

    asiakkaat_nimet = hae_mahdolliset_asiakkaat()

    common.aseta_valikko(asiakas_valikko, asiakkaat_nimet)
# -------------------------------------------------------------------
def hae_mahdolliset_asiakkaat():
    """Haetaan asiakkaiden nimet"""

    mahd_asiakas_idt = hae_mahd_asiakas_idt()

    asiakkaat = common.avaa_tiedosto("asiakastiedot.txt")
    mahd_asiakas_nimet = []

    for id, tiedot in asiakkaat.items():
        if id in mahd_asiakas_idt:
            mahd_asiakas_nimet.append(tiedot["nimi"])

    return mahd_asiakas_nimet
# -------------------------------------------------------------------
def hae_mahd_asiakas_idt():
    """Haetaan asiakkaiden ID:t, joilla on vastaanotettu tai työnalla oleva tiketti"""

    tiketit_sanakirja = common.avaa_tiedosto("tikettitiedot.txt")
    mahd_asiakas_idt = []

    for id, tiedot in tiketit_sanakirja.items():
        if tiedot["valmiusaste"] != "Valmis":

            if tiedot["asiakas_id"] not in mahd_asiakas_idt:
                mahd_asiakas_idt.append(tiedot["asiakas_id"])

    return mahd_asiakas_idt
# -------------------------------------------------------------------
def laitteet_valikko_mallit(event, asiakas_valikko, laite_valikko):
    """Täytetään asiakkaan laitteiden mallit valikkoon"""

    laitteet_idt_ja_mallit = laitteen_valinta(asiakas_valikko)

    laite_valikko.configure(values = laitteet_idt_ja_mallit[1])
    laite_valikko.set(laitteet_idt_ja_mallit[1][0])

    tiketti_id_ja_teknikko_id = vaihda_valittua_tikettia(asiakas_valikko, laite_valikko, laitteet_idt_ja_mallit)
# -------------------------------------------------------------------
def laitteen_valinta(asiakas_valikko):
    """Haetaan valitun asiakkaan laitteet, joiden tiketti on vastaanotettu tai työnalla"""

    valittu_asiakas_nimi = asiakas_valikko.get()

    valittu_asiakas_id = common.hae_id_tiedolla(valittu_asiakas_nimi, "nimi", "asiakastiedot.txt")

    tiketit_sanakirja = common.avaa_tiedosto("tikettitiedot.txt")

    haettavat_laite_idt = []
    # Haetaan asiakkaan laitteiden id:t tiketeistä
    for tiketti_id, tiedot in tiketit_sanakirja.items():
        if valittu_asiakas_id == tiedot["asiakas_id"]:
            if tiedot["valmiusaste"] != "Valmis":
                haettavat_laite_idt.append(tiedot["laite_id"])

    haettavat_laite_mallit = common.hae_tieto_lista("malli", "laitetiedot.txt", "id_lista", haettavat_laite_idt)
    print("laitteen_valinta - haettavat_laitteet_idt", haettavat_laite_idt)
    print("laitteen_valinta - haettavat_laite_mallit", haettavat_laite_mallit)

    return [haettavat_laite_idt, haettavat_laite_mallit]
# -------------------------------------------------------------------
def vaihda_valittua_tikettia(asiakas_valikko, laite_valikko, laite_idt_ja_mallit):
    """Hakee tiketin ID:n ja näyttää sen terminaalissa"""

    tiketti_id_ja_teknikko_id = hae_idt_valinnoilla(asiakas_valikko, laite_valikko, laite_idt_ja_mallit)

    return tiketti_id_ja_teknikko_id
# -------------------------------------------------------------------
def hae_idt_valinnoilla(asiakas_valikko, laite_valikko, laite_idt_ja_mallit):
    """Haetaan tiketin ID valitun laitteen ja asiakkaan perusteella"""

    valittu_laite_malli = laite_valikko.get()

    laskuri = 0
    for laite_id in laite_idt_ja_mallit[0]:
        if laite_idt_ja_mallit[1][laskuri] == valittu_laite_malli:
            valittu_laite_id = laite_id
        laskuri += 1

    valittu_asiakas_nimi = asiakas_valikko.get()
    valittu_asiakas_id = common.hae_id_tiedolla(valittu_asiakas_nimi, "nimi", "asiakastiedot.txt")

    tiketit_sanakirja = common.avaa_tiedosto("tikettitiedot.txt")

    for tiketti_id, tiedot in tiketit_sanakirja.items():
        if valittu_asiakas_id == tiedot["asiakas_id"]:
            if tiedot["valmiusaste"] != "Valmis":
                if tiedot["laite_id"] == valittu_laite_id:

                    return [tiketti_id, tiedot["teknikko_id"]]
# -------------------------------------------------------------------
def laitteet_valikko_event(event, asiakas_valikko, laite_valikko, valmiusaste_valikko, teknikko_valikko):
    """Vaihtaa tiketin ID:tä, kun valittua laitetta vaihdetaan"""

    laitteet_idt_ja_mallit = laitteen_valinta(asiakas_valikko)

    tiketti_id_ja_teknikko_id = vaihda_valittua_tikettia(asiakas_valikko, laite_valikko, laitteet_idt_ja_mallit)

    tiketin_valmiusaste = common.hae_tieto_id(tiketti_id_ja_teknikko_id[0], "valmiusaste", "tikettitiedot.txt")

    teknikon_nimi = common.hae_tieto_id(tiketti_id_ja_teknikko_id[1], "nimi", "teknikkotiedot.txt")

    valmiusasteet_lista = ["Vastaanotettu", "Työnalla", "Valmis"]

    if tiketin_valmiusaste == "Työnalla":
        valmiusasteet_lista = valmiusasteet_lista[1:]
        teknikko_valikko.set(teknikon_nimi)
        teknikko_valikko["state"] = "disabled"

    else:
        teknikko_valikko["state"] = "readonly"

    common.aseta_valikko(valmiusaste_valikko, valmiusasteet_lista)
# -------------------------------------------------------------------
def teknikot_valikko_nimet(teknikko_valikko):
    """Täytetään teknikkojen nimet valikkoon"""

    teknikot_nimet = common.hae_tieto_lista("nimi", "teknikkotiedot.txt", "erilaiset", [])

    common.aseta_valikko(teknikko_valikko, teknikot_nimet)
# -------------------------------------------------------------------
def tallenna_tiketti(teknikko_frame, asiakas_valikko, laite_valikko, valmiusaste_valikko, teknikko_valikko):

    tiedosto = "tikettitiedot.txt"
    tiketti_sanakirja = common.avaa_tiedosto(tiedosto)

    laitteet_idt_ja_mallit = laitteen_valinta(asiakas_valikko)
    tiketti_id_ja_teknikko_id = hae_idt_valinnoilla(asiakas_valikko, laite_valikko, laitteet_idt_ja_mallit)

    if tiketti_id_ja_teknikko_id[1] == "":
        teknikko_nimi = teknikko_valikko.get()
        teknikon_id = common.hae_id_tiedolla(teknikko_nimi, "nimi", "teknikkotiedot.txt")
    else:
        teknikon_id = tiketti_id_ja_teknikko_id[1]

    valmiusaste = valmiusaste_valikko.get()

    tiketti_sanakirja[tiketti_id_ja_teknikko_id[0]]["valmiusaste"] = valmiusaste
    tiketti_sanakirja[tiketti_id_ja_teknikko_id[0]]["teknikko_id"] = teknikon_id
    print("teknikon_id", teknikon_id)

    common.tallenna_tiedosto(tiketti_sanakirja, tiedosto)
    common_tkinter.luo_label(teknikko_frame, "Tiketti tallennettu!", "white.TLabel", 10, 19, 10, 10, 10, 10)
# -------------------------------------------------------------------


