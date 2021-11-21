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
    meter_kilo = Toplevel()
    meter_kilo.title("Meter To Kilometer")
    meter_kilo_entry = Entry(meter_kilo)
    meter_kilo_entry.grid(row=0, column=0)

    meter_kilo.mainloop()

def main_window():
    start_button.destroy()
    met_kil_button = Button(root, text="Meter To Kilometer", command=met_kilometer)
    met_kil_button.grid(row=1,column=0)
    
start_button = Button(root, text="Click ME!", command=main_window)
start_button.pack()







root.mainloop()