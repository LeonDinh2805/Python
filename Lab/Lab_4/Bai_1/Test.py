'''
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry

class Example(Frame):
    def __init__(self, parent):
         Frame.__init__(self, parent)

         self.parent = parent
         self.initUI()

    def initUI(self):
         self.parent.title("Review")
         self.pack(fill=BOTH, expand=True)

         frame1 = Frame(self)
         frame1.pack(fill=X)

         lbl1 = Label(frame1, text="Title", width=6)
         lbl1.pack(side=LEFT, padx=5, pady=5)

         entry1 = Entry(frame1)
         entry1.pack(fill=X, padx=5, expand=True)
        
         frame2 = Frame(self)
         frame2.pack(fill=X)

         lbl2 = Label(frame2, text="Author", width=6)
         lbl2.pack(side=LEFT, padx=5, pady=5)

         entry2 = Entry(frame2)
         entry2.pack(fill=X, padx=5, expand=True)

         frame3 = Frame(self)
         frame3.pack(fill=BOTH, expand=True)

         lbl3 = Label(frame3, text="Review", width=6)
         lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

         txt = Text(frame3)
         txt.pack(fill=BOTH, pady=5, padx=5, expand=True)

root = Tk()
root.geometry("300x300+300+300")
app = Example(root)
root.mainloop()



from tkinter import Tk, Frame, Label

class form(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="black")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Đăng kí học phần")
        self.pack(fill="both", expand=1)

        # Create a label with white text on a black background
        lbl1 = Label(self, text="Đăng kí học phần", foreground="white")
        lbl1.pack()

root = Tk()
root.geometry("450x250+300+300")
app = form(root)
root.mainloop()
'''

from tkinter import *
 
 
top = Tk()  
top.geometry("450x300") 

top.title("no")
# the label for user_name
user_name = Label(top,
                  text = "Username").place(x = 40,
                                           y = 60) 
   
# the label for user_password 
user_password = Label(top,
                      text = "Password").place(x = 40,
                                               y = 100) 
   
submit_button = Button(top,
                       text = "Submit").place(x = 40,
                                              y = 130)
   
user_name_input_area = Entry(top,
                             width = 30).place(x = 110,
                                               y = 60) 
   
user_password_entry_area = Entry(top,
                                 width = 30).place(x = 110,
                                                   y = 100) 
     
top.mainloop()