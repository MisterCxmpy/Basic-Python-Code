import tkinter as tk
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

HEIGHT = 400
WIDTH = 600

def low():
    entry.delete(0, END)

    length = var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password

    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password

    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")

def generate():
    password1 = low()
    entry.insert(10, password1)

def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)

def save():
    file = open('passwords.txt','a+')
    file.write(entry.get() + '\n')
    file.close()

root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Random Password Generator")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="#764ce0")
frame.place(relwidth=1, relheight=1)
entry = tk.Entry(frame, bg="white", bd=5)
entry.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

c_label = Label(root, text="Length")
c_label.place()

copy_button = tk.Radiobutton(root, text="Copy", value=5, command=copy1, bg="#4926a3", height=40, width=40, indicatoron=0, selectcolor="#90ee90", font=("Arial Rounded MT", 15))
copy_button.place(relx=0.525, rely=0.27, relheight=0.1, relwidth=0.3, anchor="w")

generate_button = tk.Radiobutton(root, text="Generate", value=4, command=generate, bg="#4926a3", height=40, width=40, indicatoron=0, selectcolor="#90ee90", font=("Arial Rounded MT", 15))
generate_button.place(relx=0.525, rely=0.38, relheight=0.1, relwidth=0.3, anchor="w")

weakPass = tk.Radiobutton(root, text="Weak", variable=var, value=1, bg="#4926a3", height=40, width=40, indicatoron=0, selectcolor="#90ee90", font=("Arial Rounded MT", 15))
weakPass.place(relx=0.475, rely=0.27, relheight=0.1, relwidth=0.3, anchor="e")

mediumPass = tk.Radiobutton(root, text="Medium", variable=var, value=0, bg="#4926a3", height=40, width=40, indicatoron=0, selectcolor="#90ee90", font=("Arial Rounded MT", 15))
mediumPass.place(relx=0.475, rely=0.38, relheight=0.1, relwidth=0.3, anchor="e")

strongPass = tk.Radiobutton(root, text="Strong", variable=var, value=3, bg="#4926a3", height=40, width=40, indicatoron=0, selectcolor="#90ee90", font=("Arial Rounded MT", 15))
strongPass.place(relx=0.475, rely=0.49, relheight=0.1, relwidth=0.3, anchor="e")

savePass = tk.Radiobutton(root, text="Save", variable=var, value=6, command=save,bg="#4926a3", height=40, width=40, indicatoron=0, selectcolor="#90ee90", font=("Arial Rounded MT", 15))
savePass.place(relx=0.65, rely=0.60, relheight=0.1, relwidth=0.3, anchor="e")

combo = Combobox(root, textvariable=var1)

combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.place(relx=0.525, rely=0.49, relheight=0.1, relwidth=0.3, anchor="w")

root.mainloop()