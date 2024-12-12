import tkinter as tk
from tkinter import ttk
import common_tkinter
import teknikot
# -------------------------------------------------------------------
def luo_teknikko_toiminnot(teknikko_frame):
    """Luo teknikko-välilehdelle widgetit"""

    teknikon_tiedot(teknikko_frame)

    valmiusasteen_vaihto(teknikko_frame)

# -------------------------------------------------------------------
def teknikon_tiedot(teknikko_frame):
    """Luo labelit ja entryt uuden teknikon tiedoille"""

    # tee_label(frame, teksti, tyyli, pystyrivi, vaakarivi, x, y1, y2)
    common_tkinter.luo_label(teknikko_frame, "Uusi teknikko", "white2.TLabel", 0, 1, 10, 50, 10)

    label_tekstit = ["Teknikon nimi:", "Teknikon puh.numero:", "Teknikon email-osoite:"]
    
    teknikko_nimi_entry = ttk.Entry
    teknikko_puh_numero_entry = ttk.Entry
    teknikko_email_entry = ttk.Entry
    teknikko_entryt = [teknikko_nimi_entry, teknikko_puh_numero_entry, teknikko_email_entry]

    teknikko_nimi = tk.StringVar()
    teknikko_puh_numero = tk.StringVar()
    teknikko_email = tk.StringVar()
    teknikko_muuttujat = [teknikko_nimi, teknikko_puh_numero, teknikko_email]
    
    common_tkinter.luo_labelit_ja_entryt(teknikko_frame, label_tekstit, teknikko_entryt, teknikko_muuttujat, 1, 5)

    # Button tallentaa uuden teknikon tiedot
    common_tkinter.luo_button(teknikko_frame, "Tallenna teknikko", lambda:teknikot.uusi_teknikko(teknikko_muuttujat), 1, 20)
# -------------------------------------------------------------------
def valmiusasteen_vaihto(teknikko_frame):
    """Valikot tiketin valitsemiseen ja tiketin valmiusasteen vaihtamiseksi"""

    common_tkinter.luo_label(teknikko_frame, "Vaihda tiketin valmiusastetta", "white2.TLabel", 10, 1, 10, 50, 10)

    asiakkaat_valikko = common_tkinter.luo_valikko(teknikko_frame, "Valitse asiakas", 10, 6)
    asiakkaat_valikko.bind("<<ComboboxSelected>>", lambda event: teknikot.laitteet_valikko_mallit(event, teknikko_frame, asiakkaat_valikko, laitteet_valikko))
    teknikot.asiakkaat_valikko_nimet(asiakkaat_valikko)

    laitteet_valikko = common_tkinter.luo_valikko(teknikko_frame, "Valitse asiakkaan laite", 10, 8)
    laitteet_valikko.bind("<<ComboboxSelected>>", lambda event: teknikot.laitteet_valikko_event(event, \
        teknikko_frame, asiakkaat_valikko, laitteet_valikko, valmiusasteet_valikko, teknikot_valikko))

    valmiusasteet_valikko = common_tkinter.luo_valikko(teknikko_frame, "Valitse tiketin valmiusaste", 10, 10)
    
    teknikot_valikko = common_tkinter.luo_valikko(teknikko_frame, "Tikettiä työstävä teknikko", 10, 20)
    teknikot.teknikot_valikko_nimet(teknikot_valikko)

    # Button tallentaa tiketin valmiusasteen
    common_tkinter.luo_button(teknikko_frame, "Tallenna tiketti", lambda:teknikot.tallenna_tiketti(asiakkaat_valikko, laitteet_valikko, valmiusasteet_valikko, teknikot_valikko), 10, 22)
# -------------------------------------------------------------------