import tkinter as tk  
import os
from unidecode import unidecode

def tachten(ten):
    a = ten.split()
    kq = a[-1]
    '''for i in range(len(a)-1):
        q = a[i][0].upper()
        kq = unidecode(kq).lower() + a[i][0].upper()
    return kq'''
    for i in range(len(a)-1):
        kq = kq + a[i][0].upper()
    return unidecode(kq)

def taouser(user,ou,domain,passwd):
    command =  f'dsadd user "CN={user},OU={ou},{domain}" -pwd {passwd}'
    #os.system(command)
    

if __name__ == "__main__":
    test = tk.Tk()
    test.title("create user ")
    test.configure(background="red")
    test.geometry("250x200")
    
    def executed():
        user = name_entry.get()
        ou = ou_entry.get()
        domain_NU = domain_entry.get().split(".")
        domain =f'dc={domain_NU[0]},dc={domain_NU[-1]}'
        passwd = passwd_entry.get()
        command =  f'dsadd user "CN={tachten(user)},OU={ou},{domain}" -pwd {passwd} '
        try: 
            if user and ou and domain and passwd:
                taouser(tachten(user), ou, domain, passwd)
                result_label.config(text=command)
                
            else:
                result_label.config(text="Vui lòng nhập đủ thông tin")
        except OSError as e:
            result_label.config(text=str(e))
    
    name_label = tk.Label(test, text="Nhập tên:", bg= "light green").place(x=10, y=20)
    name_entry= tk.Entry(test)
    name_entry.place(x=110, y=20)
    
    ou_label = tk.Label(test, text="Nhập ou", bg="light blue").place(x=10, y= 50)
    ou_entry = tk.Entry(test)
    ou_entry.place(x=110, y=50)
    
    domain_label = tk.Label(test, text="Nhập domain:").place(x=10, y=80)
    domain_entry = tk.Entry(test)
    domain_entry.insert(0, ".com")
    domain_entry.place(x=110, y=80)
    
    passwd_label = tk.Label(test, text="Nhập password").place(x=10, y=110)
    passwd_entry = tk.Entry(test, show="*")
    passwd_entry.place(x=110, y=110)
    
    comfirm_button = tk.Button(test, text="Tạo", command= executed)
    comfirm_button.place(x=80, y=140)
    
    result_label = tk.Label(test, text= "", bg="green", fg="white")
    result_label.place(x=10, y=170)
    test.mainloop()
    

