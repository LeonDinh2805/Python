from Bai3 import PhanSo
class DsPhanSo:
    def __init__(self) -> None:
        self.ds = []
    def them(self,ps:PhanSo):
        self.ds.append(ps)
    def xuat(self):
        for ps in self.ds:
            print(ps,end = " ")
        print()
    def docTuFile(self,tenFile):
        with open (tenFile, 'r' , encoding='utf-8') as f:
            for hang in f:
                du_lieu = hang.split("/")
                ps = PhanSo(int(du_lieu[0]),int(du_lieu[1]))
                self.ds.append(ps)
    '''def demPsAm(self):
        dem =0 
        for ps in self.ds:
            if ps.tu * ps.mau < 0:
                dem+= 1
            return dem'''
        


            
    def demPsAm(self):
        dem =0 
        for ps in self.ds:
            if ps < 0:
                dem += 1
        return dem
        
    def laPhanSoAm(self):
        return self.tu *self.mau < 0
    
    def xuatPsAm(self):
        return [ps for ps in self.ds if ps < 0]
    
    



