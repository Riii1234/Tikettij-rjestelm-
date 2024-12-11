import tkinter as tk
from tkinter import ttk
import common_tkinter
from tiketit import uusi_tiketti, tietojen_tallennus
from asiakkaat import vanha_asiakas
from laitteet import vanha_laite_valikko, vanhat_laitteet_nappi
# -------------------------------------------------------------------
def luo_tiketti_toiminnot(tiketti_frame):
    """Tiketin luonti, ottaa vastaan tiketti_framen"""

    tiketti_id = luo_tiketin_id(tiketti_frame)

    vanhat_laitteet_combobox = laitteet_valikko(tiketti_frame)

    asiakas_muuttujat = asiakas_tiedot(tiketti_frame, vanhat_laitteet_combobox)
    laite_muuttujat = laite_tiedot(tiketti_frame, asiakas_muuttujat, vanhat_laitteet_combobox)

    vikakuvaus_entry = vikakuvaus(tiketti_frame)

    tallennus(tiketti_frame, tiketti_id, asiakas_muuttujat, laite_muuttujat, vikakuvaus_entry)
# -------------------------------------------------------------------
def luo_tiketin_id(tiketti_frame):
    """Luo uuden tiketin (ID)"""

    tiketti_id = uusi_tiketti()
    ttk.Label(tiketti_frame, text = f" Tiketin ID: {tiketti_id} ", style = "white2.TLabel") \
        .grid(column = 0, row = 1, columnspan = 2, \
        padx = [5, 0], pady = [100, 0])

    return tiketti_id
# -------------------------------------------------------------------
def laitteet_valikko(tiketti_frame):
    """Valikko asiakkaan vanhoista laitteista"""
    
    ttk.Label(tiketti_frame, text = "Vanhat laitteet", style = "white.TLabel") \
        .grid(column = 10, row = 3, columnspan = 2, sticky = tk.E, padx = [112, 0], pady = [20, 0])

    vanhat_laitteet_teksti = tk.StringVar()
    
    vanhat_laitteet_combobox = ttk.Combobox(tiketti_frame, textvariable = vanhat_laitteet_teksti, state = "readonly", width = 20, style = "bw.TCombobox")
    vanhat_laitteet_combobox.grid(column = 10, row = 4, columnspan = 4, sticky = tk.E, padx = [0, 20], pady = [0, 30])

    return vanhat_laitteet_combobox
# -------------------------------------------------------------------
def asiakas_tiedot(tiketti_frame, vanhat_laitteet_combobox):
    """Tekee entryt asiakkaan tiedoille ja hakee niihin mahdolliset vanhat tiedot"""

    label_tekstit = ["Asiakkaan nimi:", "Asiakkaan osoite:", "Asiakkaan puh.numero:", "Asiakkaan email-osoite:"]
    asiakkaan_nimi = tk.StringVar()
    asiakkaan_osoite = tk.StringVar()
    asiakkaan_puh_numero = tk.StringVar()
    asiakkaan_email = tk.StringVar()

    asiakkaan_nimi_entry = ttk.Entry
    asiakkaan_osoite_entry = ttk.Entry
    asiakkaan_puh_numero_entry = ttk.Entry
    asiakkaan_email_entry = ttk.Entry
    asiakkaan_muuttujat = [asiakkaan_nimi, asiakkaan_osoite, asiakkaan_puh_numero, asiakkaan_email]
    asiakkaan_entryt = [asiakkaan_nimi_entry, asiakkaan_osoite_entry, asiakkaan_puh_numero_entry, asiakkaan_email_entry]

    common_tkinter.luo_labelit_ja_entryt(tiketti_frame, label_tekstit, asiakkaan_entryt, asiakkaan_muuttujat, 1, 5)

    # Button hakee vanhan asiakkaan tiedot nimen perusteella
    ttk.Button(tiketti_frame, text = "Hae asiakkaan tiedot", style = "bw.TButton", \
        command=lambda:vanha_asiakas(asiakkaan_muuttujat, asiakkaan_entryt, vanhat_laitteet_combobox)) \
        .grid(column = 1, row = 7, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [10, 60])

    return asiakkaan_muuttujat
# -------------------------------------------------------------------
def laite_tiedot(tiketti_frame, asiakas_muuttujat, vanhat_laitteet_combobox):
    """Tekee entryt laitteen tiedoille ja hakee niihin mahdolliset vanhat tiedot"""

    label_tekstit = ["Laitteen malli:", "Laitteen tyyppi:", "Laitteen sarjanumero:", "Laitteen tuotetunnus:", "Laitteen lisätiedot: (valinnainen)"]

    laite_malli = tk.StringVar()
    laite_tyyppi  = tk.StringVar()
    laite_sarjanumero  = tk.StringVar()
    laite_tuotetunnus  = tk.StringVar()
    laite_lisatiedot  = tk.StringVar()

    laite_malli_entry = ttk.Entry
    laite_tyyppi_entry = ttk.Entry
    laite_sarjanumero_entry = ttk.Entry
    laite_tuotetunnus_entry = ttk.Entry
    laite_lisatiedot_entry = ttk.Entry

    laite_muuttujat = [laite_malli, laite_tyyppi , laite_sarjanumero, laite_tuotetunnus, laite_lisatiedot]
    laite_entryt = [laite_malli_entry, laite_tyyppi_entry, laite_sarjanumero_entry, laite_tuotetunnus_entry, laite_lisatiedot_entry]

    common_tkinter.luo_labelit_ja_entryt(tiketti_frame, label_tekstit, laite_entryt, laite_muuttujat, 10, 5)

    # Haetaan vanhan laitteen tiedot mallin perusteella
    ttk.Button(tiketti_frame, text = "Hae laitteen tiedot", style = "bw.TButton", \
        command=lambda:vanhat_laitteet_nappi(laite_malli, laite_entryt, asiakas_muuttujat)) \
        .grid(column = 10, row = 7, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [10, 60])
    
    # Vanhat laitteet valikko bindattuna funktioon (Funktio tapahtuu joka kerta, kun valikkoa vaihdetaan)
    vanhat_laitteet_combobox.bind("<<ComboboxSelected>>", lambda event: vanha_laite_valikko(event, laite_entryt, asiakas_muuttujat, vanhat_laitteet_combobox))

    return laite_muuttujat
# -------------------------------------------------------------------
def vikakuvaus(tiketti_frame):
    """Luo monirivisen teksti-kentän vikakuvaukselle"""

    ttk.Label(tiketti_frame, text = "Laitteen vikakuvaus: ", style = "white.TLabel") \
        .grid(column = 1, row = 20, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [20, 2])
    
    vikakuvaus_entry = tk.Text(tiketti_frame, width = 40, height = 4, bg = "#101010", fg = "white", \
        insertbackground = "white", font = ("Helvetica", 10))
    vikakuvaus_entry.grid(column = 1, row = 21, columnspan = 4, sticky = tk.W, padx = [5, 0])

    return vikakuvaus_entry
# -------------------------------------------------------------------
def tallennus(tiketti_frame, tiketti_id, asiakas_muuttujat, laite_muuttujat, vikakuvaus_entry):
    """Luo buttonin tiketin tallentamiseksi"""

    ttk.Button(tiketti_frame, text = "Tallenna tiedot", style = "bw2.TButton", \
        command=lambda:tietojen_tallennus(tiketti_frame, tiketti_id, asiakas_muuttujat, laite_muuttujat, vikakuvaus_entry)) \
        .grid(column = 10, row = 21, columnspan = 2, sticky = tk.E, padx = [5, 0], pady = [5, 5])
# -------------------------------------------------------------------