import tkinter as tk
from tkinter import ttk
import common_tkinter
import haku
# -------------------------------------------------------------------
def luo_haku_toiminnot(haku_frame):
    """Luo tiedonhaku-välilehdelle widgetit"""

    # tee_label(frame, teksti, tyyli, pystyrivi, vaakarivi, x_vasen, x_oikea, y_ylä, y_ala)
    common_tkinter.luo_label(haku_frame, "Asiakastiedot", "white2.TLabel", 0, 1, 10, 0, 50, 10)
    luo_asiakastieto_haku(haku_frame)

    common_tkinter.luo_label(haku_frame, "Laitetiedot", "white2.TLabel", 10, 1, 10, 0, 50, 10)
    luo_laitetieto_haku(haku_frame)

    common_tkinter.luo_label(haku_frame, "Tikettitiedot", "white2.TLabel", 20, 1, 10, 0, 50, 10)
    luo_valmiusaste_haku(haku_frame)
# -------------------------------------------------------------------
def luo_asiakastieto_haku(haku_frame):
    """Luo widgetit asiakkaan tietojen hakuun asiakkaan nimellä tai emaililla"""

    label_tekstit = ["Asiakkaan nimi:", "tai Asiakkaan email-osoite:"]

    asiakas_nimi_entry = ttk.Entry
    asiakas_email_entry = ttk.Entry
    asiakas_entryt = [asiakas_nimi_entry, asiakas_email_entry]

    asiakas_nimi = tk.StringVar()
    asiakas_email = tk.StringVar()
    asiakas_muuttujat = [asiakas_nimi, asiakas_email]

    # luo_labelit_ja_entryt(frame, label_tekstit, entryt, muuttujat, pystyrivi, vaakarivi)
    common_tkinter.luo_labelit_ja_entryt(haku_frame, label_tekstit, asiakas_entryt, asiakas_muuttujat, 0, 3, 10, 10)

    asiakas_tekstikentta = common_tkinter.luo_teksti_kentta(haku_frame, 0, 20, 16, 10, 10)

    common_tkinter.luo_button(haku_frame, "Hae asiakkaan tiedot", \
        lambda:haku.hae_asiakas_tiedot(asiakas_entryt, asiakas_tekstikentta), 0, 9, 10, 10, 0)
# -------------------------------------------------------------------
def luo_laitetieto_haku(haku_frame):
    """Luo widgetit laitteen tietojen hakuun laitteen sarjanumerolla"""

    common_tkinter.luo_label(haku_frame, "Laitteen sarjanumero:", "white.TLabel", 10, 3, 10, 0, 6, 0)

    laite_sarjanumero = tk.StringVar()
    # luo_entry(frame, teksti_muuttuja, pystyrivi, vaakarivi, x_vasen, x_oikea, y_ylä, y_ala)
    laite_sarjanumero_entry = common_tkinter.luo_entry(haku_frame, laite_sarjanumero, 10, 4, 10, 10, 4, 10)

    laite_tyyppi_valikko = common_tkinter.luo_valikko(haku_frame, "Laitetyypit", 10, 11, 10)
    laite_malli_valikko = common_tkinter.luo_valikko(haku_frame, "Laitemallit", 10, 13, 10)

    haku.aseta_laite_valikko_tiedot(laite_tyyppi_valikko, "tyyppi")
    haku.aseta_laite_valikko_tiedot(laite_malli_valikko, "malli")

    laite_tekstikentta = common_tkinter.luo_teksti_kentta(haku_frame, 10, 20, 16, 10, 10)

    common_tkinter.luo_button(haku_frame, "Hae laitteen tiedot", \
        lambda:haku.hae_laite_tiedot(laite_sarjanumero_entry, laite_tekstikentta), 10, 7, 10, 10, 0)

    laite_tyyppi_valikko.bind("<<ComboboxSelected>>", lambda event: haku.luo_laite_valikko_event(event, laite_tyyppi_valikko, "tyyppi", laite_tekstikentta))
    laite_malli_valikko.bind("<<ComboboxSelected>>", lambda event: haku.luo_laite_valikko_event(event, laite_malli_valikko, "malli", laite_tekstikentta))
# -------------------------------------------------------------------
def luo_valmiusaste_haku(haku_frame):
    """Tikettien tietojen haku valmiusasteella"""

    valmiusaste_valikko = common_tkinter.luo_valikko(haku_frame, "Tiketin valmiusaste", 20, 3, 10)

    haku.aseta_valmiusaste_valikko_tiedot(valmiusaste_valikko)

    tiketti_tekstikentta = common_tkinter.luo_teksti_kentta(haku_frame, 20, 20, 16, 10, 10)

    valmiusaste_valikko.bind("<<ComboboxSelected>>", lambda event: haku.luo_valmiusaste_valikko_event(event, valmiusaste_valikko, tiketti_tekstikentta))
# -------------------------------------------------------------------