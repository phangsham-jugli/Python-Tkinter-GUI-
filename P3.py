import tkinter as tk
window=tk.Tk()
window.title("MY 3rd application")
window.minsize(width=300,height=300)

label=tk.Label(text="hello",font=("Times New Roman",20,"bold"))
label.pack()

def bt():
    text_input=user_input.get()
    label.config(text=text_input)

#Taking user input Entry()
user_input=tk.Entry(show="*")
user_input.pack()
user_input.get()


#button
button=tk.Button(text="Click",command=bt)
button.pack()

window.mainloop()