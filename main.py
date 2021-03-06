# This is the main file for this app
# Start Date - 20.11.21
# Srikara Narasimha
"""this is open-source and free to copy."""
""" Under the unlicence licence. Read LICENCE page """

from tkinter import * 

root = Tk()
root.title("All in One Converter - Srikara Narasimha")
# root.geometry("500x500+0+0")
root.eval('tk::PlaceWindow . center')
orig_color = root.cget("background")
root.resizable(False, False)
root.configure(bg='black')

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



def min_sec():
    global min_sec
    global min_sec_entry
    min_sec = Toplevel()
    min_sec.title("Seconds To Minutes")
    min_sec_label1 = Label(min_sec, text="Please enter Minutes value below:- ")   
    min_sec_label1.grid(row=0, column=0)
    min_sec_entry = Entry(min_sec)
    min_sec_entry.grid(row=1, column=0)   
    min_sec_enterbutton = Button(min_sec, text="Enter", command=min_sec_answer)
    min_sec_enterbutton.grid(row=1, column=1)  

def min_sec_answer():
    global min_sec_label2
    check_label2 = "min_sec_label2" in globals()   
    if check_label2 == True:
        min_sec_label2.destroy()
    else:
        pass
    user_input_min_sec = float(min_sec_entry.get())
    answer_min_sec = user_input_min_sec * 60
    min_sec_label2 = Label(min_sec, text=str(answer_min_sec) + (" sec"))
    min_sec_label2.grid(row=2, column=0)


def sec_min():
    global sec_min
    global sec_min_entry
    sec_min = Toplevel()
    sec_min.title("Seconds To Minutes")
    sec_min_label1 = Label(sec_min, text="Please enter Seconds value below:- ")   
    sec_min_label1.grid(row=0, column=0)
    sec_min_entry = Entry(sec_min)
    sec_min_entry.grid(row=1, column=0)   
    sec_min_enterbutton = Button(sec_min, text="Enter", command=sec_min_answer)
    sec_min_enterbutton.grid(row=1, column=1)  

def sec_min_answer():
    global sec_min_label2
    check_label2 = "sec_min_label2" in globals()   
    if check_label2 == True:
        sec_min_label2.destroy()
    else:
        pass
    user_input_sec_min = float(sec_min_entry.get())
    answer_sec_min = user_input_sec_min / 60
    sec_min_label2 = Label(sec_min, text=str(answer_sec_min) + (" min"))
    sec_min_label2.grid(row=2, column=0)


def sec_hour():
    global sec_hour
    global sec_hour_entry
    sec_hour = Toplevel()
    sec_hour.title("Seconds To Hour")
    sec_hour_label1 = Label(sec_hour, text="Please enter Seconds value below:- ")   
    sec_hour_label1.grid(row=0, column=0)
    sec_hour_entry = Entry(sec_hour)
    sec_hour_entry.grid(row=1, column=0)   
    sec_hour_enterbutton = Button(sec_hour, text="Enter", command=sec_hour_answer)
    sec_hour_enterbutton.grid(row=1, column=1)  

def sec_hour_answer():
    global sec_hour_label2
    check_label2 = "sec_hour_label2" in globals()   
    if check_label2 == True:
        sec_hour_label2.destroy()
    else:
        pass
    user_input_sec_hour = float(sec_hour_entry.get())
    answer_sec_hour = user_input_sec_hour / 60 / 60
    sec_hour_label2 = Label(sec_hour, text=str(answer_sec_hour) + (" hours"))
    sec_hour_label2.grid(row=2, column=0)

def min_hour():
    global min_hour
    global min_hour_entry
    min_hour = Toplevel()
    min_hour.title("Minutes To Hour")
    min_hour_label1 = Label(min_hour, text="Please enter Minutes value below:- ")   
    min_hour_label1.grid(row=0, column=0)
    min_hour_entry = Entry(min_hour)
    min_hour_entry.grid(row=1, column=0)   
    min_hour_enterbutton = Button(min_hour, text="Enter", command=min_hour_answer)
    min_hour_enterbutton.grid(row=1, column=1)  

def min_hour_answer():
    global min_hour_label2
    check_label2 = "min_hour_label2" in globals()   
    if check_label2 == True:
        min_hour_label2.destroy()
    else:
        pass
    user_input_min_hour = float(min_hour_entry.get())
    answer_min_hour = user_input_min_hour / 60 
    min_hour_label2 = Label(min_hour, text=str(answer_min_hour) + (" hours"))
    min_hour_label2.grid(row=2, column=0)

