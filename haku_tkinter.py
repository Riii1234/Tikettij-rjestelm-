import tkinter as tk
from tkinter import ttk
import common_tkinter
import haku
# -------------------------------------------------------------------
"""Tiedonhaku"""
def haku_valilehti(haku_frame):

    ttk.Label(haku_frame, text = "Asiakastiedot", style = "white2.TLabel") \
        .grid(column = 0, row = 1, columnspan = 2, \
        padx = [10, 0], pady = [40, 0])
    
    asiakastietojen_haku(haku_frame)
    
    ttk.Label(haku_frame, text = "Laitetiedot", style = "white2.TLabel") \
        .grid(column = 10, row = 1, columnspan = 2, \
        padx = [5, 0], pady = [40, 0])
    
    laitetietojen_haku(haku_frame)
    
    ttk.Label(haku_frame, text = "Tikettitiedot", style = "white2.TLabel") \
        .grid(column = 20, row = 1, columnspan = 2, \
        padx = [5, 10], pady = [40, 0])
    
    valmiusaste_haku(haku_frame)
# -------------------------------------------------------------------
"""Asiakkaan tietojen haku asiakkaan ID:llä, nimellä tai emaililla"""
def asiakastietojen_haku(haku_frame):

    tiedot_lista = ["Asiakkaan nimi:", "tai Asiakkaan email-osoite:"]

    asiakkaan_nimi = tk.StringVar()
    asiakkaan_email = tk.StringVar()

    asiakkaan_nimi_entry = ttk.Entry
    asiakkaan_email_entry = ttk.Entry
    asiakkaan_tiedot = [asiakkaan_nimi, asiakkaan_email]
    asiakkaan_entryt = [asiakkaan_nimi_entry, asiakkaan_email_entry]

    common_tkinter.luo_labelit_ja_entryt(haku_frame, tiedot_lista, asiakkaan_entryt, asiakkaan_tiedot, 1, 3)

    asiakastiedot_entry = tk.Text(haku_frame, width = 40, height = 16, bg = "#101010", fg = "white", \
    insertbackground = "white", font = ("Helvetica", 10))
    asiakastiedot_entry.grid(column = 1, row = 11, columnspan = 4, sticky = tk.W, padx = [5, 0])

    ttk.Button(haku_frame, text = "Hae asiakkaan tiedot", style = "bw.TButton", \
        command=lambda:haku.hae_asiakkaan_tiedot(asiakkaan_entryt, asiakastiedot_entry)) \
        .grid(column = 1, row = 10, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [10, 10])
# -------------------------------------------------------------------
"""Laitteen tietojen haku laitteen ID:n tai sarjanumeron perusteella"""
def laitetietojen_haku(haku_frame):

    tiedot_lista = ["Laitteen sarjanumero:"]
    laitteen_sarjanumero = tk.StringVar()

    laitteen_sarjanumero_entry = ttk.Entry
    laitteen_tiedot = [laitteen_sarjanumero]
    laitteen_entry = [laitteen_sarjanumero_entry]

    common_tkinter.luo_labelit_ja_entryt(haku_frame, tiedot_lista, laitteen_entry, laitteen_tiedot, 10, 3)

    ttk.Button(haku_frame, text = "Hae laitteen tiedot", style = "bw.TButton", \
        command=lambda:haku.hae_laitteen_tiedot(laitteen_entry, laitteet_tiedot_entry)) \
        .grid(column = 10, row = 5, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [10, 10])

    laite_tyyppi_combobox = common_tkinter.luo_valikko(haku_frame, "Laitetyypit", 10, 6)
    laite_malli_combobox = common_tkinter.luo_valikko(haku_frame, "Laitemallit", 10, 8)

    haku.laitteet_valikko(laite_tyyppi_combobox, "tyyppi")
    haku.laitteet_valikko(laite_malli_combobox, "malli")

    laite_tyyppi_combobox.bind("<<ComboboxSelected>>", lambda event: haku.laitteet_valikko_event(event, laite_tyyppi_combobox, "tyyppi", laitteet_tiedot_entry))
    laite_malli_combobox.bind("<<ComboboxSelected>>", lambda event: haku.laitteet_valikko_event(event, laite_malli_combobox, "malli", laitteet_tiedot_entry))

    laitteet_tiedot_entry = tk.Text(haku_frame, width = 40, height = 16, bg = "#101010", fg = "white", \
    insertbackground = "white", font = ("Helvetica", 10))
    laitteet_tiedot_entry.grid(column = 10, row = 11, columnspan = 4, sticky = tk.W, padx = [5, 0])
# -------------------------------------------------------------------
"""Tikettien tietojen haku valmiusasteella"""
def valmiusaste_haku(haku_frame):

    valmiusaste_combobox = common_tkinter.luo_valikko(haku_frame, "Tiketin valmiusaste", 20, 3)

    haku.tiketit_haku_valmiusaste(valmiusaste_combobox)

    valmiusaste_combobox.bind("<<ComboboxSelected>>", lambda event: haku.valmiusaste_valikko_event(event, valmiusaste_combobox, valmiusaste_tikettien_tiedot_entry))

    valmiusaste_tikettien_tiedot_entry = tk.Text(haku_frame, width = 40, height = 16, bg = "#101010", fg = "white", \
    insertbackground = "white", font = ("Helvetica", 10))
    valmiusaste_tikettien_tiedot_entry.grid(column = 20, row = 11, columnspan = 4, sticky = tk.W, padx = [5, 0])
# -------------------------------------------------------------------

