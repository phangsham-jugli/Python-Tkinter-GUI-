import tkinter as tk
from tkinter import mainloop

window=tk.Tk()
window.minsize(width=300,height=300)

window.title("MY 2nd application")

label=tk.Label(text="Hello",font=("Times New Roman",20,"italic"))
label.pack()

#changing the label
label.config(text="Have a nice day")

#Button
count=0
def Cbutton():
    global count
    count +=1
    label.config(text=f"Thank you for clicking me! the button got click {count} times")

button=tk.Button(text="Click here",command=Cbutton)
button.pack(side="left")



window.mainloop()