import tkinter as tk
from tkinter import ttk
import common_tkinter
from tiketit import uusi_tiketti, tietojen_tallennus
from asiakkaat import vanha_asiakas
from laitteet import vanha_laite_valikko, vanhat_laitteet_nappi
# -------------------------------------------------------------------
# Tiketin luonti, ottaa vastaan tiketti_framen
def tiketti_valilehti(tiketti_frame):

    tiketti_id = luo_tiketin_id(tiketti_frame)

    vanhat_laitteet_combobox = laitteet_valikko(tiketti_frame)

    asiakkaan_tiedot = asiakas_tiedot(tiketti_frame, vanhat_laitteet_combobox)
    laitteen_tiedot = laite_tiedot(tiketti_frame, asiakkaan_tiedot, vanhat_laitteet_combobox)

    vikakuvaus_entry = vikakuvaus(tiketti_frame)

    tallennus(tiketti_frame, tiketti_id, asiakkaan_tiedot, laitteen_tiedot, vikakuvaus_entry)
# -------------------------------------------------------------------
# Luo uuden tiketin (ID)
def luo_tiketin_id(tiketti_frame):

    tiketti_id = uusi_tiketti()
    ttk.Label(tiketti_frame, text = f" Tiketin ID: {tiketti_id} ", style = "white2.TLabel") \
        .grid(column = 0, row = 1, columnspan = 2, \
        padx = [5, 0], pady = [100, 0])

    return tiketti_id
# -------------------------------------------------------------------
# Valikko asiakkaan vanhoista laitteista
def laitteet_valikko(tiketti_frame):
    
    ttk.Label(tiketti_frame, text = "Vanhat laitteet", style = "white.TLabel") \
        .grid(column = 10, row = 3, columnspan = 2, sticky = tk.E, padx = [112, 0], pady = [20, 0])

    vanhat_laitteet_teksti = tk.StringVar()
    
    vanhat_laitteet_combobox = ttk.Combobox(tiketti_frame, textvariable = vanhat_laitteet_teksti, state = "readonly", width = 20, style = "bw.TCombobox")
    vanhat_laitteet_combobox.grid(column = 10, row = 4, columnspan = 4, sticky = tk.E, padx = [0, 20], pady = [0, 30])

    return vanhat_laitteet_combobox
# -------------------------------------------------------------------
# Tekee entryt asiakkaan tiedoille ja hakee niihin mahdolliset vanhat tiedot
def asiakas_tiedot(tiketti_frame, vanhat_laitteet_combobox):

    tiedot_lista = ["Asiakkaan nimi:", "Asiakkaan osoite:", "Asiakkaan puh.numero:", "Asiakkaan email-osoite:"]
    asiakkaan_nimi = tk.StringVar()
    asiakkaan_osoite = tk.StringVar()
    asiakkaan_puh_numero = tk.StringVar()
    asiakkaan_email = tk.StringVar()

    asiakkaan_nimi_entry = ttk.Entry
    asiakkaan_osoite_entry = ttk.Entry
    asiakkaan_puh_numero_entry = ttk.Entry
    asiakkaan_email_entry = ttk.Entry
    asiakkaan_tiedot = [asiakkaan_nimi, asiakkaan_osoite, asiakkaan_puh_numero, asiakkaan_email]
    asiakkaan_entryt = [asiakkaan_nimi_entry, asiakkaan_osoite_entry, asiakkaan_puh_numero_entry, asiakkaan_email_entry]

    common_tkinter.luo_labelit_ja_entryt(tiketti_frame, tiedot_lista, asiakkaan_entryt, asiakkaan_tiedot, 1, 5)

    # Button hakee vanhan asiakkaan tiedot nimen perusteella
    ttk.Button(tiketti_frame, text = "Hae asiakkaan tiedot", style = "bw.TButton", \
        command=lambda:vanha_asiakas(asiakkaan_tiedot, asiakkaan_entryt, vanhat_laitteet_combobox)) \
        .grid(column = 1, row = 7, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [10, 60])

    return asiakkaan_tiedot
# -------------------------------------------------------------------
# Tekee entryt laitteen tiedoille ja hakee niihin mahdolliset vanhat tiedot
def laite_tiedot(tiketti_frame, asiakkaan_tiedot, vanhat_laitteet_combobox):

    tiedot_lista = ["Laitteen malli:", "Laitteen tyyppi:", "Laitteen sarjanumero:", "Laitteen tuotetunnus:", "Laitteen lisätiedot: (valinnainen)"]

    laitteen_malli = tk.StringVar()
    laitteen_tyyppi  = tk.StringVar()
    laitteen_sarjanumero  = tk.StringVar()
    laitteen_tuotetunnus  = tk.StringVar()
    laitteen_lisatiedot  = tk.StringVar()

    laitteen_malli_entry = ttk.Entry
    laitteen_tyyppi_entry = ttk.Entry
    laitteen_sarjanumero_entry = ttk.Entry
    laitteen_tuotetunnus_entry = ttk.Entry
    laitteen_lisatiedot_entry = ttk.Entry

    laitteen_tiedot = [laitteen_malli, laitteen_tyyppi , laitteen_sarjanumero, laitteen_tuotetunnus, laitteen_lisatiedot]
    laitteen_entryt = [laitteen_malli_entry, laitteen_tyyppi_entry, laitteen_sarjanumero_entry, laitteen_tuotetunnus_entry, laitteen_lisatiedot_entry]

    common_tkinter.luo_labelit_ja_entryt(tiketti_frame, tiedot_lista, laitteen_entryt, laitteen_tiedot, 10, 5)

    # Haetaan vanhan laitteen tiedot mallin perusteella
    ttk.Button(tiketti_frame, text = "Hae laitteen tiedot", style = "bw.TButton", \
        command=lambda:vanhat_laitteet_nappi(laitteen_malli, laitteen_entryt, asiakkaan_tiedot)) \
        .grid(column = 10, row = 7, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [10, 60])
    
    # Vanhat laitteet valikko bindattuna funktioon (Funktio tapahtuu joka kerta, kun valikkoa vaihdetaan)
    vanhat_laitteet_combobox.bind("<<ComboboxSelected>>", lambda event: vanha_laite_valikko(event, laitteen_entryt, asiakkaan_tiedot, vanhat_laitteet_combobox))

    return laitteen_tiedot
# -------------------------------------------------------------------

# Luo monirivisen teksti-kentän vikakuvaukselle
def vikakuvaus(tiketti_frame):

    ttk.Label(tiketti_frame, text = "Laitteen vikakuvaus: ", style = "white.TLabel") \
        .grid(column = 1, row = 20, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [20, 2])
    vikakuvaus_entry = tk.Text(tiketti_frame, width = 40, height = 4, bg = "#101010", fg = "white", \
        insertbackground = "white", font = ("Helvetica", 10))
    vikakuvaus_entry.grid(column = 1, row = 21, columnspan = 4, sticky = tk.W, padx = [5, 0])

    return vikakuvaus_entry
# -------------------------------------------------------------------
# Luo buttonin tiketin tallentamiseksi
def tallennus(tiketti_frame, tiketti_id, asiakkaan_tiedot, laitteen_tiedot, vikakuvaus_entry):

    ttk.Button(tiketti_frame, text = "Tallenna tiedot", style = "bw2.TButton", \
        command=lambda:tietojen_tallennus(tiketti_frame, tiketti_id, asiakkaan_tiedot, laitteen_tiedot, vikakuvaus_entry)) \
        .grid(column = 10, row = 21, columnspan = 2, sticky = tk.E, padx = [5, 0], pady = [5, 5])
# -------------------------------------------------------------------

