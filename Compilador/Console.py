from tkinter import *
global text

class GUI(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.grid()

        self.lnameLabel = Label(master, text="Consola")
        self.lnameLabel.grid()
        self.var =StringVar()

        self.t = Text(master, height=20, width=40)
        self.t.grid()


        self.submitButton = Button(command=self.buttonClick, text="Submit")
        self.submitButton.grid()



    def buttonClick(self):
        text=self.t.get("1.0",END)
        self.var=text
        self.master.destroy()


    def show(self):
        self.wait_window()
        return self.var