import tkinter as tk
from tkinter import ttk
import common_tkinter
import haku
# -------------------------------------------------------------------
# Tiedonhaku
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
    
    tikettitietojen_haku(haku_frame)
# -------------------------------------------------------------------
def asiakastietojen_haku(haku_frame):

    tiedot_lista = ["Asiakkaan ID:", "tai Asiakkaan nimi:", "tai Asiakkaan email-osoite:"]
    asiakkaan_id = tk.StringVar()
    asiakkaan_nimi = tk.StringVar()
    asiakkaan_email = tk.StringVar()

    asiakkaan_id_entry = ttk.Entry
    asiakkaan_nimi_entry = ttk.Entry
    asiakkaan_email_entry = ttk.Entry
    asiakkaan_tiedot = [asiakkaan_id, asiakkaan_nimi, asiakkaan_email]
    asiakkaan_entryt = [asiakkaan_id_entry, asiakkaan_nimi_entry, asiakkaan_email_entry]

    common_tkinter.luo_labelit_ja_entryt(haku_frame, tiedot_lista, asiakkaan_entryt, asiakkaan_tiedot, 1, 3)

    asiakastiedot_entry = tk.Text(haku_frame, width = 40, height = 5, bg = "#101010", fg = "white", \
    insertbackground = "white", font = ("Helvetica", 10))
    asiakastiedot_entry.grid(column = 1, row = 11, columnspan = 4, sticky = tk.W, padx = [5, 0])

    ttk.Button(haku_frame, text = "Hae asiakkaan tiedot", style = "bw.TButton", \
        command=lambda:haku.hae_asiakkaan_tiedot(asiakkaan_entryt, asiakastiedot_entry)) \
        .grid(column = 1, row = 10, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [10, 10])
# -------------------------------------------------------------------
def laitetietojen_haku(haku_frame):

    tiedot_lista = ["Laitteen ID:", "tai Laitteen sarjanumero:"]
    laitteen_id = tk.StringVar()
    laitteen_sarjanumero = tk.StringVar()

    laitteen_id_entry = ttk.Entry
    laitteen_sarjanumero_entry = ttk.Entry
    laitteen_tiedot = [laitteen_id, laitteen_sarjanumero]
    laitteen_entryt = [laitteen_id_entry, laitteen_sarjanumero_entry]

    common_tkinter.luo_labelit_ja_entryt(haku_frame, tiedot_lista, laitteen_entryt, laitteen_tiedot, 10, 3)

    laite_tiedot_entry = tk.Text(haku_frame, width = 40, height = 5, bg = "#101010", fg = "white", \
    insertbackground = "white", font = ("Helvetica", 10))
    laite_tiedot_entry.grid(column = 10, row = 11, columnspan = 4, sticky = tk.W, padx = [5, 0])

    ttk.Button(haku_frame, text = "Hae laitteen tiedot", style = "bw.TButton", \
        command=lambda:haku.hae_laitteen_tiedot(laitteen_entryt, laite_tiedot_entry)) \
        .grid(column = 10, row = 10, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [10, 10])

    laite_tyyppi_combobox = common_tkinter.luo_valikko(haku_frame, "Laitetyypit", 10, 12)
    laite_malli_combobox = common_tkinter.luo_valikko(haku_frame, "Laitemallit", 10, 14)

    haku.laitteet_valikko(laite_tyyppi_combobox, "tyyppi")
    haku.laitteet_valikko(laite_malli_combobox, "malli")

    laite_tyyppi_combobox.bind("<<ComboboxSelected>>", lambda event: haku.laitteet_valikko_event(event, laite_tyyppi_combobox, "tyyppi", laitteet_tiedot_entry))
    laite_malli_combobox.bind("<<ComboboxSelected>>", lambda event: haku.laitteet_valikko_event(event, laite_malli_combobox, "malli", laitteet_tiedot_entry))

    laitteet_tiedot_entry = tk.Text(haku_frame, width = 40, height = 6, bg = "#101010", fg = "white", \
    insertbackground = "white", font = ("Helvetica", 10))
    laitteet_tiedot_entry.grid(column = 10, row = 16, columnspan = 4, sticky = tk.W, padx = [5, 0])
