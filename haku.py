import tkinter as tk
import common
# -------------------------------------------------------------------
def hae_asiakkaan_tiedot(asiakas_entryt, asiakastieto_kentta):
    """Asiakkaan tietojen haku ID:n, nimen tai emailin perusteella"""

    tiedosto = "asiakastiedot.txt"

    asiakas_nimi = asiakas_entryt[0].get()
    asiakas_email = asiakas_entryt[1].get()

    asiakas_tekstit = ["Nimi:", "Osoite:", "Puh.numero:", "Email:"]
    asiakas_avaimet = ["nimi", "osoite", "puh.numero", "email"]
    montako_valia = [12, 9, 1, 11]

    if asiakas_nimi != "":

        tiedot = common.hae_tiedot(asiakas_nimi, "nimi", tiedosto)
        tietojen_taytto(asiakastieto_kentta, tiedot, asiakas_avaimet, asiakas_tekstit, montako_valia)

    elif asiakas_email != "":

        tiedot = common.hae_tiedot(asiakas_email, "email", tiedosto)
        tietojen_taytto(asiakastieto_kentta, tiedot, asiakas_avaimet, asiakas_tekstit, montako_valia)
# -------------------------------------------------------------------
def tietojen_taytto(tieto_kentta, tiedot, avaimet, tekstit, montako_valia):

    tieto_kentta.delete('1.0', tk.END)

    i = 0
    vali = " "
    while i < len(tekstit):
        if i < len(tekstit) - 1:
            # Sijoitetaan tiedot terminaaliin
            tieto_kentta.insert(tk.END, f"{tekstit[i]} {vali * montako_valia[i]} {tiedot[avaimet[i]]}\n")
        else:
            tieto_kentta.insert(tk.END, f"{tekstit[i]} {vali * montako_valia[i]} {tiedot[avaimet[i]]}")
        i += 1
# -------------------------------------------------------------------
def hae_laitteen_tiedot(laitteen_entry, laitetieto_kentta):
    """Laitteen tietojen haku ID:n tai sarjanumeron perusteella"""

    tiedosto = "laitetiedot.txt"

    laitteen_sarjanumero = laitteen_entry[0].get()

    laitteen_tekstit = ["Malli:", "Tyyppi:", "Sarjanumero:", "Tuotetunnus:", "Lisätiedot:"]
    laitteen_avaimet = ["malli", "tyyppi", "sarjanumero", "tuotetunnus", "lisa"]
    montako_valia = [13, 10, 1, 2, 6]

    if laitteen_sarjanumero != "":

        tiedot = common.hae_tiedot(laitteen_sarjanumero, "sarjanumero", tiedosto)
        tietojen_taytto(laitetieto_kentta, tiedot, laitteen_avaimet, laitteen_tekstit, montako_valia)
# -------------------------------------------------------------------
def laitteet_valikko(laite_combobox, milla_tiedolla):
    """Luo valikot laitetyypeille ja -malleille"""

    tiedosto = "laitetiedot.txt"

    tiedot = common.hae_tiedot_kaikkien_erit(milla_tiedolla, tiedosto)

    laite_combobox.configure(values = tiedot)
    laite_combobox.set(tiedot[0])
# -------------------------------------------------------------------
def laitteet_valikko_event(event, laite_combobox, tieto_avain, laitetieto_kentta):
    """Useamman laitteen haku laitetyypin tai laitemallin perusteella"""

    tiedosto = "laitetiedot.txt"

    mika_tieto = laite_combobox.get()

    tiedot_lista = common.hae_tietoja(mika_tieto, tieto_avain, tiedosto)

    laitteen_tekstit = ["Malli:", "Tyyppi:", "Sarjanumero:", "Tuotetunnus:", "Lisätiedot:"]
    laitteen_avaimet = ["malli", "tyyppi", "sarjanumero", "tuotetunnus", "lisa"]
    montako_valia = [13, 10, 1, 2, 6]

    tietojen_taytto_useat(laitetieto_kentta, tiedot_lista, laitteen_avaimet, laitteen_tekstit, mika_tieto, montako_valia)
