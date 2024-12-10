import tkinter as tk
import common
# -------------------------------------------------------------------
"""Asiakkaan tietojen haku ID:n, nimen tai emailin perusteella"""
def hae_asiakkaan_tiedot(asiakkaan_entryt, asiakastiedot_entry):

    tiedosto = "asiakastiedot.txt"

    asiakkaan_id = asiakkaan_entryt[0].get()
    asiakkaan_nimi = asiakkaan_entryt[1].get()
    asiakkaan_email = asiakkaan_entryt[2].get()

    asiakkaan_tekstit = ["Nimi:", "Osoite:", "Puh.numero:", "Email:"]
    asiakkaan_nimikkeet = ["nimi", "osoite", "puh.numero", "email"]

    if asiakkaan_id != "":

        tiedot = common.hae_tiedot_id(asiakkaan_id, tiedosto)
        tietojen_taytto(asiakastiedot_entry, tiedot, asiakkaan_nimikkeet, asiakkaan_tekstit)

    elif asiakkaan_nimi != "":

        tiedot = common.hae_tiedot(asiakkaan_nimi, "nimi", tiedosto)
        tietojen_taytto(asiakastiedot_entry, tiedot, asiakkaan_nimikkeet, asiakkaan_tekstit)

    elif asiakkaan_email != "":

        tiedot = common.hae_tiedot(asiakkaan_email, "email", tiedosto)
        tietojen_taytto(asiakastiedot_entry, tiedot, asiakkaan_nimikkeet, asiakkaan_tekstit)
# -------------------------------------------------------------------
def tietojen_taytto(tiedot_entry, tiedot, nimikkeet, tekstit):

    tiedot_entry.delete('1.0', tk.END)

    i = 0
    while i < len(tekstit):
        if i < len(tekstit) - 1:
            # Sijoitetaan tiedot terminaaliin
            tiedot_entry.insert(tk.END, f"{tekstit[i]} {tiedot[nimikkeet[i]]}\n")
        else:
            tiedot_entry.insert(tk.END, f"{tekstit[i]} {tiedot[nimikkeet[i]]}")
        i += 1
# -------------------------------------------------------------------
"""Laitteen tietojen haku ID:n tai sarjanumeron perusteella"""
def hae_laitteen_tiedot(laitteen_entry, laitteet_tiedot_entry):

    tiedosto = "laitetiedot.txt"

    laitteen_sarjanumero = laitteen_entry[0].get()

    laitteen_tekstit = ["Malli:", "Tyyppi:", "Sarjanumero:", "Tuotetunnus:", "Lisätiedot:"]
    laitteen_nimikkeet = ["malli", "tyyppi", "sarjanumero", "tuotetunnus", "lisa"]

    if laitteen_sarjanumero != "":

        tiedot = common.hae_tiedot(laitteen_sarjanumero, "sarjanumero", tiedosto)
        tietojen_taytto(laitteet_tiedot_entry, tiedot, laitteen_nimikkeet, laitteen_tekstit)
# -------------------------------------------------------------------
"""Luo valikot laitetyypeille ja -malleille"""
def laitteet_valikko(laite_combobox, milla_tiedolla):

    tiedosto = "laitetiedot.txt"

    tiedot = common.hae_tiedot_kaikkien_erit(milla_tiedolla, tiedosto)

    laite_combobox.configure(values = tiedot)
    laite_combobox.set(tiedot[0])
# -------------------------------------------------------------------
"""Useamman laitteen haku laitetyypin tai laitemallin perusteella"""
def laitteet_valikko_event(event, laite_combobox, tieto_nimike, laitteet_tiedot_entry):

    tiedosto = "laitetiedot.txt"

    mika_tieto = laite_combobox.get()

    tiedot_lista = common.hae_tietoja(mika_tieto, tieto_nimike, tiedosto)

    laitteen_tekstit = ["Malli:", "Tyyppi:", "Sarjanumero:", "Tuotetunnus:", "Lisätiedot:"]
    laitteen_nimikkeet = ["malli", "tyyppi", "sarjanumero", "tuotetunnus", "lisa"]

    tietojen_taytto_useat(laitteet_tiedot_entry, tiedot_lista, laitteen_nimikkeet, laitteen_tekstit, mika_tieto)
