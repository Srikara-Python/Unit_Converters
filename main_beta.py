# This is the main file for this app
# Start Date - 20.11.21
# Srikara Narasimha
"""this is open-source and free to copy."""
""" Under the unlicence licence. Read LICENCE page """

from tkinter import * 
from tkinter import messagebox

root = Tk()
root.title("All in One Converter - Srikara Narasimha")
# root.geometry("500x500+0+0")
root.eval('tk::PlaceWindow . center')
orig_color = root.cget("background")
root.resizable(False, False)
root.configure(bg='black')

main_entry = Entry(root)
main_entry.grid(row=0, column=0, columnspan=5)

def kilo_gram():
    try:
        user_input = float(main_entry.get())
        main_entry.delete(0, END)

        answer = user_input * 1000
        main_entry.insert(0, (str(answer) + "g"))

    except ValueError:
        error = messagebox.askokcancel("Value Error ", "Please Enter an valid expression")
        if error == True:
            pass
        else:
            root.quit()


def gram_kilo():
    try:
        user_input = float(main_entry.get())
        main_entry.delete(0, END)

        answer = user_input / 1000
        main_entry.insert(0, (str(answer) + "Kg"))

    except ValueError:
        error = messagebox.askokcancel("Value Error ", "Please Enter an valid expression")
        if error == True:
            pass
        else:
            root.quit()

def m_km():
    try:
        user_input = float(main_entry.get())
        main_entry.delete(0, END)

        answer = user_input / 1000
        main_entry.insert(0, (str(answer) + "Km"))

    except ValueError:
        error = messagebox.askokcancel("Value Error ", "Please Enter an valid expression")
        if error == True:
            pass
        else:
            root.quit()

def km_m():
    try:
        user_input = float(main_entry.get())
        main_entry.delete(0, END)

        answer = user_input * 1000
        main_entry.insert(0, (str(answer) + "m"))

    except ValueError:
        error = messagebox.askokcancel("Value Error ", "Please Enter an valid expression")
        if error == True:
            pass
        else:
            root.quit()

def clear():
    main_entry.delete(0, END)

kg_g = Button(root, text="Kg To g", command=kilo_gram, padx=15, borderwidth=1, highlightbackground = "green", highlightthickness = 1, bd=0)
kg_g.grid(row=1, column=0, columnspan=1)

g_kg = Button(root, text="g To Kg", command=gram_kilo, padx=15, borderwidth=1, highlightbackground = "green", highlightthickness = 1, bd=0)
g_kg.grid(row=1, column=1, columnspan=1)

m_km = Button(root, text="M To Km", command=m_km, borderwidth=1, highlightbackground = "green", highlightthickness = 1, bd=0)
m_km.grid(row=2, column=0, columnspan=1)

km_m = Button(root, text="Km To M", command=km_m, borderwidth=1, highlightbackground = "green", highlightthickness = 1, bd=0)
km_m.grid(row=2, column=1, columnspan=1)

clear_button = Button(root, text="Clear", command=clear, borderwidth=1, highlightbackground = "green", highlightthickness = 1, bd=0)
clear_button.grid(row=0, column=5, columnspan=1)
exit_button = Button(root, text="exit", command=root.destroy, borderwidth=1, highlightbackground = "green", highlightthickness = 1, bd=0)
exit_button.grid(row=0, column=6, columnspan=1)




root.mainloop()