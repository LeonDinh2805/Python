import os
import csv

def tachten(ten):
    a = ten.split()
    kq = a[0]
    for i in range(len(a)-1):
        kq = kq + a[i][0]
    return kq
#print(tachten("Dinh Le Quang Nguyen"))

def taouser(user,ou,domain,passwd):
    command =  f'dsadd user "CN={user},OU={ou},{domain}" -pwd {passwd} '
    print(command)
    #os.system(command)
    
'''
ten = str(input("Nhập tên người dùng: "))
username = tachten(ten)
password = int(input("Nhập mật khẩu người dùng: "))
domain = input("nhập tên domain: ")
ou = input("Nhập ou: ")'''

def doipass(username,password,ou,domain):
    command = "dsmod user " + chr(34) + "cn=" + username + ",ou="+ou+",dc="+domain+chr(34)+" -pwd "+password
    print(command)
    #os.system(command)
#doipass("Nguyendlq","123123","com","soloys")

def taoProfile(username,ou,domain):
    ip_Sever = input("Nhap Ip cua sever: ")
    nameFolder = input("Nhập tên thư mục muốn tạo folder: ")
    taofile = "mkdir C:\\"+nameFolder
    os.system(taofile)
    taofilesshare = "net share "+ nameFolder +"=C:\\"+nameFolder +" /grant:everyone,full"
    print(taofilesshare)
    pathProfile = " -profile " + chr(92)+chr(92) + ip_Sever+"\\profiles\\"+username
    print(pathProfile)
    command = "dsmod user "+ chr(34) +"cn="+username+",ou="+ou+",dc="+domain + chr(34)+pathProfile
    print(command)
#taoProfile("nguyendlq","com","soloys")

def delete_user(username, ou, domain):
    command = f'dsrm user "CN={username}",OU={ou},dc={domain}"'
    print(command)
    #os.system(command)
#delete_user("nguyendlq","com","soloys")


def install_service_web():
	cmd = "powershell.exe Install-windowsFeature - name Web-Server -IncludeManagermenttools"
	try:
		print(cmd)
		#os.system(cmd)
	except Exception as e:
		print(e)
  
def install_telnet_service():
    command = 'dism /online /Enable-Feature /FeatureName:TelnetClient'
    try:
        print(command)
        #os.system(command)
    except Exception as e:
        print(e)

def read_csv_file(file_path):
    user_data = []
    try: 
        with open(file_path, newline='', encoding='utf8') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                 if len(row) >= 3:
                      user = {
                           'user' : row[0],
                           'passwd' : row[1],
                           'ou' : row[2]
                      }
                      user_data.append(user)
            return user_data               
    except Exception as e:
        print(e)
        return None
#print(read_csv_file(r'E:\Python\Project\user.csv'))



def add_QTM_CTY(data,qtm):
    for user in data:
        user['OU']=f'{qtm}'
    return data
#print(add_QTM_CTY(read_csv_file(r'E:\Python\Project\user.csv'),'QTM_CTY'))

def change_user_in_data(data):
    for user in data:
        user['user'] = tachten(user['user'])
    return data
#print(change_user_in_data(add_QTM_CTY(read_csv_file(r'E:\Python\Project\user.csv'),'QTM_CTY')))

def create_profile(data):
    pass

def doi_pass_moi(data):
    for user in data:
        user['passwd'] = 'QTM2023@'
    return data
print(doi_pass_moi(change_user_in_data(add_QTM_CTY(read_csv_file(r'E:\Python\Project\user.csv'),'QTM_CTY'))))

def coppy():
    pass

def deploy():
    pass 



    
'''QUẢN TRỊ HỆ THỐNG BẰNG PYTHON
1.	Viết hàm tạo Một User trên hệ thống Domain Controller nhập từ bàn phím theo dạng tên sinh viên. Ví dụ sinh viên tên “Le Tan Dan Huy” , user tạo ra là HuyLTD
2.	Viết hàm cập nhật mật khẩu của Một User nhập từ bàn phím.
3.	Viết hàm tạo Profile và Home Dir cho Một user  nhập từ bàn phím.
4.	Viết hàm xóa Một User trên hệ thống Domain Controller.
5.	Viết hàm cài dịch vụ Web cho Server.
6.	Viết hàm cài dịch vụ Telnet cho Server.
7.	Viết hàm đọc file CSV
8.	Tạo OU từ CSV đã đọc, lưu ý OU cha là QTM_CTY
9.	Tạo tất cả User từ username và password từ file CSV đã đọc ở câu 7. Lưu ý tất cả User tạo ra phải có dạng HuyLTD nếu là tên theo họ.
10.	Tạo tất cả Profile cho các User của câu 9
11.	Đổi tất cả mật khẩu của các User đã tạo ở câu 9 thành QTM2023@
12.	Viết hàm thiết lập cho Một user chỉ định có quyền remote desktop
13.	Viết hàm copy file txt từ thư mục nguồn sang thư mục đích
14.	Deploy phần mềm Foxi Reader.msi 
15.	Cài đặt Website bằng IIS
16.	Tìm hiểu Join domain trên linux.'''