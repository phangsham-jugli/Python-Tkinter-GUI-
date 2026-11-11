import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.title("my application")
window.minsize(width=400,height=400)

label=ttk.Label(text="Hello",font=("Times new roman",14,"bold"))
label.pack()

#Combobox
selected_country=tk.StringVar()
countries=ttk.Combobox(textvariable=selected_country,values=("India","Canada","Australia","Sweden","US"))
countries["state"]="readonly"
countries.pack()

def display_country(event):
    country_label=ttk.Label(text=f"{selected_country.get()}")
    country_label.pack()

countries.bind("<<ComboboxSelected>>",display_country)

#Listbox
food_items = ("Pizza", "Burger", "Garlic bread", "Nachos", "Salad")
fav_food = tk.StringVar(value=food_items)

food_list = tk.Listbox(window, listvariable=fav_food, height=5, selectmode="extended")
food_list.pack(pady=8)

def get_fav_food(event):
    food_indices = food_list.curselection()
    print("--- Current Selection ---")
    for i in food_indices:
        print(food_list.get(i))

food_list.bind("<ButtonRelease-1>", get_fav_food)

#Spinbox
counter=tk.IntVar(value=10)

def get_spin_box_value():
    print(f"Current spinbox value:{spin_box.get()}")

spin_box=ttk.Spinbox(from_=2,to=20,textvariable=counter,wrap=True,command=get_spin_box_value)
spin_box.pack(pady=8)

print(f"initial value spinbox:{spin_box.get()}")

window.mainloop()
