#Bai_1
from datetime import datetime
class SinhVien:   
    truong = "Truong dai hoc da lat"

    def __init__(self, maSo: int, hoTen : str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    @property
    def maSo(self):
        return self.__maSo
    @property
    def hoTen(self):
        return self.__hoTen
    @property
    def ngaySinh(self):
        return self.__ngaySinh
    
    
    @maSo.setter
    def maSo(self,maso):
        if self.LaMaSoHopLe(maso):
            self.__maSo = maso
 
    @staticmethod
    def LaMaSoHopLe(maso:int):
        return len(str(maso)) == 7
    
    @classmethod
    def doiTenTruong(self,tenmoi):
        self.truong = tenmoi
        
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")
SinhVien1 = SinhVien("2111867","Đinh Lê Quang Nguyên","28/05/2001")
ngay_sinh = datetime(2000, 1, 1)
SinhVien2 = SinhVien(1234567, "Nguyen Van A", ngay_sinh)
SinhVien3 = SinhVien("2111868","Nguyen Van B","1/05/2000")
SinhVien4 = SinhVien("2111869","Nguyen Van C","1/01/2000")



class DanSachSV:
    def __init__(self) -> None:
        self.dssv = []
        
    def themSinhVien(self,sv:SinhVien):
        self.dssv.append(sv)
        
    def xuat(self):
        for sv in self.dssv:
            print(sv)
            
    def timSVTheoMssv(self,mssv : int):
        return [sv for sv in self.dssv if sv.maSo == mssv]
    
    def timVTSVTheoMssv(self,mssv:int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
        return -1
    
    def xoaSVTheoMssv(self,maSo:int)->bool:
        vt = self.timVTSVTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
        
    def timSVTheoTen(self, ten: str):
        ten = [sv for sv in self.dssv if ten.lower() in sv.hoTen.lower()]
        return ten

    
    def timSVSinhTruocNgay(self,ngay: datetime):
        timtheongay = [sv for sv in self.dssv if sv.ngaySinh < ngay]
        return timtheongay
    
    def docTuFile(self, tenfile):
     with open(tenfile, 'r', encoding='utf-8') as f:
        for hang in f:
            du_lieu = hang.strip().split('/')
            if len(du_lieu) == 4:
                maSo = int(du_lieu[0])
                hoTen = du_lieu[1]
                ngaySinh = datetime.strptime(du_lieu[3], '%d/%m/%Y')
                sv = SinhVien(maSo, hoTen, ngaySinh)
                self.themSinhVien(sv)
                
danh_sach_sv = DanSachSV()
danh_sach_sv.docTuFile("E:\Python\Lab2\Sinh_vien.txt")
danh_sach_sv.xuat()
'''
danh_sach_sv = DanSachSV()
danh_sach_sv.themSinhVien(SinhVien1)
danh_sach_sv.themSinhVien(SinhVien2)
danh_sach_sv.themSinhVien(SinhVien3)
danh_sach_sv.themSinhVien(SinhVien4)
print("Tất cả sinh viên:")
danh_sach_sv.xuat()

Kq = danh_sach_sv.timSVTheoMssv(1234567)
if Kq:
    print(Kq[0].hoTen)
else:
    print("không tìm thấy sinh viên")


danh_sach_sv.xoaSVTheoMssv(1234567)
print("Danh sách sau khi xóa sv có mã số 1234567 ")
danh_sach_sv.xuat()

ten = danh_sach_sv.timSVTheoTen("Nguyên")
if ten:
    print("Tìm theo tên:")
    for student in ten:
        student.xuat() 
else:
    print("Không có tên bạn vừa nhập")
'''

    

    
    






    



#Bai_3:
'''
class PhanSo:
    def __init__(self)->none:
        pass
    def rutGon(self):
        pass
    def __add__(self):
        pass
    def __sub__(self,other):
        pass
    def __mul__(self,other):
        pass
    def __truediv__(self,other):
        pass
    
a=PhanSo()
a.tu = 2
a.mau = 3
b = PhanSo(3,5)

print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
'''

#Bai_5:

    
    
    