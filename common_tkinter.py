import tkinter as tk
from tkinter import ttk
# -------------------------------------------------------------------
def luo_frame(root):
    # Luo frame widgetin padding = (left, top, right, bottom)
    frame = ttk.Frame(root, padding = f"10 10 10 10", style = "black.TFrame")
    frame.grid(column = 0, row = 0, sticky = (tk.N, tk.W, tk.E, tk.S))
    # Makes the frame expand to fill any extra space if the window is resized
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    #frame.rowconfigure(1, weight=1)
    #frame.columnconfigure(1, weight=1)

    # Tekee reunukset
    frame['borderwidth'] = 2
    frame['relief'] = 'sunken'

    return frame
# ------------------------------------------------------------------- 
def tee_label_teksti(frame, teksti, vaakarivi, pystyrivi):
    ttk.Label(frame, text = teksti, style = "white.TLabel") \
        .place(x = vaakarivi, y = pystyrivi, anchor = tk.NW)
# ------------------------------------------------------------------- 
# Luo teksti-labelit ja entry-kohdat asiakkaan tai laitteen tiedoille
def luo_labelit_ja_entryt(frame, tiedot_lista, entryt, tiedot, pystyrivi, vaakarivi):

    i = 0
    rivi_laskuri = vaakarivi
    for tieto in tiedot_lista:

        ttk.Label(frame, text = tieto, style = "white.TLabel") \
            .grid(column = pystyrivi, row = rivi_laskuri, columnspan = 2, sticky = (tk.W, tk.S), padx = [10, 0], pady = [6, 2])

        entryt[i] = ttk.Entry(frame, textvariable = tiedot[i], width = 40, style = "bw.TEntry")
        entryt[i].grid(column = pystyrivi, row = rivi_laskuri + 1, columnspan = 4, sticky = tk.W, padx = [10, 20])

        i += 1
        rivi_laskuri += 2
# -------------------------------------------------------------------
def luo_valikko(haku_frame, teksti, pystyrivi, vaakarivi):
    
    ttk.Label(haku_frame, text = teksti, style = "white.TLabel") \
        .grid(column = pystyrivi, row = vaakarivi, columnspan = 2, sticky = tk.W, padx = [0, 0], pady = [0, 0])

    teksti_muuttuja = tk.StringVar()
    
    combobox = ttk.Combobox(haku_frame, textvariable = teksti_muuttuja, state = "readonly", width = 20, style = "bw.TCombobox")
    combobox.grid(column = pystyrivi, row = vaakarivi + 1, columnspan = 4, sticky = tk.W, padx = [0, 0], pady = [0, 10])

    return combobox
# -------------------------------------------------------------------