# -------------------------------------------------------------------
def tikettitietojen_haku(haku_frame):

    tiketin_tietojen_haku_tiketti_id(haku_frame)

    tikettien_tietojen_haku(haku_frame)

    valmiusaste_haku(haku_frame)
# -------------------------------------------------------------------
def tiketin_tietojen_haku_tiketti_id(haku_frame):

    tiketin_id = tk.StringVar()

    ttk.Label(haku_frame, text = "Tiketin ID:", style = "white.TLabel") \
        .grid(column = 20, row = 3, columnspan = 2, sticky = (tk.W, tk.S), padx = [10, 0], pady = [6, 2])

    tiketin_id_entry = ttk.Entry(haku_frame, textvariable = tiketin_id, width = 40, style = "bw.TEntry")
    tiketin_id_entry.grid(column = 20, row = 4, columnspan = 4, sticky = tk.W, padx = [10, 20])
    
    tiketin_tiedot_entry = tk.Text(haku_frame, width = 40, height = 5, bg = "#101010", fg = "white", \
    insertbackground = "white", font = ("Helvetica", 10))
    tiketin_tiedot_entry.grid(column = 20, row = 6, columnspan = 4, sticky = tk.W, padx = [5, 0])

    ttk.Button(haku_frame, text = "Hae tiketin tiedot", style = "bw.TButton", \
        command=lambda:haku.hae_tiketin_tiedot(tiketin_id_entry, tiketin_tiedot_entry)) \
        .grid(column = 20, row = 5, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [10, 10])
 # -------------------------------------------------------------------
def tikettien_tietojen_haku(haku_frame):

    tiedot_lista = ["Asiakkaan ID:", "tai Laitteen ID:"]
    asiakkaan_id = tk.StringVar()
    laitteen_id = tk.StringVar()

    asiakkaan_id_entry = ttk.Entry
    laitteen_id_entry = ttk.Entry
    tiketin_tiedot = [asiakkaan_id, laitteen_id]
    tiketin_entryt = [asiakkaan_id_entry, laitteen_id_entry]

    common_tkinter.luo_labelit_ja_entryt(haku_frame, tiedot_lista, tiketin_entryt, tiketin_tiedot, 20, 10)

    tiketit_tiedot_entry = tk.Text(haku_frame, width = 40, height = 7, bg = "#101010", fg = "white", \
    insertbackground = "white", font = ("Helvetica", 10))
    tiketit_tiedot_entry.grid(column = 20, row = 16, columnspan = 4, sticky = tk.W, padx = [5, 0])

    ttk.Button(haku_frame, text = "Hae tikettien tiedot", style = "bw.TButton", \
        command=lambda:haku.hae_tikettien_tiedot(tiketin_entryt, tiketit_tiedot_entry)) \
        .grid(column = 20, row = 15, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [10, 10])
# -------------------------------------------------------------------
def valmiusaste_haku(haku_frame):

    valmiusaste_combobox = common_tkinter.luo_valikko(haku_frame, "Tiketin valmiusaste", 20, 20)

    haku.tiketit_haku_valmiusaste(valmiusaste_combobox)

    valmiusaste_combobox.bind("<<ComboboxSelected>>", lambda event: haku.valmiusaste_valikko_event(event, valmiusaste_combobox, valmiusaste_tikettien_tiedot_entry))

    valmiusaste_tikettien_tiedot_entry = tk.Text(haku_frame, width = 40, height = 7, bg = "#101010", fg = "white", \
    insertbackground = "white", font = ("Helvetica", 10))
    valmiusaste_tikettien_tiedot_entry.grid(column = 20, row = 22, columnspan = 4, sticky = tk.W, padx = [5, 0])
# -------------------------------------------------------------------

