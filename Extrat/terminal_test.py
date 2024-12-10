from tkinter import *
from tkinter import ttk
# -------------------------------------------------------------------
def terminaalin_aloitus():
    root = Tk()
    root.title("Tikettijärjestelmä")

    frame = luo_frame(root)

    valilehdet(frame)

    # Lisää kaikkiin widgetteihin mainframessa lisätilaa
    for child in frame.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    # Ohjelman aloitus
    root.mainloop()
# -------------------------------------------------------------------
def luo_frame(root):
    # Luo mainframe frame widgetin 800=leveys, 600=korkeus
    mainframe = ttk.Frame(root, padding="3 3 800 600")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    # Makes the frame expand to fill any extra space if the window is resized
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    return mainframe
# -------------------------------------------------------------------
def valilehdet(frame):
    # Luo button-widgetin
    ttk.Button(frame, text="Luo uusi tiketti", command=tiketti_lehti(frame)).grid(column=2, row=2, sticky=W)
    ttk.Button(frame, text="Haku", command=haku_lehti(frame)).grid(column=4, row=2, sticky=W)
# -------------------------------------------------------------------
def tiketti_lehti(frame):
    
    ttk.Label(frame, text="Uusi asiakas").grid(column=4, row=4, sticky=W)
    #ttk.Button(frame,text="Uusi asiakas", command=uusi_asiakas).grid(column=4, row=4, sticky=W)
# -------------------------------------------------------------------
def haku_lehti(frame):
    ttk.Label(frame, text="Tiedonhaku").grid(column=4, row=4, sticky=W)

#feet = StringVar()
#meters = StringVar()
    # Luo entry-widgetin
#feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
    # Grid asettaa sen ruudulle
#feet_entry.grid(column=2, row=1, sticky=(W, E))

    # Luo label-widgetin
#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
    
#ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

    # focus määrittää kursorin aloituskohdan
#feet_entry.focus()
    # Jos painaa return (enter windowsissa), suoritetaan calculate (sama kuin button)
#root.bind("<Return>", calculate)

# -------------------------------------------------------------------

terminaalin_aloitus()

