import tkinter as tk
from tkinter import messagebox
from tkinter.constants import SUNKEN
import math

window = tk.Tk()
window.title('Calculator')

frame = tk.Frame(master=window, bg="silver", padx=30, pady=20)
frame.pack()

label1 = tk.Label(frame, text='BASIC CALCULATOR', bg='orange', fg='white', font=('Arial', 16, 'bold'))
label1.grid(row=0, column=0, columnspan=5, pady=(0, 10))

entry = tk.Entry(frame, relief=SUNKEN, borderwidth=4, width=28, font=('Arial', 14), justify='right')
entry.grid(row=1, column=0, columnspan=5, ipady=5, pady=5)

def touch(value):
    entry.insert(tk.END, value)

def equal():
    try:
        expr = entry.get()
        expr = expr.replace('sin', 'math.sin')
        expr = expr.replace('cos', 'math.cos')
        expr = expr.replace('tan', 'math.tan')
        expr = expr.replace('sqrt', 'math.sqrt')
        expr = expr.replace('pi', 'math.pi')
        expr = expr.replace('e', 'math.e')
        y = str(eval(expr))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except Exception:
        messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Button layout
button_texts = [
    ['7', '8', '9', '/', 'sin'],
    ['4', '5', '6', '*', 'cos'],
    ['1', '2', '3', '-', 'tan'],
    ['0', '.', '%', '+', 'sqrt'],
    ['pi', 'e', '(', ')', '^']
]

for r, row in enumerate(button_texts, start=2):
    for c, text in enumerate(row):
        if text == '^':
            btn = tk.Button(frame, text=text, width=6, height=2,
                            command=lambda t='**': touch(t))
        elif text in ['sin', 'cos', 'tan', 'sqrt']:
            btn = tk.Button(frame, text=text, width=6, height=2,
                            command=lambda t=text: touch(t + '('))
        elif text in ['pi', 'e']:
            btn = tk.Button(frame, text=text, width=6, height=2,
                            command=lambda t=text: touch(t))
        else:
            btn = tk.Button(frame, text=text, width=6, height=2,
                            command=lambda t=text: touch(t))
        btn.grid(row=r, column=c, padx=2, pady=2)

# Control buttons
button_clear = tk.Button(frame, text="Clear", width=13, height=2, command=clear, bg="#ff5252", fg="white")
button_clear.grid(row=7, column=0, columnspan=2, pady=5, padx=2)

button_back = tk.Button(frame, text="Back", width=6, height=2, command=backspace, bg="#ffa726", fg="white")
button_back.grid(row=7, column=2, pady=5, padx=2)

button_equal = tk.Button(frame, text="=", width=13, height=2, command=equal, bg="#66bb6a", fg="white")
button_equal.grid(row=7, column=3, columnspan=2, pady=5, padx=2)

window.mainloop()
