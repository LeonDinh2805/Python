#FORM DANG NHAP
import tkinter as tk
from tkinter import *

root = tk.Tk()

root.geometry("400x100")

ten = tk.StringVar()
mk =tk.StringVar()

def submit():
    name =ten.get()
    password = mk.get()
    print("Tên Đăng Nhập: "+name)
    print("Mật khẩu là: "+password)
    ten.set("")
    mk.set("")
    
root.title("Login")
name_label = tk.Label(root, text = 'Tên Đăng Nhập', font=('Times New Roman',10, 'bold'))
name_entry = tk.Entry(root,textvariable = ten, font=('Times New Roman',13,'normal'))
passw_label = tk.Label(root, text = 'Mật Khẩu', font = ('Times New Roman',10,'bold'))
passw_entry=tk.Entry(root, textvariable = mk, font = ('Times New Roman',13,'normal'), show = '*')
sub_btn=tk.Button(root,text = 'Đăng Nhập', command = submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=3,column=1)
root.mainloop()

