import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("MY 3rd application")
window.minsize(width=300,height=300)

label=ttk.Label(text="hello",font=("Times New Roman",20,"bold"))
label.pack()

def bt():
    text_input=user_input.get()
    label.config(text=text_input)

#Taking user input Entry()
user_input=ttk.Entry(show="*")
user_input.pack()
user_input.get()


#button
button=ttk.Button(text="Click",command=bt)
button.pack()

#button for quitting
quit_button=ttk.Button(text="Quit",command=window.destroy)
quit_button.pack()

window.mainloop()