# -------------------------------------------------------------------
"""Täyttää tiedot entryyn"""
def tietojen_taytto_useat(tiedot_entry, tiedot_lista, nimikkeet, tekstit, mika_tieto):

    tiedot_entry.delete('1.0', tk.END)

    laskuri = 0
    for tiedot in tiedot_lista:

        if laskuri % 2 == 0:
            laskuri += 1
        elif laskuri < len(tiedot_lista) - 1:
            tietojen_taytto_entryyn(tiedot, tiedot_entry, nimikkeet, tekstit, mika_tieto, "\n\n")
            laskuri += 1
        else:
            tietojen_taytto_entryyn(tiedot, tiedot_entry, nimikkeet, tekstit, mika_tieto, "")
# -------------------------------------------------------------------
def tietojen_taytto_entryyn(tiedot, tiedot_entry, nimikkeet, tekstit, mika_tieto, rivinvaihto):
    i = 0

    while i < len(tekstit) - 1:
        if tiedot[nimikkeet[i]] != mika_tieto:
            # Sijoitetaan tiedot terminaaliin
            tiedot_entry.insert(tk.END, f"{tekstit[i]} {tiedot[nimikkeet[i]]}\n")
        i += 1
    else:
        tiedot_entry.insert(tk.END, f"{tekstit[i]} {tiedot[nimikkeet[i]]}{rivinvaihto}")
# -------------------------------------------------------------------
"""Täyttää tiedot entryyn + tiketin ID"""
def tietojen_taytto_useat_id(tiedot_entry, tiedot_lista, nimikkeet, tekstit, mika_tieto, tiketin_id_teksti):

    tiedot_entry.delete('1.0', tk.END)

    laskuri = 0
    for tiedot in tiedot_lista:
        
        if laskuri % 2 == 0:
            tiedot_entry.insert(tk.END, f"{tiketin_id_teksti} {tiedot}\n")
            laskuri += 1

        elif laskuri < len(tiedot_lista) - 1:
            tietojen_taytto_entryyn(tiedot, tiedot_entry, nimikkeet, tekstit, mika_tieto, "\n\n")
            laskuri += 1
        else:
            tietojen_taytto_entryyn(tiedot, tiedot_entry, nimikkeet, tekstit, mika_tieto, "")
# -------------------------------------------------------------------
"""Valmiusasteiden asetus valikkoon"""
def tiketit_haku_valmiusaste(valmiusaste_combobox):

    tiedot = ["Vastaanotettu", "Työnalla", "Valmis"]

    valmiusaste_combobox.configure(values = tiedot)
    valmiusaste_combobox.set(tiedot[0])
# -------------------------------------------------------------------
"""Tikettien tietojen haku valmiusasteen perusteella"""
def valmiusaste_valikko_event(event, valmiusaste_combobox, valmiusaste_tikettien_tiedot_entry):

    tiedosto = "tikettitiedot.txt"

    valittu_valmiusaste = valmiusaste_combobox.get()

    tiketin_id_teksti = "Tiketin ID:"
    tiketin_tekstit = ["Asiakkaan nimi:", "Laitteen sarjanumero:", "Valmiusaste:", "Teknikon nimi:", "Laitteen vika:"]
    tiketin_nimikkeet = ["asiakas_id", "laite_id", "valmiusaste", "teknikko_id", "vika"]

    tiedot_lista = common.hae_tietoja(valittu_valmiusaste, "valmiusaste", tiedosto)

    tietojen_taytto_useat_id(valmiusaste_tikettien_tiedot_entry, tiedot_lista, tiketin_nimikkeet, tiketin_tekstit, valittu_valmiusaste, tiketin_id_teksti)
# -------------------------------------------------------------------


