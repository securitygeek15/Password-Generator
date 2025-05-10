import random  
import customtkinter as ctk
from tkinter import CENTER
import tkinter.messagebox as tsmg

ctk.set_appearance_mode('light')

def passgen():
    global password
    chars = "0123456789abcdefghijklmnopqrstuvwxyz$%&@"

    length = int(Entry.get())
    password = ""

    for i in range(length):
        password += random.choice(chars)

    label_result.configure(text=f"Password : {password}", text_color="black")

def copy_to_clipboard():
    try:
        win.clipboard_clear()
        win.clipboard_append(password)
        tsmg.showinfo("Copied", "Password copied to clipboard!")
    except:
        tsmg.showerror("Error", "No password to copy. Please generate one first.")

win = ctk.CTk()
win.geometry('400x400')
win.title("Password Generator")

label1 = ctk.CTkLabel(win,text="Password Generator",font=("Comic Sans Ms",20,'bold'),text_color='red')
label1.pack()

Entry = ctk.CTkEntry(win,font=("Rubik",17,'bold'),placeholder_text="Enter the length you want - ",width=250)
Entry.pack()

label_result = ctk.CTkLabel(win, text="", font=("Comic Sans Ms", 18, 'bold'))
label_result.pack()

Button1 = ctk.CTkButton(win,text="Generate",font=("Comic Sans Ms",24, 'bold'),text_color='white',fg_color='blue',command=passgen)
Button1.pack()

# New "Copy" button
Button2 = ctk.CTkButton(win,text="Copy",font=("Comic Sans Ms",18, 'bold'),text_color='white',fg_color='green',command=copy_to_clipboard)
Button2.pack()

win.mainloop()
