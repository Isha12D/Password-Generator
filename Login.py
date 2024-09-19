from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as c

conn = c.connect(host='localhost', password='IshaSql@562', user='root', database='loginauth')

if conn.is_connected():
    print("Connection established...")

cursor = conn.cursor()

root = Tk()
root.title("LogIn")
root.geometry("660x460")
root.minsize(width=660, height=460)

def show_message_box():
    messagebox.showinfo(message="Login Successfull")

def check():
    ckuname = username_entry.get()
    ckpass = password_entry.get()
    q2 = "select Username from user_info where exists( select Password from user_info where Password=(%s))"
    cursor.execute(q2, (ckpass,))
    test = cursor.fetchall()
    conn.commit()

    if test:
        if test[0][0] == ckuname:
            messagebox.showinfo(message="Login Successfull")
        else:
            messagebox.showinfo(message="Invalid Credentials")
    else:
        messagebox.showinfo(message="Invalid Credentials")

image = Image.open("py2.png")
resize_image = image.resize((644, 444))
photo = ImageTk.PhotoImage(resize_image)

canvas = Canvas(root, width=644, height=444)
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=photo)

canvas.create_text(322, 111, text="Login", fill="white", font=("comicsansms", 40))

username_value = StringVar()
password_value = StringVar()

canvas.create_text(220, 200, text="Username:", fill="white", font=("comicsansms", 16))
canvas.create_text(220, 240, text="Password:", fill="white", font=("comicsansms", 16))

username_entry = Entry(root, textvariable=username_value)
password_entry = Entry(root, textvariable=password_value)

canvas.create_window(400, 200, window=username_entry)
canvas.create_window(400, 240, window=password_entry)

btn = Button(root, text='Submit', bd='10', bg="white", width=15, command=check)
btn.place(x=250, y=300)


root.mainloop()
