# This is the main file for this app
# Start Date - 20.11.21
# Srikara Narasimha

from tkinter import * 



root = Tk()
root.title("All in One Converter - Srikara Narasimha")
root.geometry("500x500+0+0")
root.eval('tk::PlaceWindow . center')
orig_color = root.cget("background")


def main_window():
    start_button.destroy()
    
start_button = Button(root, text="Click ME!", command=main_window)
start_button.pack()







root.mainloop()