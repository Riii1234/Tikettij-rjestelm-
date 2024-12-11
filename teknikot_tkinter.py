import tkinter as tk
from tkinter import ttk
import common_tkinter
import teknikot
# -------------------------------------------------------------------
def luo_teknikko_toiminnot(teknikko_frame):
    """Teknikko-välilehti"""

    teknikon_tiedot(teknikko_frame)

    valmiusasteen_vaihto(teknikko_frame)

# -------------------------------------------------------------------
def teknikon_tiedot(teknikko_frame):
    """Luo labelit ja entryt uuden teknikon tiedoille"""

    ttk.Label(teknikko_frame, text = "Uusi teknikko", style = "white2.TLabel") \
        .grid(column = 1, row = 1, columnspan = 2, \
        padx = [5, 0], pady = [100, 0])

    label_tekstit = ["Teknikon nimi:", "Teknikon puh.numero:", "Teknikon email-osoite:"]
    teknikko_nimi = tk.StringVar()
    teknikko_puh_numero = tk.StringVar()
    teknikko_email = tk.StringVar()

    teknikko_nimi_entry = ttk.Entry
    teknikko_puh_numero_entry = ttk.Entry
    teknikko_email_entry = ttk.Entry
    teknikko_muuttujat = [teknikko_nimi, teknikko_puh_numero, teknikko_email]
    teknikko_entryt = [teknikko_nimi_entry, teknikko_puh_numero_entry, teknikko_email_entry]

    common_tkinter.luo_labelit_ja_entryt(teknikko_frame, label_tekstit, teknikko_entryt, teknikko_muuttujat, 1, 5)

    # Button tallentaa uuden teknikon tiedot
    ttk.Button(teknikko_frame, text = "Tallenna teknikko", style = "bw2.TButton", \
        command=lambda:teknikot.uusi_teknikko(teknikko_muuttujat)) \
        .grid(column = 1, row = 20, columnspan = 2, sticky = tk.W, padx = [5, 0], pady = [10, 10])
# -------------------------------------------------------------------
def valmiusasteen_vaihto(teknikko_frame):
    """Valikot tiketin valitsemiseen ja tiketin valmiusasteen vaihtamiseksi"""

    ttk.Label(teknikko_frame, text = "Vaihda tiketin valmiusastetta", style = "white2.TLabel") \
        .grid(column = 10, row = 1, columnspan = 2, \
        padx = [5, 0], pady = [100, 0])

    asiakkaat_combobox = comboboxin_luonti(teknikko_frame, "Valitse asiakas", 6)
    asiakkaat_combobox.bind("<<ComboboxSelected>>", lambda event: teknikot.laitteet_valikko_mallit(event, teknikko_frame, asiakkaat_combobox, laitteet_combobox))
    teknikot.asiakkaat_valikko_nimet(asiakkaat_combobox)

    laitteet_combobox = comboboxin_luonti(teknikko_frame, "Valitse asiakkaan laite", 8)
    laitteet_combobox.bind("<<ComboboxSelected>>", lambda event: teknikot.laitteet_valikko_event(event, \
        teknikko_frame, asiakkaat_combobox, laitteet_combobox, valmiusasteet_combobox, teknikot_combobox))

    valmiusasteet_combobox = comboboxin_luonti(teknikko_frame, "Valitse tiketin valmiusaste", 10)

    teknikot_combobox = comboboxin_luonti(teknikko_frame, "Tikettiä työstävä teknikko", 20)
    teknikot.teknikot_valikko_nimet(teknikot_combobox)

    # Button tallentaa tiketin valmiusasteen
    ttk.Button(teknikko_frame, text = "Tallenna tiketti", style = "bw2.TButton", \
        command=lambda:teknikot.tallenna_tiketti(asiakkaat_combobox, laitteet_combobox, valmiusasteet_combobox, teknikot_combobox)) \
        .grid(column = 10, row = 22, columnspan = 2, sticky = tk.E, padx = [0, 10], pady = [0, 100])
# -------------------------------------------------------------------
def comboboxin_luonti(teknikko_frame, teksti, rivi):

    ttk.Label(teknikko_frame, text = teksti, style = "white.TLabel") \
        .grid(column = 10, row = rivi, columnspan = 2, sticky = tk.E, padx = [114, 10], pady = [5, 10])

    combobox_teksti = tk.StringVar()
    
    combobox_nimi = ttk.Combobox(teknikko_frame, textvariable = combobox_teksti, state = "readonly", width = 20, style = "bw.TCombobox")
    combobox_nimi.grid(column = 10, row = rivi + 1, columnspan = 4, sticky = tk.E, padx = [0, 10], pady = [0, 20])

    return combobox_nimi
# -------------------------------------------------------------------

