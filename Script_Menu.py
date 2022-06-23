import BENTON_FUNCTION_LIB as EM
import tkinter as tk
from tkinter import ttk

#Connecting to BlueZone
EM.Connect()

#Setting title
root = tk.Tk()
root.title("BlueZone Script Home")

#setting window size and where it pops up
width=700
height=400
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

# Create Tab Control
TAB_CONTROL = ttk.Notebook(root)

# Tab 1
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='   Home   ')
TAB_CONTROL.pack(expand=1, fill="both") 

# Tab 2
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='  Actions  ')

# Tab 3
TAB3 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB3, text='   Admin   ')

# Tab 4
TAB4 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB4, text='   Bulk   ')

# Tab 5
TAB5 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB5, text='   Dail   ')

# Tab 6
TAB6 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB6, text='   Notes   ')

# Tab 7
TAB7 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB7, text='  Notices  ')

# Tab 8
TAB8 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB8, text=' Utilities ')

# Tab 9
TAB9 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB9, text='  Testing  ')

#--------------------------------------- Tab Buttons / Text ------------------------------------------#
class TAB1_home:
    def __init__(self, TAB1):

        def things_button_command():
            EM.pf3()
            print("Pf3 has been pressed")
            
        #Updates Text
        tk.Label(TAB1, text="~ Updates ~", width=8, fg=("black"), font=("Arial", 14)).place(x=350, y=25, width="150", anchor="center")

        tk.Label(TAB1, text="6/23/2022 - This is an example of where the update would go!", justify="center", width=250, command=things_button_command).place(x=100, y=100, width="100", anchor="center")

class TAB2_actions:
    def __init__(self, TAB2):

        def do_things_button_command():
            #EM.SetCursor(20, 38)
            EM.SendKey("309189")
            print("Text has been sent...")

        tk.Button(TAB2, text="add Case Number", justify="center", width=10, font=("Arial, 10"), command=do_things_button_command).place(x=100, y=100, width="100", anchor="center")
        tk.Button(TAB2, text="add Case Number", justify="center", width=10, font=("Arial, 10"),command=do_things_button_command).place(x=100, y=100, width="100", anchor="center")


#TAB CLASSES
TAB1_home_page = TAB1_home(TAB1)
TAB2_actions_page = TAB2_actions(TAB2)

root.mainloop()