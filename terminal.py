import tkinter as tk
from tkinter import ttk
# -------------------------------------------------------------------
"""Käynnistää terminaalin ja luo tyylit widgeteille"""
def terminaalin_aloitus():
    root = tk.Tk()
    root.title("Tikettijärjestelmä")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    root.resizable(0, 0)
    
    style = ttk.Style()
    print(style.theme_names())
    style.theme_use("default")

    style.configure("white.TLabel", foreground = "white", background = "#202020", font = ("Helvetica", 10))
    style.configure("white2.TLabel", foreground = "white", background = "#101010", borderwidth = 3, relief = "solid", font = ("Helvetica", 20))
    
    style.configure("black.TFrame", background = "#202020")

    style.configure("bw.TButton", foreground = "white", background = "#101010", borderwidth = 3, relief="raised", font = ("Helvetica", 11))
    style.configure("bw2.TButton", foreground = "white", background = "#101010", borderwidth = 3, relief="raised", font = ("Helvetica", 16))
    
    style.configure("bw.TEntry", foreground = "white", fieldbackground = "#101010", insertcolor = "white", font = ("Helvetica", 10))
    
    style.configure("bw.TCombobox", foreground = "black", font = ("Helvetica", 10))

    return root
# -------------------------------------------------------------------
from common_tkinter import luo_frame
from tiketit_tkinter import tiketti_valilehti
from haku_tkinter import haku_valilehti
from teknikot_tkinter import teknikot_valilehti
# -------------------------------------------------------------------
def terminaalin_sisalto(root):
    # Luo framet eli välilehdet
    etusivu_frame = luo_frame(root)
    tiketti_frame = luo_frame(root)
    haku_frame = luo_frame(root)
    teknikot_frame = luo_frame(root)

    # Luo buttonit välilehtien vaihtamiseksi
    buttons(etusivu_frame, tiketti_frame, haku_frame, teknikot_frame)
    buttons(tiketti_frame, tiketti_frame, haku_frame, teknikot_frame)
    buttons(haku_frame, tiketti_frame, haku_frame, teknikot_frame)
    buttons(teknikot_frame, tiketti_frame, haku_frame, teknikot_frame)

    # Funktiot välilehdillä oleville asioille
    etusivu_valilehti(etusivu_frame)
    tiketti_valilehti(tiketti_frame)
    haku_valilehti(haku_frame)
    teknikot_valilehti(teknikot_frame)

    # Aloitus-frame
    etusivu_frame.tkraise()
    
    # Ohjelman aloitus
    root.mainloop()
# -------------------------------------------------------------------
def buttons(frame, tiketti_frame, haku_frame, teknikot_frame):
    # Luo välilehtien button-widgetit
    b1 = ttk.Button(frame, text = "Luo uusi tiketti", style = "bw.TButton",  \
        command = lambda:tiketti_frame.tkraise())
    b1.place(x = 1, y = 1, anchor = tk.NW)

    b2 = ttk.Button(frame, text = "Haku", style = "bw.TButton",  \
        command = lambda:haku_frame.tkraise())
    b2.place(x = 110, y = 1, anchor = tk.NW)

    b2 = ttk.Button(frame, text = "Teknikot", style = "bw.TButton",  \
        command = lambda:teknikot_frame.tkraise())
    b2.place(x = 199, y = 1, anchor = tk.NW)
# -------------------------------------------------------------------
"""Luo otsikon etusivulle"""
def etusivu_valilehti(etusivu_frame):

    otsikko = tk.Label(etusivu_frame, text = "Tikettijärjestelmä", foreground = "white", background = "#202020", font = ("Helvetica", 30))

    otsikko.grid(column = 0, row = 0)
# ------------------------------------------------------------------- 

