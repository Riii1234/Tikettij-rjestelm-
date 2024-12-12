import tkinter as tk
from tkinter import ttk
import common_tkinter
from tiketit import uusi_tiketti, tietojen_tallennus
from asiakkaat import vanha_asiakas
from laitteet import vanha_laite_valikko, vanhat_laitteet_nappi
# -------------------------------------------------------------------
def luo_tiketti_toiminnot(tiketti_frame):
    """Luo tiketit-välilehdelle widgetit"""

    tiketti_id = luo_tiketin_id(tiketti_frame)

    vanhat_laitteet_valikko = laitteet_valikko(tiketti_frame)

    asiakas_muuttujat = asiakas_tiedot(tiketti_frame, vanhat_laitteet_valikko)
    laite_muuttujat = laite_tiedot(tiketti_frame, asiakas_muuttujat, vanhat_laitteet_valikko)

    vikakuvaus_entry = vikakuvaus(tiketti_frame)

    tallennus(tiketti_frame, tiketti_id, asiakas_muuttujat, laite_muuttujat, vikakuvaus_entry)
# -------------------------------------------------------------------
def luo_tiketin_id(tiketti_frame):
    """Luo uuden tiketin (ID)"""

    tiketti_id = uusi_tiketti()

    # tee_label(frame, teksti, tyyli, pystyrivi, vaakarivi, x_vasen, x_oikea, y_ylä, y_ala)
    common_tkinter.luo_label(tiketti_frame, f" Tiketin ID: {tiketti_id} ", "white2.TLabel", 0, 1, 100, 0, 50, 10)

    return tiketti_id
# -------------------------------------------------------------------
def laitteet_valikko(tiketti_frame):
    """Valikko asiakkaan vanhoista laitteista"""

    vanhat_laitteet_valikko = common_tkinter.luo_valikko(tiketti_frame, "Vanhat laitteet", 10, 3)

    return vanhat_laitteet_valikko
# -------------------------------------------------------------------
def asiakas_tiedot(tiketti_frame, vanhat_laitteet_valikko):
    """Tekee entryt asiakkaan tiedoille ja hakee niihin mahdolliset vanhat tiedot"""

    label_tekstit = ["Asiakkaan nimi:", "Asiakkaan osoite:", "Asiakkaan puh.numero:", "Asiakkaan email-osoite:"]

    asiakas_nimi_entry = ttk.Entry
    asiakas_osoite_entry = ttk.Entry
    asiakas_puh_numero_entry = ttk.Entry
    asiakas_email_entry = ttk.Entry
    asiakas_entryt = [asiakas_nimi_entry, asiakas_osoite_entry, asiakas_puh_numero_entry, asiakas_email_entry]

    asiakas_nimi = tk.StringVar()
    asiakas_osoite = tk.StringVar()
    asiakas_puh_numero = tk.StringVar()
    asiakas_email = tk.StringVar()
    asiakas_muuttujat = [asiakas_nimi, asiakas_osoite, asiakas_puh_numero, asiakas_email]
    
    common_tkinter.luo_labelit_ja_entryt(tiketti_frame, label_tekstit, asiakas_entryt, asiakas_muuttujat, 0, 5, 100, 10)

    # Button hakee vanhan asiakkaan tiedot nimen perusteella
    common_tkinter.luo_button(tiketti_frame, "Hae asiakkaan tiedot", \
        lambda:vanha_asiakas(asiakas_muuttujat, asiakas_entryt, vanhat_laitteet_valikko), 0, 7, 100, 10, 10)

    return asiakas_muuttujat
# -------------------------------------------------------------------
def laite_tiedot(tiketti_frame, asiakas_muuttujat, vanhat_laitteet_valikko):
    """Tekee entryt laitteen tiedoille ja hakee niihin mahdolliset vanhat tiedot"""

    label_tekstit = ["Laitteen malli:", "Laitteen tyyppi:", "Laitteen sarjanumero:", "Laitteen tuotetunnus:", "Laitteen lisätiedot: (valinnainen)"]

    laite_malli_entry = ttk.Entry
    laite_tyyppi_entry = ttk.Entry
    laite_sarjanumero_entry = ttk.Entry
    laite_tuotetunnus_entry = ttk.Entry
    laite_lisatiedot_entry = ttk.Entry
    laite_entryt = [laite_malli_entry, laite_tyyppi_entry, laite_sarjanumero_entry, laite_tuotetunnus_entry, laite_lisatiedot_entry]

    laite_malli = tk.StringVar()
    laite_tyyppi  = tk.StringVar()
    laite_sarjanumero  = tk.StringVar()
    laite_tuotetunnus  = tk.StringVar()
    laite_lisatiedot  = tk.StringVar()
    laite_muuttujat = [laite_malli, laite_tyyppi , laite_sarjanumero, laite_tuotetunnus, laite_lisatiedot]
    
    common_tkinter.luo_labelit_ja_entryt(tiketti_frame, label_tekstit, laite_entryt, laite_muuttujat, 10, 5, 10, 100)

    # Haetaan vanhan laitteen tiedot mallin perusteella
    common_tkinter.luo_button(tiketti_frame, "Hae laitteen tiedot", \
        lambda:vanhat_laitteet_nappi(laite_malli, laite_entryt, asiakas_muuttujat), 10, 7, 10, 10, 10)
    
    # Vanhat laitteet valikko bindattuna funktioon (Funktio tapahtuu joka kerta, kun valikkoa vaihdetaan)
    vanhat_laitteet_valikko.bind("<<ComboboxSelected>>", lambda event: vanha_laite_valikko(event, laite_entryt, asiakas_muuttujat, vanhat_laitteet_valikko))

    return laite_muuttujat
# -------------------------------------------------------------------
def vikakuvaus(tiketti_frame):
    """Luo monirivisen teksti-kentän vikakuvaukselle"""
    
    common_tkinter.luo_label(tiketti_frame, "Laitteen vikakuvaus: ", "white.TLabel", 0, 23, 100, 10, 6, 0)

    vikakuvaus_entry = common_tkinter.luo_teksti_kentta(tiketti_frame, 0, 24, 6, 100, 10)

    return vikakuvaus_entry
# -------------------------------------------------------------------
def tallennus(tiketti_frame, tiketti_id, asiakas_muuttujat, laite_muuttujat, vikakuvaus_entry):
    """Luo buttonin tiketin tallentamiseksi"""

    common_tkinter.luo_button(tiketti_frame, "Tallenna tiedot", \
        lambda:tietojen_tallennus(tiketti_frame, tiketti_id, asiakas_muuttujat, laite_muuttujat, vikakuvaus_entry), 10, 25, 10, 10, 40)
# -------------------------------------------------------------------