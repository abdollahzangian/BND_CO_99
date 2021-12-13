from tkinter import Tk, Button,  Entry, Frame
from tkinter.constants import TOP


class View(Tk):
    def __init__(self):
        super(View, self).__init__()
        self.title("ماشین حساب")
        self.geometry("312x305+600+200")
        self.resizable(False, False)
        self.config(bg="#496961")
        
        input_fr = Frame(self, width=312, height=60, bd=2, bg= "Black")
        input_fr.pack(side=TOP)
        
        input_Ent = Entry(input_fr, width= 312, font=('arial', 14, 'italic'), bg="white", fg="black")
        input_Ent.pack()
        
        btn_fr = Frame(self, width=312, height=272.5, bd=2, bg="black")
        btn_fr.pack()

        clear = Button(btn_fr, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg="#496961")
        clear.grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
        
        divide = Button(btn_fr, text = "/", fg = "black", width = 10, height = 3, bd = 0 , bg="#496961")
        divide.grid(row = 0, column = 3, padx = 1, pady = 1)

        seven = Button(btn_fr, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg= "#8fb399")
        seven.grid(row = 1, column = 0, padx = 1, pady = 1)

        eight = Button(btn_fr, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#8fb399")
        eight.grid(row = 1, column = 1, padx = 1, pady = 1)
 
        nine = Button(btn_fr, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#8fb399")
        nine.grid(row = 1, column = 2, padx = 1, pady = 1)
 
        multiply = Button(btn_fr, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg="#496961")
        multiply.grid(row = 1, column = 3, padx = 1, pady = 1)

        four = Button(btn_fr, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg="#8fb399")
        four.grid(row = 2, column = 0, padx = 1, pady = 1)
 
        five = Button(btn_fr, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#8fb399")
        five.grid(row = 2, column = 1, padx = 1, pady = 1)
 
        six = Button(btn_fr, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#8fb399")
        six.grid(row = 2, column = 2, padx = 1, pady = 1)
 
        minus = Button(btn_fr, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg="#496961")
        minus.grid(row = 2, column = 3, padx = 1, pady = 1)

        one = Button(btn_fr, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#8fb399")
        one.grid(row = 3, column = 0, padx = 1, pady = 1)
 
        two = Button(btn_fr, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg ="#8fb399")
        two.grid(row = 3, column = 1, padx = 1, pady = 1)
 
        three = Button(btn_fr, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#8fb399")
        three.grid(row = 3, column = 2, padx = 1, pady = 1)
 
        plus = Button(btn_fr, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg="#496961")
        plus.grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row
 
        zero = Button(btn_fr, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#8fb399")
        zero.grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
        point = Button(btn_fr, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#8fb399")
        point.grid(row = 4, column = 2, padx = 1, pady = 1)
 
        answer = Button(btn_fr, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg="#496961")
        answer.grid(row = 4, column = 3, padx = 1, pady = 1)


