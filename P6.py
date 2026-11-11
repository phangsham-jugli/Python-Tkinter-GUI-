import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("MY 3rd application")
window.minsize(width=300,height=300)

label=ttk.Label(text="hello",font=("Times New Roman",20,"bold"))
label.pack(pady=5)

def bt():
    text_input=user_input.get()
    label.config(text=text_input)

#Taking user input Entry()
user_input=ttk.Entry()
user_input.pack(pady=3)
user_input.get()


#button
button=ttk.Button(text="Click",command=bt)
button.pack(pady=3)

#button for quitting
quit_button=ttk.Button(text="Quit",command=window.destroy)
quit_button.pack(pady=3)

# above is P4.py

# ---------------------------------------------------- #

#Separator()
sep=ttk.Separator(orient="horizontal")
sep.pack(fill="x")


#Text()
text=tk.Text(height=5,width=25)
text.pack(pady=7)

#focus()
text.focus( )

#inert()//comments
text.insert("1.0","Enter your comments")

#to disable widget
text["state"]="disabled"

#enable button for text
def enable_txt():
    text["state"]="normal"

enable_button=ttk.Button(text="Enable text box",command=enable_txt)
enable_button.pack()

#to fetch text
def btt():
    input_text = text.get("1.0", "end")
    print(input_text)

button=ttk.Button(text="Click",command=btt)
button.pack()

window.mainloop()