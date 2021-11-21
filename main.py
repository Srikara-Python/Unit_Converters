# This is the main file for this app
# Start Date - 20.11.21
# Srikara Narasimha
"""this is open-source and free to copy."""


from tkinter import * 



root = Tk()
root.title("All in One Converter - Srikara Narasimha")
root.geometry("500x500+0+0")
root.eval('tk::PlaceWindow . center')
orig_color = root.cget("background")

def met_kilometer():
    global meter_kilo
    global meter_kilo_entry
    meter_kilo = Toplevel()
    meter_kilo.title("Meter To Kilometer")
    meter_kilo_label1 = Label(meter_kilo, text="Please enter meter value below:- ")
    meter_kilo_label1.grid(row=0, column=0)
    meter_kilo_entry = Entry(meter_kilo)
    meter_kilo_entry.grid(row=1, column=0)
    meter_kilo_enterbutton = Button(meter_kilo, text="Enter", command=met_kilometer_answer)
    meter_kilo_enterbutton.grid(row=1, column=1)

def met_kilometer_answer():
    global meter_kilo_label2
    check_label2 = "meter_kilo_label2" in globals()
    if check_label2 == True:
        meter_kilo_label2.destroy()
    else:
        pass
    user_input_met_kilo = float(meter_kilo_entry.get())
    answer_met_kilo = user_input_met_kilo / 1000
    meter_kilo_label2 = Label(meter_kilo, text=str(answer_met_kilo) + (" Km"))
    meter_kilo_label2.grid(row=2, column=0)

    meter_kilo.mainloop()

def main_window():
    start_button.destroy()
    met_kil_button = Button(root, text="Meter To Kilometer", command=met_kilometer)
    met_kil_button.grid(row=1,column=0)
    
start_button = Button(root, text="Click ME!", command=main_window)
start_button.pack()







root.mainloop()