# -------------------------------------------------------------------
def tietojen_taytto_useat(tieto_kentta, tiedot_lista, avaimet, tekstit, mika_tieto, montako_valia):
    """Täyttää tiedot entryyn"""

    tieto_kentta.delete('1.0', tk.END)

    laskuri = 0
    for tiedot in tiedot_lista:

        if laskuri % 2 == 0:
            laskuri += 1
        elif laskuri < len(tiedot_lista) - 1:
            tietojen_taytto_entryyn(tiedot, tieto_kentta, avaimet, tekstit, mika_tieto, "\n\n", montako_valia)
            laskuri += 1
        else:
            tietojen_taytto_entryyn(tiedot, tieto_kentta, avaimet, tekstit, mika_tieto, "", montako_valia)
# -------------------------------------------------------------------
def tietojen_taytto_entryyn(tiedot, tieto_kentta, avaimet, tekstit, mika_tieto, rivinvaihto, montako_valia):
    i = 0
    vali = " "

    while i < len(tekstit) - 1:
        if tiedot[avaimet[i]] != mika_tieto:
            # Sijoitetaan tiedot terminaaliin
            tieto_kentta.insert(tk.END, f"{tekstit[i]} {vali * montako_valia[i]} {tiedot[avaimet[i]]}\n")
        i += 1
    else:
        tieto_kentta.insert(tk.END, f"{tekstit[i]} {vali * montako_valia[i]} {tiedot[avaimet[i]]}{rivinvaihto}")
# -------------------------------------------------------------------
def tietojen_taytto_useat_id(tieto_kentta, tiedot_lista, avaimet, tekstit, mika_tieto, tiketin_id_teksti, montako_valia):
    """Täyttää tiedot entryyn + tiketin ID"""

    tieto_kentta.delete('1.0', tk.END)

    laskuri = 0
    for tiedot in tiedot_lista:
        
        if laskuri % 2 == 0:
            tieto_kentta.insert(tk.END, f"{tiketin_id_teksti} {" "*18} {tiedot}\n")
            laskuri += 1

        elif laskuri < len(tiedot_lista) - 1:
            tietojen_taytto_entryyn(tiedot, tieto_kentta, avaimet, tekstit, mika_tieto, "\n\n", montako_valia)
            laskuri += 1
        else:
            tietojen_taytto_entryyn(tiedot, tieto_kentta, avaimet, tekstit, mika_tieto, "", montako_valia)
# -------------------------------------------------------------------
def tiketit_haku_valmiusaste(valmiusaste_combobox):
    """Valmiusasteiden asetus valikkoon"""

    tiedot = ["Vastaanotettu", "Työnalla", "Valmis"]

    valmiusaste_combobox.configure(values = tiedot)
    valmiusaste_combobox.set(tiedot[0])
# -------------------------------------------------------------------
def valmiusaste_valikko_event(event, valmiusaste_combobox, tikettitieto_kentta):
    """Tikettien tietojen haku valmiusasteen perusteella"""

    tiedosto = "tikettitiedot.txt"

    valittu_valmiusaste = valmiusaste_combobox.get()

    tiketin_id_teksti = "Tiketin ID:"
    tiketin_tekstit = ["Asiakkaan nimi:", "Laitteen sarjanumero:", "Valmiusaste:", "Teknikon nimi:", "Laitteen vika:"]
    tiketin_avaimet = ["asiakas_nimi", "laite_sarjanumero", "valmiusaste", "teknikko_nimi", "vika"]
    montako_valia = [9, 1, 0, 11, 13]

    tiketin_tiedot_lista = common.hae_tietoja(valittu_valmiusaste, "valmiusaste", tiedosto)

    tiedot_lista = asiakas_nimet_ja_laite_sarjanumerot(tiketin_tiedot_lista)

    tietojen_taytto_useat_id(tikettitieto_kentta, tiedot_lista, tiketin_avaimet, tiketin_tekstit, valittu_valmiusaste, tiketin_id_teksti, montako_valia)
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
