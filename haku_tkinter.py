import tkinter as tk
from tkinter import ttk
import common_tkinter
import haku
# -------------------------------------------------------------------
def haku_valilehti(haku_frame):
    """Luo tiedonhaku-välilehdelle widgetit"""

    # tee_label(frame, teksti, tyyli, pystyrivi, vaakarivi, x, y)
    common_tkinter.luo_label(haku_frame, "Asiakastiedot", "white2.TLabel", 0, 1, 10, 50)
    asiakastietojen_haku(haku_frame)

    common_tkinter.luo_label(haku_frame, "Laitetiedot", "white2.TLabel", 10, 1, 10, 50)
    laitetietojen_haku(haku_frame)

    common_tkinter.luo_label(haku_frame, "Tikettitiedot", "white2.TLabel", 20, 1, 10, 50)
    valmiusaste_haku(haku_frame)
# -------------------------------------------------------------------
def asiakastietojen_haku(haku_frame):
    """Luo widgetit asiakkaan tietojen hakuun asiakkaan nimellä tai emaililla"""

    label_tekstit = ["Asiakkaan nimi:", "tai Asiakkaan email-osoite:"]

    asiakas_nimi = tk.StringVar()
    asiakas_email = tk.StringVar()

    asiakas_nimi_entry = ttk.Entry
    asiakas_email_entry = ttk.Entry
    asiakas_muuttujat = [asiakas_nimi, asiakas_email]
    asiakas_entryt = [asiakas_nimi_entry, asiakas_email_entry]

    # luo_labelit_ja_entryt(frame, label_tekstit, entryt, muuttujat, pystyrivi, vaakarivi)
    common_tkinter.luo_labelit_ja_entryt(haku_frame, label_tekstit, asiakas_entryt, asiakas_muuttujat, 1, 3)

    asiakastieto_kentta = common_tkinter.luo_teksti_kentta(haku_frame, 1, 20, 16)

    ttk.Button(haku_frame, text = "Hae asiakkaan tiedot", style = "bw.TButton", \
        command=lambda:haku.hae_asiakkaan_tiedot(asiakas_entryt, asiakastieto_kentta)) \
        .grid(column = 1, row = 16, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [10, 10])
# -------------------------------------------------------------------
def laitetietojen_haku(haku_frame):
    """Laitteen tietojen haku laitteen ID:n tai sarjanumeron perusteella"""

    tekstit_lista = ["Laitteen sarjanumero:"]
    laitteen_sarjanumero = tk.StringVar()

    laitteen_sarjanumero_entry = ttk.Entry
    laitteen_tiedot = [laitteen_sarjanumero]
    laitteen_entry = [laitteen_sarjanumero_entry]

    common_tkinter.luo_labelit_ja_entryt(haku_frame, tekstit_lista, laitteen_entry, laitteen_tiedot, 10, 3)

    laite_tyyppi_combobox = common_tkinter.luo_valikko(haku_frame, "Laitetyypit", 10, 7)
    laite_malli_combobox = common_tkinter.luo_valikko(haku_frame, "Laitemallit", 10, 9)

    haku.laitteet_valikko(laite_tyyppi_combobox, "tyyppi")
    haku.laitteet_valikko(laite_malli_combobox, "malli")

    laitetieto_kentta = common_tkinter.luo_teksti_kentta(haku_frame, 10, 20, 16)

    ttk.Button(haku_frame, text = "Hae laitteen tiedot", style = "bw.TButton", \
        command=lambda:haku.hae_laitteen_tiedot(laitteen_entry, laitetieto_kentta)) \
        .grid(column = 10, row = 5, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [10, 10])

    laite_tyyppi_combobox.bind("<<ComboboxSelected>>", lambda event: haku.laitteet_valikko_event(event, laite_tyyppi_combobox, "tyyppi", laitetieto_kentta))
    laite_malli_combobox.bind("<<ComboboxSelected>>", lambda event: haku.laitteet_valikko_event(event, laite_malli_combobox, "malli", laitetieto_kentta))
# -------------------------------------------------------------------
def valmiusaste_haku(haku_frame):
    """Tikettien tietojen haku valmiusasteella"""

    valmiusaste_combobox = common_tkinter.luo_valikko(haku_frame, "Tiketin valmiusaste", 20, 3)

    haku.tiketit_haku_valmiusaste(valmiusaste_combobox)

    tikettitieto_kentta = common_tkinter.luo_teksti_kentta(haku_frame, 20, 20, 16)

    valmiusaste_combobox.bind("<<ComboboxSelected>>", lambda event: haku.valmiusaste_valikko_event(event, valmiusaste_combobox, tikettitieto_kentta))
# -------------------------------------------------------------------