import common
import common_tkinter
# -------------------------------------------------------------------
# Luo uudelle teknikolle ID:n ja ottaa vastaan teknikon tiedot
def uusi_teknikko(teknikon_tiedot):

    tiedosto = "teknikkotiedot.txt"
    # Lukee tiedostosta olemassa olevien teknikoiden tiedot sanakirjaan
    teknikot_sanakirja = common.avaa_tiedosto(tiedosto)

    # Laskee montako teknikkoa on jo olemassa ID:n luomista varten
    montako = common.id_lukumaara(teknikot_sanakirja)

    # Luo uudelle teknikolle ID-tunnuksen
    teknikon_id = common.luo_uusi_id("te-", montako)

    teknikon_tieto_nimikkeet = ["nimi", "puh.numero", "email"]

    teknikon_tiedot_lista = common.lue_tiedot(teknikon_tiedot)

    # Kirjataan asiakkaan tiedot sanakirjaan
    sanakirja = common.lisaa_tiedot_sanakirjaan(teknikon_tiedot_lista, teknikon_tieto_nimikkeet)

    teknikot_sanakirja[teknikon_id] = sanakirja

    # Tallentaa teknikon tiedot tiedostoon
    common.tallenna_tiedostoon(teknikot_sanakirja, teknikon_id, tiedosto)
# -------------------------------------------------------------------
# Täytetään asiakkaiden nimet valikkoon
def asiakkaat_valikko_nimet(asiakkaat_combobox):

    asiakkaat_nimet = hae_mahdolliset_asiakkaat()

    asiakkaat_combobox.configure(values = asiakkaat_nimet)
    asiakkaat_combobox.set(asiakkaat_nimet[0])
# -------------------------------------------------------------------
# Haetaan asiakkaiden nimet
def hae_mahdolliset_asiakkaat():

    mahd_asiakas_idt = hae_mahd_asiakas_idt()

    asiakkaat = common.avaa_tiedosto("asiakastiedot.txt")
    mahd_asiakas_nimet = []

    for id, tiedot in asiakkaat.items():
        if id in mahd_asiakas_idt:
            mahd_asiakas_nimet.append(tiedot["nimi"])

    return mahd_asiakas_nimet
# -------------------------------------------------------------------
# Haetaan asiakkaiden ID:t, joilla on vastaanotettu tai työnalla oleva tiketti
def hae_mahd_asiakas_idt():

    tiketit_sanakirja = common.avaa_tiedosto("tikettitiedot.txt")
    mahd_asiakas_idt = []

    for id, tiedot in tiketit_sanakirja.items():
        if tiedot["valmiusaste"] != "Valmis":

            if tiedot["asiakas_id"] not in mahd_asiakas_idt:
                mahd_asiakas_idt.append(tiedot["asiakas_id"])

    return mahd_asiakas_idt
# -------------------------------------------------------------------
# Täytetään asiakkaan laitteiden mallit valikkoon
def laitteet_valikko_mallit(event, teknikot_frame, asiakkaat_combobox, laitteet_combobox):

    laitteet_idt_ja_mallit = laitteen_valinta(asiakkaat_combobox)

    laitteet_combobox.configure(values = laitteet_idt_ja_mallit[1])
    laitteet_combobox.set(laitteet_idt_ja_mallit[1][0])

    tiketti_id_ja_teknikko_id = vaihda_valittua_tikettia(teknikot_frame, asiakkaat_combobox, laitteet_combobox, laitteet_idt_ja_mallit)
# -------------------------------------------------------------------
# Haetaan valitun asiakkaan laitteet, joiden tiketti on vastaanotettu tai työnalla
def laitteen_valinta(asiakkaat_combobox):

    valittu_asiakas_nimi = asiakkaat_combobox.get()

    valittu_asiakas_id = common.hae_id_tiedolla(valittu_asiakas_nimi, "nimi", "asiakastiedot.txt")

    tiketit_sanakirja = common.avaa_tiedosto("tikettitiedot.txt")

    haettavat_laitteet_idt = []
    # Haetaan asiakkaan laitteiden id:t tiketeistä
    for tiketti_id, tiedot in tiketit_sanakirja.items():
        if valittu_asiakas_id == tiedot["asiakas_id"]:
            if tiedot["valmiusaste"] != "Valmis":
                haettavat_laitteet_idt.append(tiedot["laite_id"])

    haettavat_laitteet_mallit = common.hae_mahd_tieto_kaikki(haettavat_laitteet_idt, "malli", "laitetiedot.txt")

    return [haettavat_laitteet_idt, haettavat_laitteet_mallit]
