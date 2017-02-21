from tkinter import *
global text

class GUI(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.grid()

        self.lnameLabel = Label(master, text="Descripcion")
        self.lnameLabel.grid()

        self.sampleBox= Text(master,height=15, width=70)
        self.sampleBox.grid()

        self.lconsoleLabel = Label(master, text="Consola")
        self.lconsoleLabel.grid()
        self.var = StringVar()

        self.t = Text(master, height=20, width=70)
        self.t.config(background="Gray",fg="White")
        self.t.grid()


        self.submitButton = Button(command=self.buttonClick, text="Submit")
        self.submitButton.grid()



    def buttonClick(self):
        text=self.t.get("1.0",'end-1c')
        self.var=text
        self.master.destroy()


    def show(self):
        self.wait_window()
        return self.var

    def loadSample(self,texto):
        self.sampleBox.insert(END,texto)
        self.sampleBox.config(state=DISABLED)