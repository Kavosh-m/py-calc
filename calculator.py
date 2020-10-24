from tkinter import *

root = Tk()
root.title('A Simple Calculator')
#root.geometry('500x600')
width=500
height=366
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

#Screen of the calculator
isPushed = StringVar()
#print(isPushed.get() == '')
var = StringVar()
#screenFrame = Frame(root)
screenLabel = Label(root, text='', width=20, height=3,padx=150, pady=13, bg='black',
                    fg='white', font=('Times', 15), textvariable=var)

#define commands
#numbers
def one():
    if isPushed.get() == '':
        s = var.get()
        var.set(s + '1')
    else:
        var.set('')
        var.set('1')
        isPushed.set('')
def two():
    if isPushed.get() == '':
        s = var.get()
        var.set(s + '2')
    else:
        var.set('')
        var.set('2')
        isPushed.set('')
def three():
    if isPushed.get() == '':
        s = var.get()
        var.set(s + '3')
    else:
        var.set('')
        var.set('3')
        isPushed.set('')
def four():
    if isPushed.get() == '':
        s = var.get()
        var.set(s + '4')
    else:
        var.set('')
        var.set('4')
        isPushed.set('')
def five():
    if isPushed.get() == '':
        s = var.get()
        var.set(s + '5')
    else:
        var.set('')
        var.set('5')
        isPushed.set('')
def six():
    if isPushed.get() == '':
        s = var.get()
        var.set(s + '6')
    else:
        var.set('')
        var.set('6')
        isPushed.set('')
def seven():
    if isPushed.get() == '':
        s = var.get()
        var.set(s + '7')
    else:
        var.set('')
        var.set('7')
        isPushed.set('')
def eight():
    if isPushed.get() == '':
        s = var.get()
        var.set(s + '8')
    else:
        var.set('')
        var.set('8')
        isPushed.set('')
def nine():
    if isPushed.get() == '':
        s = var.get()
        var.set(s + '9')
    else:
        var.set('')
        var.set('9')
        isPushed.set('')
def zero():
    if isPushed.get() == '':
        s = var.get()
        var.set(s + '0')
    else:
        var.set('')
        var.set('0')
        isPushed.set('')

#operations
def add():
    s = var.get()
    var.set(' {} + '.format(s))
    isPushed.set('')
def subtract():
    s = var.get()
    var.set(' {} - '.format(s))
    isPushed.set('')
def multiply():
    s = var.get()
    var.set(' {} {} '.format(s, chr(215)))
    isPushed.set('')
def divide():
    s = var.get()
    var.set(' {} {} '.format(s, chr(247)))
    isPushed.set('')
def calculate():
    isPushed.set('y')
    s = var.get()
    s = s.split()
    #exclude operands
    if '.' in s[0] or '.' in s[2]:
        x = float(s[0])
        y = float(s[2])
    else:
        x = int(s[0])
        y = int(s[2])
    #make the operation
    if s[1] == '+':
        var.set(x + y)
    elif s[1] == '-':
        var.set(x - y)
    elif s[1] == chr(215):
        var.set(x * y)
    else:
        var.set(x / y if x % y != 0 else x // y)



#functional Buttons
def clean():
    var.set('')
def decimal_point():
    s = var.get()
    var.set('{}.'.format(s))

    


#define Buttons
#numbers
num_1 = Button(root, text='1', font=('Times', 20), command=one)
num_2 = Button(root, text='2', font=('Times', 20), command=two)
num_3 = Button(root, text='3', font=('Times', 20), command=three)
num_4 = Button(root, text='4', font=('Times', 20), command=four)
num_5 = Button(root, text='5', font=('Times', 20), command=five)
num_6 = Button(root, text='6', font=('Times', 20), command=six)
num_7 = Button(root, text='7', font=('Times', 20), command=seven)
num_8 = Button(root, text='8', font=('Times', 20), command=eight)
num_9 = Button(root, text='9', font=('Times', 20), command=nine)
num_0 = Button(root, text='0', font=('Times', 20), command=zero)

#operations
addition = Button(root, text='+', font=('Times', 20), command=add)
subtraction = Button(root, text='-', font=('Times', 20), command=subtract)
multiplication = Button(root, text=chr(215), font=('Times', 20), command=multiply)
division = Button(root, text=chr(247), font=('Times', 20), command=divide)
equal = Button(root, text='=', font=('Times', 20), command=calculate)

#functional Buttons
clear = Button(root, text='C', font=('Times', 20), command=clean)
period = Button(root, text='.', font=('Times', 20), command=decimal_point)

#Packing Buttons into the form
#Screen of the calculator
#screenFrame.grid(row=0, column=0, columnspan=4, sticky=W+E)
#screenLabel.pack()
screenLabel.grid(row=0, column=0, columnspan=4, sticky=W+E)

#numbers
num_1.grid(row=1, column=0, sticky=W+E)
num_2.grid(row=1, column=1, sticky=W+E)
num_3.grid(row=1, column=2, sticky=W+E)

num_4.grid(row=2, column=0, sticky=W+E)
num_5.grid(row=2, column=1, sticky=W+E)
num_6.grid(row=2, column=2, sticky=W+E)

num_7.grid(row=3, column=0, sticky=W+E)
num_8.grid(row=3, column=1, sticky=W+E)
num_9.grid(row=3, column=2, sticky=W+E)

num_0.grid(row=4, column=0, columnspan=2, sticky=W+E)

#operations
addition.grid(row=1, column=3, sticky=W+E)
subtraction.grid(row=2, column=3, sticky=W+E)
multiplication.grid(row=3, column=3, sticky=W+E)
division.grid(row=4, column=3, sticky=W+E)
equal.grid(row=5, column=3, sticky=W+E)

#functional Buttons
clear.grid(row=5, column=0, columnspan=3, sticky=W+E)
period.grid(row=4, column=2, sticky=W+E)




root.mainloop()