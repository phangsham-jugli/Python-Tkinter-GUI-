import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("MY application")
window.minsize(height=400,width=400)


#Radiobutton
radio_value=tk.StringVar()

def get_radio():
    print(radio_value.get())

option_1=ttk.Radiobutton(text="Male",variable=radio_value,value="male",command=get_radio)
option_2=ttk.Radiobutton(text="Female",variable=radio_value,value="Female",command=get_radio)

option_1.pack()
option_2.pack()


#Checkbutton
check_option=tk.IntVar()

def check_opt():
    print(check_option.get())


check_btn=ttk.Checkbutton(text="Agree with terms and condition",variable=check_option,command=check_opt)
check_btn.pack(side="bottom")


window.mainloop()