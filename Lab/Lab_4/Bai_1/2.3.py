from tkinter import Tk, Text, TOP,BOTH,X,N,LEFT
from tkinter.ttk import Frame, Label,Entry

class Example(Frame):
     def __init__(self,parent):
          Frame.__init__(self,parent)
          
          self.parent = parent
          self.initUI()
     
     def initUI(self):
          self.parent.title("Review")
          self.pack(fill=BOTH,expand=True)
          
          frame1 = Frame(self)
          frame1.pack(fill=X)
          
          lbl1 = Label(frame1, text= "Title",width = 6)
          lbl1.pack(side=LEFT,padx=5,pady=5)
          
root = Tk()
root.geometry("300x300+300+300")
app = Example(root)
root.mainloop()