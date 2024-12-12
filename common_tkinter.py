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
def luo_label(frame, teksti, tyyli, pystyrivi, vaakarivi, x, y1, y2):
    """Luo teksti-labelin ja asettaa sen frameen"""

    ttk.Label(frame, text = teksti, style = tyyli) \
        .grid(column = pystyrivi, row = vaakarivi, columnspan = 2, sticky = tk.W, padx = [x, 0], pady = [y1, y2])
# -------------------------------------------------------------------
def luo_entry(frame, teksti_muuttuja, pystyrivi, vaakarivi, x, y):
    """Luo entry-kirjoituspalkin ja asettaa sen frameen"""

    entry = ttk.Entry(frame, textvariable = teksti_muuttuja, width = 40, style = "bw.TEntry")
    entry.grid(column = pystyrivi, row = vaakarivi, columnspan = 4, sticky = tk.W, padx = [x, 0], pady = [y, 0])
    return entry
# -------------------------------------------------------------------
def luo_labelit_ja_entryt(frame, label_tekstit, entryt, muuttujat, pystyrivi, vaakarivi):
    """Luo teksti-labelit ja entry-kohdat tiedoille"""

    i = 0
    vaakarivi_laskuri = vaakarivi
    for teksti in label_tekstit:

        luo_label(frame, teksti, "white.TLabel", pystyrivi, vaakarivi_laskuri, 10, 6, 0)
        entryt[i] = luo_entry(frame, muuttujat[i], pystyrivi, vaakarivi_laskuri + 1, 10, 4)

        i += 1
        vaakarivi_laskuri += 4
# -------------------------------------------------------------------
def luo_teksti_kentta(frame, pystyrivi, vaakarivi, korkeus):
    """Luo monirivisen teksti-kentän"""

    tekstikentta = tk.Text(frame, width = 40, height = korkeus, bg = "#101010", fg = "white", insertbackground = "white", font = ("Helvetica", 10))
    tekstikentta.grid(column = pystyrivi, row = vaakarivi, columnspan = 4, sticky = tk.W, padx = [10, 10])

    return tekstikentta
# -------------------------------------------------------------------
def luo_valikko(frame, teksti, pystyrivi, vaakarivi):
    """Luo teksti-labelin valikolle ja valikon"""

    luo_label(frame, teksti, "white.TLabel", pystyrivi, vaakarivi, 10, 6, 0)

    teksti_muuttuja = tk.StringVar()
    
    valikko = ttk.Combobox(frame, textvariable = teksti_muuttuja, state = "readonly", width = 20, style = "bw.TCombobox")
    valikko.grid(column = pystyrivi, row = vaakarivi + 1, columnspan = 4, sticky = tk.W, padx = [10, 0], pady = [4, 6])

    return valikko
# -------------------------------------------------------------------
def luo_button(frame, teksti, funktio, pystyrivi, vaakarivi, y2):
    """Luo buttonin"""

    ttk.Button(frame, text = teksti, style = "bw.TButton", command=funktio) \
        .grid(column = pystyrivi, row = vaakarivi, columnspan = 2, rowspan = 2, sticky = tk.W, padx = [10, 0], pady = [10, y2])
# -------------------------------------------------------------------