def g_kg():
    global g_kg
    global g_kg_entry
    g_kg = Toplevel()
    g_kg.title("Minutes To Hour")
    g_kg_label1 = Label(g_kg, text="Please enter Grams value below:- ")   
    g_kg_label1.grid(row=0, column=0)
    g_kg_entry = Entry(g_kg)
    g_kg_entry.grid(row=1, column=0)   
    g_kg_enterbutton = Button(g_kg, text="Enter", command=g_kg_answer)
    g_kg_enterbutton.grid(row=1, column=1)  

def g_kg_answer():
    global g_kg_label2
    check_label2 = "g_kg_label2" in globals()   
    if check_label2 == True:
        g_kg_label2.destroy()
    else:
        pass
    user_input_g_kg = float(g_kg_entry.get())
    answer_g_kg = user_input_g_kg / 1000 
    g_kg_label2 = Label(g_kg, text=str(answer_g_kg) + (" Kg"))
    g_kg_label2.grid(row=2, column=0)


def kg_g():
    global kg_g
    global kg_g_entry
    kg_g = Toplevel()
    kg_g.title("Minutes To Hour")
    kg_g_label1 = Label(kg_g, text="Please enter KiloGrams value below:- ")   
    kg_g_label1.grid(row=0, column=0)
    kg_g_entry = Entry(kg_g)
    kg_g_entry.grid(row=1, column=0)   
    kg_g_enterbutton = Button(kg_g, text="Enter", command=kg_g_answer)
    kg_g_enterbutton.grid(row=1, column=1)  

def kg_g_answer():
    global kg_g_label2
    check_label2 = "kg_g_label2" in globals()   
    if check_label2 == True:
        kg_g_label2.destroy()
    else:
        pass
    user_input_kg_g = float(kg_g_entry.get())
    answer_kg_g = user_input_kg_g * 1000 
    kg_g_label2 = Label(kg_g, text=str(answer_kg_g) + (" Grams"))
    kg_g_label2.grid(row=2, column=0)

def main_window():
    start_label.destroy()
    start_button.destroy()

    exit_button = Button(root, command=root.destroy, text='Exit', bg='black', fg='purple')
    exit_button.grid(row=0, column=2)

    mass_label = Label(root, text="                 Distance", bg='black', fg='white')
    mass_label.grid(row=0, column=0, columnspan=4)
    divider_label1 = Label(root, text="---------------------------------------------------------------", bg='black', fg='white')
    divider_label1.grid(row=4, column=0, columnspan=5)

    time_label = Label(root, text="             Time", bg='black', fg='white')
    time_label.grid(row=5, column=0, columnspan=4)
    divider_label2 = Label(root, text="---------------------------------------------------------------", bg='black', fg='white')
    divider_label2.grid(row=8, column=0, columnspan=5)

    distance_label = Label(root, text="              Mass", bg='black', fg='white')
    distance_label.grid(row=9, column=0, columnspan=4)

    met_kil_button = Button(root, text="Meter To Kilometer", command=met_kilometer, bg='blue')
    met_kil_button.grid(row=1,column=0)
    kil_met_button = Button(root, text="Kilometer to Meter", command=kilo_meter, bg='blue', )
    kil_met_button.grid(row=1,column=1)


    sec_min_button = Button(root, text="Seconds To Minutes", command=sec_min, bg='green')
    sec_min_button.grid(row=6,column=2)
    min_sec_button = Button(root, text="Minutes to Seconds", command=min_sec, bg='green')
    min_sec_button.grid(row=6,column=0)
    min_hour_button = Button(root, text="Minutes to Hours", command=min_hour, bg='green')
    min_hour_button.grid(row=7,column=0)         
    sec_hour_button = Button(root, text="Seconds to Hours", command=sec_hour, bg='green')
    sec_hour_button.grid(row=6,column=1)

    g_kg_button = Button(root, text="Grams To KiloGrams", command=g_kg, bg='orange')
    g_kg_button.grid(row=11,column=0)
    kg_g_button = Button(root, text="Kilograms to Grams", command=kg_g, bg='orange')
    kg_g_button.grid(row=11,column=1)           

start_label = Label(root, text="Welcome! Click the below button to start.", bg='black', fg='white')
start_label.pack()
start_button = Button(root, text="Click ME!", command=main_window, bg='black', fg='grey')
start_button.pack()


root.mainloop()