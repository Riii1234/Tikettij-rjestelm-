import tkinter as tk
from tkinter import ttk
# -------------------------------------------------------------------
def aloita_terminaali():
    """Käynnistää terminaalin ja luo tyylit widgeteille"""
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
from tiketit_tkinter import luo_tiketti_toiminnot
from haku_tkinter import luo_haku_toiminnot
from teknikot_tkinter import luo_teknikko_toiminnot
# -------------------------------------------------------------------
def luo_terminaalin_sisalto(root):
    """Luo välilehdet ja niiden sisällön"""

    # Luo framet eli välilehdet
    etusivu_frame = luo_frame(root)
    tiketti_frame = luo_frame(root)
    haku_frame = luo_frame(root)
    teknikko_frame = luo_frame(root)

    # Luo buttonit välilehtien vaihtamiseksi
    luo_buttons(etusivu_frame, tiketti_frame, haku_frame, teknikko_frame)
    luo_buttons(tiketti_frame, tiketti_frame, haku_frame, teknikko_frame)
    luo_buttons(haku_frame, tiketti_frame, haku_frame, teknikko_frame)
    luo_buttons(teknikko_frame, tiketti_frame, haku_frame, teknikko_frame)

    # Funktiot välilehdillä oleville asioille
    luo_etusivu_otsikko(etusivu_frame)
    luo_tiketti_toiminnot(tiketti_frame)
    luo_haku_toiminnot(haku_frame)
    luo_teknikko_toiminnot(teknikko_frame)

    # Aloitus-frame
    etusivu_frame.tkraise()
    
    # Ohjelman aloitus
    root.mainloop()
# -------------------------------------------------------------------
def luo_buttons(frame, tiketti_frame, haku_frame, teknikko_frame):
    """Luo välilehtien vaihtamiseen button-widgetit"""

    b1 = ttk.Button(frame, text = "Luo uusi tiketti", style = "bw.TButton", command = lambda:tiketti_frame.tkraise())
    b1.place(x = 1, y = 1, anchor = tk.NW)

    b2 = ttk.Button(frame, text = "Haku", style = "bw.TButton", command = lambda:haku_frame.tkraise())
    b2.place(x = 110, y = 1, anchor = tk.NW)

    b2 = ttk.Button(frame, text = "Teknikot", style = "bw.TButton", command = lambda:teknikko_frame.tkraise())
    b2.place(x = 199, y = 1, anchor = tk.NW)
# -------------------------------------------------------------------
def luo_etusivu_otsikko(etusivu_frame):
    """Luo otsikon etusivulle"""

    otsikko = tk.Label(etusivu_frame, text = "Tikettijärjestelmä", foreground = "white", background = "#202020", font = ("Helvetica", 30))
    otsikko.grid(column = 0, row = 0)
# -------------------------------------------------------------------