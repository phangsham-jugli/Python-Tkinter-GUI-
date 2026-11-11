import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("MY application")
window.minsize(width=200,height=200)

#Frame()
my_frame=ttk.Frame()
my_frame.pack(side="left",fill="both",expand=True)

label1=tk.Label(my_frame,text="Hello world!",bg="black")
label1.pack(side="left",expand=True,fill="both")

#part of main window
label1=tk.Label(text="Hello world!",bg="light blue")
label1.pack(side="left",expand=True,fill="both")

label2=tk.Label(text="How are you!",bg="light yellow")
label2.pack(side="left",expand=True,fill='both')

label3=tk.Label(text="Have a nice day!",bg="light green")
label3.pack(side="left",expand=True,fill='both')

window.mainloop()
