
import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(500,200))
        self.master.title('Check files')
        self.master.config(bg='#F0F0F0')
        
        self.varFirst = StringVar()
        self.varSecond = StringVar()
        
        
        self.btnBrowOne = Button(self.master, text="Browse...", width=12, height=1,command=self.browse)
        self.btnBrowOne.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.btnBrowOne = Button(self.master, text="Browse...", width=12, height=1,command=self.browse)
        self.btnBrowOne.grid(row=1, column=0, padx=(30,0), pady=(30,0))
        

        self.txtFirst = Entry(self.master,text=self.varFirst, font=("Helvetica",16), fg='black', bg='white')
        self.txtFirst.grid(row=0,column=1,columnspan=2,padx=(30,0),pady=(30,0), sticky=NW)

        self.txtSecond = Entry(self.master,text=self.varSecond, font=("Helvetica",16), fg='black', bg='white')
        self.txtSecond.grid(row=1,column=1,columnspan=2,padx=(30,0),pady=(30,0), sticky=NW)

        self.btnCheck = Button(self.master, text="Check for files...", width=12, height=2,command=self.browse)
        self.btnCheck.grid(row=2, column=0, padx=(30,0), pady=(20,0))


        self.btnClose = Button(self.master, text="Close Program", width=12, height=2,command=self.Close)
        self.btnClose.grid(row=2, column=2, padx=(0,0), pady=(0,0),sticky=SE)





    def Close(self):
        self.master.destroy()
        
    def browse(self):
       fn=self.varFirst.get()
       sn=self.varSecond.get()

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

