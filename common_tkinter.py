import tkinter as tk
from tkinter import ttk
# -------------------------------------------------------------------
def luo_frame(root):
    """Luo framen ja reunukset"""
    # Luo frame widgetin padding = (left, top, right, bottom)
    frame = ttk.Frame(root, padding = f"10 10 10 10", style = "black.TFrame")
    frame.grid(column = 0, row = 0, sticky = (tk.N, tk.W, tk.E, tk.S))
    # Makes the frame expand to fill any extra space if the window is resized
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    # Tekee reunukset
    frame['borderwidth'] = 2
    frame['relief'] = 'sunken'

    return frame
# -------------------------------------------------------------------
def luo_label(frame, teksti, tyyli, pystyrivi, vaakarivi, x_vasen, x_oikea, y_yla, y_ala):
    """Luo teksti-labelin ja asettaa sen frameen"""

    ttk.Label(frame, text = teksti, style = tyyli) \
        .grid(column = pystyrivi, row = vaakarivi, columnspan = 2, sticky = tk.W, padx = [x_vasen, x_oikea], pady = [y_yla, y_ala])
# -------------------------------------------------------------------
def luo_entry(frame, teksti_muuttuja, pystyrivi, vaakarivi, x_vasen, x_oikea, y_yla, y_ala):
    """Luo entry-kirjoituspalkin ja asettaa sen frameen"""

    entry = ttk.Entry(frame, textvariable = teksti_muuttuja, width = 40, style = "bw.TEntry")
    entry.grid(column = pystyrivi, row = vaakarivi, columnspan = 4, sticky = tk.W, padx = [x_vasen, x_oikea], pady = [y_yla, y_ala])
    return entry
# -------------------------------------------------------------------
def luo_labelit_ja_entryt(frame, label_tekstit, entryt, muuttujat, pystyrivi, vaakarivi, x_vasen, x_oikea):
    """Luo teksti-labelit ja entry-kohdat tiedoille"""

    i = 0
    vaakarivi_laskuri = vaakarivi
    for teksti in label_tekstit:

        luo_label(frame, teksti, "white.TLabel", pystyrivi, vaakarivi_laskuri, x_vasen, x_oikea, 6, 0)
        entryt[i] = luo_entry(frame, muuttujat[i], pystyrivi, vaakarivi_laskuri + 1, x_vasen, x_oikea, 4, 10)

        i += 1
        vaakarivi_laskuri += 4
# -------------------------------------------------------------------
def luo_teksti_kentta(frame, pystyrivi, vaakarivi, korkeus, x_vasen, x_oikea):
    """Luo monirivisen teksti-kentän"""

    tekstikentta = tk.Text(frame, width = 40, height = korkeus, bg = "#101010", fg = "white", insertbackground = "white", font = ("Helvetica", 10))
    tekstikentta.grid(column = pystyrivi, row = vaakarivi, columnspan = 4, rowspan = int(korkeus / 2), sticky = tk.W, \
        padx = [x_vasen, x_oikea], pady = [4, 10])

    return tekstikentta
# -------------------------------------------------------------------
def luo_valikko(frame, teksti, pystyrivi, vaakarivi, x_vasen):
    """Luo teksti-labelin valikolle ja valikon"""

    luo_label(frame, teksti, "white.TLabel", pystyrivi, vaakarivi, x_vasen, 0, 6, 0)

    teksti_muuttuja = tk.StringVar()
    
    valikko = ttk.Combobox(frame, textvariable = teksti_muuttuja, state = "readonly", width = 20, style = "bw.TCombobox")
    valikko.grid(column = pystyrivi, row = vaakarivi + 1, columnspan = 4, sticky = tk.W, padx = [x_vasen, 0], pady = [4, 10])

    return valikko
# -------------------------------------------------------------------
def luo_button(frame, teksti, funktio, pystyrivi, vaakarivi, x_vasen, x_oikea, y_ala):
    """Luo buttonin"""

    ttk.Button(frame, text = teksti, style = "bw.TButton", command=funktio) \
        .grid(column = pystyrivi, row = vaakarivi, columnspan = 2, rowspan = 2, sticky = tk.W, padx = [x_vasen, x_oikea], pady = [10, y_ala])
# -------------------------------------------------------------------