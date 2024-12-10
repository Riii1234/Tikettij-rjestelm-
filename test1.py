import tkinter as tk
from tkinter import ttk

def selection_changed(event, combo):
    selection = combo.get()

    print(f"Selected option: {selection}")


main_window = tk.Tk()
main_window.config(width=300, height=200)
main_window.title("Combobox")

def combomaker():
    combo = ttk.Combobox(values=["Python", "C", "C++", "Java"])
    combo.bind("<<ComboboxSelected>>", lambda event: selection_changed(event, combo))
    combo.place(x=50, y=50)


combomaker()
main_window.mainloop()



