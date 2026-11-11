import tkinter as tk
from tkinter import ttk

window=tk.Tk()

window.minsize(height=500,width=500)
l=tk.Label(text="CalCulator",font=("Italic",20,"bold"),fg="red",bg="lightblue")
l.place(x=180,y=10)

#Entry
user_input=tk.Entry(width=44,borderwidth=5)
user_input.place(x=115,y=60)


#Buttons
def click(num):
    result=user_input.get()
    user_input.delete(0,tk.END)
    user_input.insert(0,str(result)+str(num))

b=ttk.Button(text='1',width=12,command=lambda :click(1))
b.place(x=120,y=100)

b=ttk.Button(text='2',width=12,command=lambda :click(2))
b.place(x=210,y=100)

b=ttk.Button(text='3',width=12,command=lambda :click(3))
b.place(x=300,y=100)

b=ttk.Button(text='4',width=12,command=lambda :click(4))
b.place(x=120,y=130)

b=ttk.Button(text='5',width=12,command=lambda :click(5))
b.place(x=210,y=130)

b=ttk.Button(text='6',width=12,command=lambda :click(6))
b.place(x=300,y=130)

b=ttk.Button(text='7',width=12,command=lambda :click(7))
b.place(x=120,y=160)

b=ttk.Button(text='8',width=12,command=lambda :click(8))
b.place(x=210,y=160)

b=ttk.Button(text='9',width=12,command=lambda :click(9))
b.place(x=300,y=160)

b=ttk.Button(text='0',width=12,command=lambda :click(0))
b.place(x=120,y=190)

#OPERATORS
def add():
    global i, operation
    i = int(user_input.get())
    operation = "+"
    user_input.delete(0, tk.END)



b=ttk.Button(text='+',width=12,command=add)
b.place(x=210,y=190)

def sub():
    global i, operation
    i = int(user_input.get())
    operation = "-"
    user_input.delete(0, tk.END)

b=ttk.Button(text='-',width=12,command=sub)
b.place(x=300,y=190)

def mul():
    global i, operation
    i = int(user_input.get())
    operation = "*"
    user_input.delete(0, tk.END)



b=ttk.Button(text='*',width=12,command=mul)
b.place(x=120,y=220)

def div():
    global i, operation
    i = int(user_input.get())
    operation = "/"
    user_input.delete(0, tk.END)

b=ttk.Button(text='/',width=12,command=div)
b.place(x=210,y=220)

def equal():
    n2 = int(user_input.get())
    user_input.delete(0, tk.END)

    if operation == "+":
        result = i + n2
    elif operation == "-":
        result = i - n2
    elif operation == "*":
        result = i * n2
    elif operation == "/":
        result = i / n2

    user_input.insert(tk.END, str(result))

b=ttk.Button(text='=',width=12,command=equal)
b.place(x=300,y=220)

#Clear
def clear():
    global i, operation
    user_input.delete(0, tk.END)
    i = 0
    operation = ""

b=ttk.Button(text='CLEAR',width=12,command=clear)
b.place(x=210,y=250)




window.mainloop()