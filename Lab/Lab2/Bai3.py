'''
class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def __repr__(self):
        return f"Phân số({self.tu_so}, {self.mau_so})"

    def __add__(self, other):
        return PhanSo(self.tu_so * other.mau_so + other.tu_so * self.mau_so,
                        self.mau_so * other.mau_so)

    def __sub__(self, other):
        return PhanSo(self.tu_so * other.mau_so - other.tu_so * self.mau_so,
                        self.mau_so * other.mau_so)

    def __mul__(self, other):
        return PhanSo(self.tu_so * other.tu_so,
                        self.mau_so * other.mau_so)

    def __truediv__(self, other):
        return PhanSo(self.tu_so * other.mau_so,
                        self.mau_so * other.tu_so)
        
a= PhanSo(2,3)
b = PhanSo (3,5)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a)
print(b)
'''

import math
class PhanSo:
    def __init__(self,tu=1,mau=1)-> None:
        self.tu = tu
        self.mau = mau if mau != 0 else 1
    def __str__(self) ->str:
        return f"{self.tu}/{self.mau}"
    def rutGon(self):
        ucln = math.gcd(self.tu,self.mau)
        self.tu //= ucln
        self.mau //= ucln
    def __add__(self,other):
        kq = PhanSo()
        if not isinstance(other,PhanSo):
            other = PhanSo(other)
        kq.tu = self.tu * other.mau + self.mau * other.tu
        kq.mau = self.mau * other.mau 
        kq.rutGon()
        return kq
    
    def __lt__(self,other):
        kq = PhanSo()
        if not isinstance(other,PhanSo):
            other = PhanSo(other)
        return self.tu * other.mau + self.mau * other.tu <  self.mau * other.tu 

    def __sub__(self,other):
        kq = PhanSo()
        if not isinstance(other,PhanSo):
            other = PhanSo(other)
        kq.tu = self.tu * other.mau - self.mau * other.tu
        kq.mau = self.mau * other.mau 
        kq.rutGon()
        return kq
    
    
    def __mul__(self, other):
        kq = PhanSo()
        if not isinstance(other,PhanSo):
            other = PhanSo(other)
        kq.tu=self.tu * other.tu
        kq.mau=self.mau * other.mau
        kq.rutGon()
        return kq

    def __truediv__(self, other):
        kq = PhanSo()
        if not isinstance(other,PhanSo):
            other = PhanSo(other)
        kq.tu=self.tu * other.mau
        kq.mau=self.mau * other.tu
        kq.rutGon()
        return kq
        

        
ps1 = PhanSo(4,5)
ps2 = PhanSo(3,5)
print (ps1 < ps2)

