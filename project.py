from tkinter import *

def button(num):
    
    global equation_text
    
    equation_text = equation_text + str(num)
    equation_lable.set(equation_text)

def equals():
    global equation_text
    
    try:
        total = str(eval(equation_text))
        equation_lable.set(total)
        equation_text = total
        
    except SyntaxError:
        equation_lable.set("syntax error")
        equation_text = ""
        
    except ZeroDivisionError:
        equation_lable.set("can't divide by zero")
        equation_text = ""
    
def clear():
    global equation_text
     
    equation_lable.set("")
    equation_text = ""

calculator = Tk()
calculator.title("calculator")
calculator.geometry("555x555")

equation_text = ""
equation_lable = StringVar()

Label=Label(calculator, textvariable=equation_lable, font=('times new roman', 30), bg="white", fg="black", width=30, height=2 )
Label.pack()

frame = Frame(calculator)
frame.pack()

button1= Button(frame, text=1,height=4, width=9 , font=35, command=lambda : button(1)) 
button1.grid(row=0, column=0)

button2= Button(frame, text=2,height=4, width=9 , font=35, command=lambda : button(2)) 
button2.grid(row=0, column=1)

button3= Button(frame, text=3,height=4, width=9 , font=35, command=lambda : button(3)) 
button3.grid(row=0, column=2)

button4= Button(frame, text=4,height=4, width=9 , font=35, command=lambda : button(4)) 
button4.grid(row=1, column=0)

button5= Button(frame, text=5,height=4, width=9 , font=35, command=lambda : button(5)) 
button5.grid(row=1, column=1)

button6= Button(frame, text=6,height=4, width=9 , font=35, command=lambda : button(6)) 
button6.grid(row=1, column=2)

button7= Button(frame, text=7,height=4, width=9 , font=35, command=lambda : button(7)) 
button7.grid(row=2, column=0)

button8= Button(frame, text=8,height=4, width=9 , font=35, command=lambda : button(8)) 
button8.grid(row=2, column=1)

button9= Button(frame, text=9,height=4, width=9 , font=35, command=lambda : button(9)) 
button9.grid(row=2, column=2)

button0= Button(frame, text=0,height=4, width=9 , font=35, command=lambda : button(0)) 
button0.grid(row=3, column=1)

add = Button(frame, text='+',height=4, width=9 , font=35, command=lambda : button('+')) 
add.grid(row=0, column=3)

sub = Button(frame, text='-',height=4, width=9 , font=35, command=lambda : button('-')) 
sub.grid(row=1, column=3)

mult = Button(frame, text='*',height=4, width=9 , font=35, command=lambda : button('*')) 
mult.grid(row=2, column=3)

div = Button(frame, text='/',height=4, width=9 , font=35, command=lambda : button('/')) 
div.grid(row=3, column=3)

equal= Button(frame, text='=',height=4, width=9 , font=35, command=equals) 
equal.grid(row=3, column=0)

dot= Button(frame, text='.',height=4, width=9 , font=35, command=lambda : button('.')) 
dot.grid(row=3, column=2)

clear= Button(calculator, text='clear',height=4, width=48 , font=35, command=clear) 
clear.pack()

calculator.mainloop()