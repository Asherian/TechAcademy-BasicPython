#Video page 108 Tkinter introduction pt1, pt2 pg 109, pt3 pg 110

import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgrey')

        self.varFName = StringVar()
        self.varLName = StringVar()

        self.lblFName = Label(self.master,text='First Name: ',font=("Helvetica",16), fg='black', bg='lightblue')
        self.lblFName.grid(row=0,column=0,padx=(30,0),pady=(30,0))

        self.lblLName = Label(self.master,text='Last Name: ',font=("Helvetica",16), fg='black', bg='lightblue')
        self.lblLName.grid(row=1,column=0,padx=(30,0),pady=(30,0))

        self.lblDisplay= Label(self.master,text='',font=("Helvetica",16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3,column=1,padx=(30,0),pady=(30,0))

        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica",16), fg='black', bg='lightblue')
        self.txtFName.grid(row=0,column=1,padx=(30,0),pady=(30,0))
        
#python tkinter pack manager - google recommend search terms for the geometry of pack commands
#python tkinter grid manager - google search for dan's preferred geometry tool.
#Never mix grid and pack - they will lock up the program trying to work.
        
        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica",16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1,column=1,padx=(30,0),pady=(30,0))

        self.btnSubmit= Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2,column=1,padx=(0,0),pady=(30,0), sticky=NE)
       #video 5, adding buttons. 
        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))
        
    def cancel(self):
        #Close the window
        self.master.destroy()
        
        
if __name__ =="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
