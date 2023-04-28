from tkinter import *
#import InitialScreen

class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = "white")
        self.setupGUI()

    def process(self, arg):
        result = ""
        # if someone types AC then clear the screen
        if (arg == "AC"):
            self.display["text"] = ""
        #backspace
        elif(arg == "bak"):
            self.display["text"] = self.display["text"][:-1]
        elif(arg == "enter"):
                InitialScreen.py
        elif (arg == "="):
            expr = self.display["text"]
            try:
                result = str(eval(expr))
                #rounding to 11 characters then ...
                if (int(len(str(result))) > 14):
                    self.display["text"] = result[:11]
                    self.display["text"] += "..."
                else:
                    self.display["text"] = result[:14]
            except: 
                self.display["text"] = "ERROR131"
        else:
            if (self.display["text"] == "ERROR131"):
                self.display["text"] = ""
            self.display["text"] += arg
    
    def setupGUI(self):
        self.display = Label(self, text = "", anchor = E, bg = "white",\
                height = 1, width = 15, font = ("TexGyreAdventor",45)) 
        self.display.grid(row = 0, column = 0, columnspan = 4) 

        for row in range (7):
                Grid.rowconfigure(self, row, weight = 1)
        for col in range (4):
            Grid.columnconfigure(self, col, weight = 1)

        img = PhotoImage(file = "images-gif/clr.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process("AC"))
        button.img = img
        button.grid(row = 3, column = 3, sticky = N+E+W+S)

        img = PhotoImage(file = "images-gif/bak.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process("bak"))
        button.img = img
        button.grid(row = 2, column = 3, sticky = N+E+W+S)

        img = PhotoImage(file = "images-gif/7.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process("7"))
        button.img = img
        button.grid(row = 2, column = 0, sticky = N+E+W+S)

        img = PhotoImage(file = "images-gif/8.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process("8"))
        button.img = img
        button.grid(row = 2, column = 1, sticky = N+E+W+S)

        img = PhotoImage(file = "images-gif/9.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process("9"))
        button.img = img
        button.grid(row = 2, column = 2, sticky = N+E+W+S)

        img = PhotoImage(file = "images-gif/4.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process("4"))
        button.img = img
        button.grid(row = 3, column = 0, sticky = N+E+W+S)

        img = PhotoImage(file = "images-gif/5.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process("5"))
        button.img = img
        button.grid(row = 3, column = 1, sticky = N+E+W+S)

        img = PhotoImage(file = "images-gif/6.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process("6"))
        button.img = img
        button.grid(row = 3, column = 2, sticky = N+E+W+S)

        img = PhotoImage(file = "images-gif/1.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process("1"))
        button.img = img
        button.grid(row = 4, column = 0, sticky = N+E+W+S)

        img = PhotoImage(file = "images-gif/2.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process("2"))
        button.img = img
        button.grid(row = 4, column = 1, sticky = N+E+W+S)

        img = PhotoImage(file = "images-gif/3.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process("3"))
        button.img = img
        button.grid(row = 4, column = 2, sticky = N+E+W+S)

        img = PhotoImage(file = "images-gif/0.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process("0"))
        button.img = img
        button.grid(row = 5, column = 0, sticky = N+E+W+S)

        img = PhotoImage(file = "images-gif/am.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process("AM"))
        button.img = img
        button.grid(row = 4, column = 3, sticky = N+E+W+S)

        img = PhotoImage(file = "images-gif/pm.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process("PM"))
        button.img = img
        button.grid(row = 5, column = 3, sticky = N+E+W+S)

        
        img = PhotoImage(file = "images-gif/colon.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process(":"))
        button.img = img
        button.grid(row = 5, column = 1, sticky = N+E+W+S)

        img = PhotoImage(file = "images-gif/enter.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0,\
                highlightthickness = 0, activebackground = "white",\
                command = lambda : self.process("enter"))
        button.img = img
        button.grid(row = 5, column = 2, sticky = N+E+W+S)
              
        

        self.pack(fill = BOTH, expand = 1)
        









window = Tk()
window.title("Set Time")
p = MainGUI(window)
window.mainloop()

