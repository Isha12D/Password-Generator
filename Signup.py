from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import string
import mysql.connector as c

conn = c.connect(host='localhost', password='IshaSql@562', user='root', database='loginauth')

if conn.is_connected():
    print("Connection established...")

cursor = conn.cursor()

root = Tk()
root.title("SignUp")
root.geometry("660x460")
root.minsize(width=660, height=460)

def generate_pswd(length):
    while True:
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation
        if length < 4:
            error_box()
            return None
        else:
            password_list = [random.choice(s1), random.choice(s2), random.choice(s3), random.choice(s4)]
            password_list.extend(random.choices(s1 + s2 + s3 + s4, k=length - 4))
            random.shuffle(password_list)
            password = "".join(password_list)
            return password

def error_box():
    messagebox.showinfo("Error Message", "Please enter a password length greater than 3.")

def show_message_box():
    length = pswd_len_value.get()
    generated_password = generate_pswd(length)
    if generated_password:
        final_pswd_value.set(generated_password)
        message = f"Your generated Password is: {generated_password}"
        message_box = messagebox.showinfo("Generated Password", message)

        if message_box:
            root.clipboard_clear()
            root.clipboard_append(generated_password)

def get_info():
    uname=username_entry.get()
    pword=gen_pswd_entry.get()
    email=email_entry.get()
    phone=phone_entry.get()
    q1 = "insert into user_info(Username, Password, Email, Phone) values(%s, %s, %s, %s)"
    cursor.execute(q1, (uname, pword, email, phone))
    conn.commit()
    messagebox.showinfo("Registration Successful", "User registered successfully!")

image = Image.open("py2.png")
resize_image = image.resize((644, 444))
photo = ImageTk.PhotoImage(resize_image)

canvas = Canvas(root, width=644, height=444)
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=photo)

canvas.create_text(319, 60, text="SignUp", fill="white", font=("comicsansms", 30))

username_value = StringVar()
email_value = StringVar()
phone_value = StringVar()
pswd_len_value = IntVar()
final_pswd_value = StringVar()

canvas.create_text(220, 120, text="Username:", fill="white", font=("comicsansms", 16))
canvas.create_text(220, 160, text="E-Mail:", fill="white", font=("comicsansms", 16))
canvas.create_text(220, 200, text="Phone No.:", fill="white", font=("comicsansms", 16))
canvas.create_text(220, 240, text="Password Length:", fill="white", font=("comicsansms", 16))
canvas.create_text(220, 280, text="Generated Password:", fill="white", font=("comicsansms", 16))

username_entry = Entry(root, textvariable=username_value)
email_entry = Entry(root, textvariable=email_value)
phone_entry = Entry(root, textvariable=phone_value)
pswd_entry = Entry(root, textvariable=pswd_len_value)
gen_pswd_entry = Entry(root, textvariable=final_pswd_value)

canvas.create_window(400, 120, window=username_entry)
canvas.create_window(400, 160, window=email_entry)
canvas.create_window(400, 200, window=phone_entry)
canvas.create_window(400, 240, window=pswd_entry)
canvas.create_window(400, 280, window=gen_pswd_entry)

btn = Button(root, text='Generate Password', bd='10', bg="white", width=17, command=show_message_box)
canvas.create_window(218, 340, window=btn)

btn = Button(root, text='Submit', bd='10', bg="white", width=17, command=get_info)
canvas.create_window(382, 340, window=btn)

root.mainloop()
