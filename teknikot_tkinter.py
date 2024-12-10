import tkinter as tk
from tkinter import ttk
import common_tkinter
import teknikot
# -------------------------------------------------------------------
# Teknikko-välilehti
def teknikot_valilehti(teknikot_frame):

    teknikon_tiedot(teknikot_frame)

    valmiusasteen_vaihto(teknikot_frame)

# -------------------------------------------------------------------
# Luo labelit ja entryt uuden teknikon tiedoille
def teknikon_tiedot(teknikot_frame):

    ttk.Label(teknikot_frame, text = "Uusi teknikko", style = "white2.TLabel") \
        .grid(column = 1, row = 1, columnspan = 2, \
        padx = [5, 0], pady = [100, 0])

    tiedot_lista = ["Teknikon nimi:", "Teknikon puh.numero:", "Teknikon email-osoite:"]
    teknikon_nimi = tk.StringVar()
    teknikon_puh_numero = tk.StringVar()
    teknikon_email = tk.StringVar()

    teknikon_nimi_entry = ttk.Entry
    teknikon_puh_numero_entry = ttk.Entry
    teknikon_email_entry = ttk.Entry
    teknikon_tiedot = [teknikon_nimi, teknikon_puh_numero, teknikon_email]
    teknikon_entryt = [teknikon_nimi_entry, teknikon_puh_numero_entry, teknikon_email_entry]

    common_tkinter.luo_labelit_ja_entryt(teknikot_frame, tiedot_lista, teknikon_entryt, teknikon_tiedot, 1, 5)

    # Button tallentaa uuden teknikon tiedot
    ttk.Button(teknikot_frame, text = "Tallenna teknikko", style = "bw2.TButton", \
        command=lambda:teknikot.uusi_teknikko(teknikon_tiedot)) \
        .grid(column = 1, row = 20, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [10, 10])
# -------------------------------------------------------------------
# Valikot tiketin valitsemiseen ja tiketin valmiusasteen vaihtamiseksi
def valmiusasteen_vaihto(teknikot_frame):

    ttk.Label(teknikot_frame, text = "Vaihda tiketin valmiusastetta", style = "white2.TLabel") \
        .grid(column = 10, row = 1, columnspan = 2, \
        padx = [5, 0], pady = [100, 0])

    asiakkaat_combobox = comboboxin_luonti(teknikot_frame, "Valitse asiakas", 6)
    asiakkaat_combobox.bind("<<ComboboxSelected>>", lambda event: teknikot.laitteet_valikko_mallit(event, teknikot_frame, asiakkaat_combobox, laitteet_combobox))
    teknikot.asiakkaat_valikko_nimet(asiakkaat_combobox)

    laitteet_combobox = comboboxin_luonti(teknikot_frame, "Valitse asiakkaan laite", 8)
    laitteet_combobox.bind("<<ComboboxSelected>>", lambda event: teknikot.laitteet_valikko_event(event, \
        teknikot_frame, asiakkaat_combobox, laitteet_combobox, valmiusasteet_combobox, teknikot_combobox))

    valmiusasteet_combobox = comboboxin_luonti(teknikot_frame, "Valitse tiketin valmiusaste", 10)

    teknikot_combobox = comboboxin_luonti(teknikot_frame, "Tikettiä työstävä teknikko", 20)
    teknikot.teknikot_valikko_nimet(teknikot_combobox)

    # Button tallentaa tiketin valmiusasteen
    ttk.Button(teknikot_frame, text = "Tallenna tiketti", style = "bw2.TButton", \
        command=lambda:teknikot.tallenna_tiketti(asiakkaat_combobox, laitteet_combobox, valmiusasteet_combobox, teknikot_combobox)) \
        .grid(column = 10, row = 22, columnspan = 2, sticky = tk.E, padx = [0, 10], pady = [0, 100])
# -------------------------------------------------------------------
def comboboxin_luonti(teknikot_frame, teksti, rivi):

    ttk.Label(teknikot_frame, text = teksti, style = "white.TLabel") \
        .grid(column = 10, row = rivi, columnspan = 2, sticky = tk.E, padx = [114, 10], pady = [5, 10])

    combobox_teksti = tk.StringVar()
    
    combobox_nimi = ttk.Combobox(teknikot_frame, textvariable = combobox_teksti, state = "readonly", width = 20, style = "bw.TCombobox")
    combobox_nimi.grid(column = 10, row = rivi + 1, columnspan = 4, sticky = tk.E, padx = [0, 10], pady = [0, 20])

    return combobox_nimi
# -------------------------------------------------------------------

