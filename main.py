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



def kilo_meter():
    global kilo_meter
    global kilo_meter_entry
    kilo_meter = Toplevel()
    kilo_meter.title("Meter To Kilometer")
    kilo_meter_label1 = Label(kilo_meter, text="Please enter Kilometer value below:- ")
    kilo_meter_label1.grid(row=0, column=0)
    kilo_meter_entry = Entry(kilo_meter)
    kilo_meter_entry.grid(row=1, column=0)
    kilo_meter_enterbutton = Button(kilo_meter, text="Enter", command=kilo_meter_answer)
    kilo_meter_enterbutton.grid(row=1, column=1)  

def kilo_meter_answer():
    global kilo_meter_label2
    check_label2 = "kilo_meter_label2" in globals()
    if check_label2 == True:
        kilo_meter_label2.destroy()
    else:
        pass
    user_input_kilo_meter = float(kilo_meter_entry.get())
    answer_kilo_meter = user_input_kilo_meter * 1000
    kilo_meter_label2 = Label(kilo_meter, text=str(answer_kilo_meter) + (" m"))
    kilo_meter_label2.grid(row=2, column=0)

    kilo_meter.mainloop()



def main_window():
    start_button.destroy()
    met_kil_button = Button(root, text="Meter To Kilometer", command=met_kilometer)
    met_kil_button.grid(row=1,column=0)
    kil_met_button = Button(root, text="Kilometer to Meter", command=kilo_meter)
    kil_met_button.grid(row=1,column=1)
    
start_button = Button(root, text="Click ME!", command=main_window)
start_button.pack()







root.mainloop()