import customtkinter
from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

app = customtkinter.CTk()
app.title('Random Password Generator')
app.geometry('390x285+480+200')
app.config(bg='#000')
app.resizable(False,False)

title_font = ('Arial',20,'bold')
subtitle_font = ('Arial',17,'bold')
password_font = ('Arial',14,'bold')
button_font = ('Arial',18,'bold')

min_password_length = 4
max_password_length = 16
default_password_length = 8

def generate_password():
    password_length = password_length_var.get()
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_text_box.configure(state='normal')
    password_text_box.delete(0,END)
    password_text_box.insert(0,password)
    password_text_box.configure(state='disabled')

def copy_password():
    password = password_text_box.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo(title='Copied',message="Password copied successfully to your clipboard.")
    else:
        messagebox.showinfo(title='Error',message="Generate a password to copy.")
def update_length_value(*args):
    length_label.configure(text=f"Password Length: {password_length_var.get()}")

title_label = customtkinter.CTkLabel(app,text='Random Password Generator',font=title_font,text_color='#fff',bg_color='#000')
title_label.place(x=55,y=20)

password_text_box = customtkinter.CTkEntry(app,font=password_font,state='disabled',text_color='#fff',fg_color='#000',border_color='#8807E9',width=280,height=30)
password_text_box.place(x=55,y=60)

length_label = customtkinter.CTkLabel(app,text=f"Password Length: {default_password_length}",font=subtitle_font,text_color='#fff',bg_color='#000')
length_label.place(x=55,y=110)

password_length_var = IntVar(value=default_password_length)
password_length_var.trace_add('write',update_length_value)

lenght_slider = customtkinter.CTkSlider(app,from_=min_password_length,to=max_password_length,progress_color='#0F0',button_color='#0f0',hover='#0f0',fg_color='#fff',bg_color='#000',height=20,width=290,variable=password_length_var)
lenght_slider.place(x=50,y=150)

generate_button = customtkinter.CTkButton(app,command=generate_password,font=button_font,text_color='#fff',text='Generate',fg_color='#6B0289',hover_color='#54026C',bg_color='#000',cursor='hand2',corner_radius=5,width=120,height=40)
generate_button.place(x=60,y=180)

copy_button = customtkinter.CTkButton(app,command=copy_password,font=button_font,text_color='#fff',text='Copy',fg_color='#6B0289',hover_color='#54026C',bg_color='#000',cursor='hand2',corner_radius=5,width=120,height=40)
copy_button.place(x=205,y=180)
app.mainloop()