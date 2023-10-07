from datetime import datetime

class SinhVien:
    truong = "Dai hoc Da Lat"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo=maSo
        self.__hoTen=hoTen
        self.__ngaySinh=ngaySinh
    
    @property
    def maSo(self):
        return self.__maSo
    
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo=maso
    
    @property
    def ngaySinh(self):
        return self.__ngaySinh
    
    @ngaySinh.setter
    def ngaySinh(self, ngaySinh):
        self.__ngaySinh = ngaySinh

    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso))==7
    
    @classmethod 
    def doiTenTruong(self, tenmoi):
        self.truong=tenmoi
    
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"

    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []

    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSvTheoMSSV(self, mssv: int):
        return [sv for sv in self.dssv if sv.maSo == mssv]
    
    def timVTSvTheoMSSV(self, mssv:int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
            return -1
        
    def xoaSvTheoMSSV(self, maSo: int)->bool:
        vt = self.timSvTheoMSSV(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    
    def timSvTheoTen(self, ten:str):
        return [sv for sv in self.dssv if sv.hoTen.rsplit(' ', 1)[-1] == ten]

    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]

sv1 = SinhVien(2113014, "Pham anh quan", datetime.strptime("17/10/2003","%d/%m/%Y"))
sv2 = SinhVien(2111241, "anh quan pham", datetime.strptime("17/10/2003","%d/%m/%Y"))
sv3 = SinhVien(2124455, "anh quan", datetime.strptime("17/10/2003","%d/%m/%Y"))
sv4 = SinhVien(2154645, "quan anh", datetime.strptime("17/10/2003","%d/%m/%Y"))
sv5 = SinhVien(2123423, "Quan pham anh", datetime.strptime("17/10/2003","%d/%m/%Y"))

dssv = DanhSachSv()
dssv.themSinhVien(sv1)
dssv.themSinhVien(sv2)
dssv.themSinhVien(sv3)
dssv.themSinhVien(sv4)
dssv.themSinhVien(sv5)

dssv.xuat()

timMaso = int(input("Nhap ma so muon tim: "))
kq = dssv.timSvTheoMSSV(timMaso)
print(f"Da tim thay sinh vien co ma so: {timMaso}")
for sv in kq:
    sv.xuat()
print(dssv.timVTSvTheoMSSV(timMaso))

xoaMaSo = int(input("Nhap ma so muon xoa: "))
kq = dssv.xoaSvTheoMSSV(xoaMaSo)
dssv.xuat()

timTen = input("Nhap ten can tim: ")
kq = dssv.timSvTheoTen(timTen)
print(f"Da tim thay sinh vien co ten: {timTen}")
for sv in kq:
    sv.xuat()

timSVtruocNgay = datetime.strptime("15/06/2000", "%d/%m/%Y")
kq = dssv.timSvSinhTruocNgay(timSVtruocNgay)
print("Da tim thay sinh vien")
for sv in kq:
    sv.xuat()