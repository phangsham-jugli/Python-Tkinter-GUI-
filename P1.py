import tkinter as tk

#Tk()
window=tk.Tk()

#title()
window.title("My application")

#minsize
window.minsize(width=400,height=300)

#label()
label=tk.Label(text="Hello welcome",font=("Times New Roman",20,"italic"))
label.pack()

#mainloop()
window.mainloop()