# -------------------------------------------------------------------
# Hakee tiketin ID:n ja näyttää sen terminaalissa
def vaihda_valittua_tikettia(teknikot_frame, asiakkaat_combobox, laitteet_combobox, laitteet_idt_ja_mallit):

    tiketti_id_ja_teknikko_id = hae_idt_valinnoilla(asiakkaat_combobox, laitteet_combobox, laitteet_idt_ja_mallit)

    common_tkinter.tee_label_teksti(teknikot_frame, f" Tiketin ID: {tiketti_id_ja_teknikko_id[0]} ", 500, 390)

    return tiketti_id_ja_teknikko_id
# -------------------------------------------------------------------
# Haetaan tiketin ID valitun laitteen ja asiakkaan perusteella
def hae_idt_valinnoilla(asiakkaat_combobox, laitteet_combobox, laitteet_idt_ja_mallit):

    valittu_laite_malli = laitteet_combobox.get()

    laskuri = 0
    for laite_id in laitteet_idt_ja_mallit[0]:
        if laitteet_idt_ja_mallit[1][laskuri] == valittu_laite_malli:
            valittu_laite_id = laite_id
        laskuri += 1

    valittu_asiakas_nimi = asiakkaat_combobox.get()
    valittu_asiakas_id = common.hae_id_tiedolla(valittu_asiakas_nimi, "nimi", "asiakastiedot.txt")

    tiketit_sanakirja = common.avaa_tiedosto("tikettitiedot.txt")

    for tiketti_id, tiedot in tiketit_sanakirja.items():
        if valittu_asiakas_id == tiedot["asiakas_id"]:
            if tiedot["valmiusaste"] != "Valmis":
                if tiedot["laite_id"] == valittu_laite_id:
                    print("tiedot[teknikko_id]", tiedot["teknikko_id"])
                    print("tiedot", tiedot)

                    return [tiketti_id, tiedot["teknikko_id"]]
# -------------------------------------------------------------------
# Vaihtaa tiketin ID:tä, kun valittua laitetta vaihdetaan
def laitteet_valikko_event(event, teknikot_frame, asiakkaat_combobox, laitteet_combobox, valmiusasteet_combobox, teknikot_combobox):

    laitteet_idt_ja_mallit = laitteen_valinta(asiakkaat_combobox)

    tiketti_id_ja_teknikko_id = vaihda_valittua_tikettia(teknikot_frame, asiakkaat_combobox, laitteet_combobox, laitteet_idt_ja_mallit)

    tiketin_valmiusaste = common.hae_tieto_id(tiketti_id_ja_teknikko_id[0], "valmiusaste", "tikettitiedot.txt")

    teknikon_nimi = common.hae_tieto_id(tiketti_id_ja_teknikko_id[1], "nimi", "teknikkotiedot.txt")

    valmiusasteet_lista = ["Vastaanotettu", "Työnalla", "Valmis"]

    if tiketin_valmiusaste == "Työnalla":
        valmiusasteet_lista = valmiusasteet_lista[1:]
        teknikot_combobox.set(teknikon_nimi)
        teknikot_combobox["state"] = "disabled"

    else:
        teknikot_combobox["state"] = "readonly"

    valmiusasteet_combobox.configure(values = valmiusasteet_lista)
    valmiusasteet_combobox.set(valmiusasteet_lista[0])
# -------------------------------------------------------------------
# Täytetään teknikkojen nimet valikkoon
def teknikot_valikko_nimet(teknikot_combobox):

    teknikot_nimet = common.hae_tiedot_kaikkien("nimi", "teknikkotiedot.txt")

    teknikot_combobox.configure(values = teknikot_nimet)
    teknikot_combobox.set(teknikot_nimet[0])
# -------------------------------------------------------------------
def tallenna_tiketti(asiakkaat_combobox, laitteet_combobox, valmiusasteet_combobox, teknikot_combobox):

    tiedosto = "tikettitiedot.txt"
    tiketti_sanakirja = common.avaa_tiedosto(tiedosto)

    laitteet_idt_ja_mallit = laitteen_valinta(asiakkaat_combobox)
    tiketti_id_ja_teknikko_id = hae_idt_valinnoilla(asiakkaat_combobox, laitteet_combobox, laitteet_idt_ja_mallit)

    if tiketti_id_ja_teknikko_id[1] == "":
        teknikko_nimi = teknikot_combobox.get()
        teknikon_id = common.hae_id_tiedolla(teknikko_nimi, "nimi", "teknikkotiedot.txt")
    else:
        teknikon_id = tiketti_id_ja_teknikko_id[1]

    valmiusaste = valmiusasteet_combobox.get()

    tiketti_sanakirja[tiketti_id_ja_teknikko_id[0]]["valmiusaste"] = valmiusaste
    tiketti_sanakirja[tiketti_id_ja_teknikko_id[0]]["teknikko_id"] = teknikon_id
    print("teknikon_id", teknikon_id)

    common.tallenna_tiedosto(tiketti_sanakirja, tiedosto)
# -------------------------------------------------------------------


