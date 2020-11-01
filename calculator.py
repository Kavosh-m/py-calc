from tkinter import *

root = Tk()
root.title('A Simple Calculator')
#root.geometry('500x600')
width=490
height=390
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

#Screen of the calculator
isPushed = StringVar()
#print(isPushed.get() == '')
var = StringVar()
screenFrame = Frame(root, width=32, height=20, bd=4, relief=SUNKEN)
screenFrame.pack(fill=X, padx=10, pady=4)

buttonFrame = Frame(root, width=32, height=40, bd=4, relief=SUNKEN)
buttonFrame.pack(fill=X, padx=10, pady=4)


screenLabel = Label(
	screenFrame,
	text='',
	padx=1,
	pady=1,
	width=20,
	height=2,
	bg='#ffe6e6',
	fg='#332600',
	font=('Times', 20),
	anchor=E,
	textvariable=var
)

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
    var.set(' {} − '.format(s))
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
        var.set('{:,}'.format(x + y))
    elif s[1] == '−':
        var.set('{:,}'.format(x - y))
    elif s[1] == chr(215):
        var.set('{:,}'.format(x * y))
    else:
        var.set('{:,}'.format(x / y if x % y != 0 else x // y))



#functional Buttons
def clean():
    var.set('')
def decimal_point():
    s = var.get()
    var.set('{}.'.format(s))

    


#define Buttons
#numbers
num_1 = Button(buttonFrame, text='1', width=7, bg='#1a000d', fg='#33ffff', font=('Times', 20), command=one)
num_2 = Button(buttonFrame, text='2', width=7, bg='#1a000d', fg='#33ffff', font=('Times', 20), command=two)
num_3 = Button(buttonFrame, text='3', width=7, bg='#1a000d', fg='#33ffff', font=('Times', 20), command=three)
num_4 = Button(buttonFrame, text='4', bg='#1a000d', fg='#33ffff', font=('Times', 20), command=four)
num_5 = Button(buttonFrame, text='5', bg='#1a000d', fg='#33ffff', font=('Times', 20), command=five)
num_6 = Button(buttonFrame, text='6', bg='#1a000d', fg='#33ffff', font=('Times', 20), command=six)
num_7 = Button(buttonFrame, text='7', bg='#1a000d', fg='#33ffff', font=('Times', 20), command=seven)
num_8 = Button(buttonFrame, text='8', bg='#1a000d', fg='#33ffff', font=('Times', 20), command=eight)
num_9 = Button(buttonFrame, text='9', bg='#1a000d', fg='#33ffff', font=('Times', 20), command=nine)
num_0 = Button(buttonFrame, text='0', bg='#1a000d', fg='#33ffff', font=('Times', 20), command=zero)

#operations
addition = Button(buttonFrame, text='+', width=7, bg='#1a000d', fg='#33ffff', font=('Times', 20), command=add)
subtraction = Button(buttonFrame, text='−', bg='#1a000d', fg='#33ffff', font=('Times', 20), command=subtract)
multiplication = Button(buttonFrame, text=chr(215), bg='#1a000d', fg='#33ffff', font=('Times', 20), command=multiply)
division = Button(buttonFrame, text=chr(247), bg='#1a000d', fg='#33ffff', font=('Times', 20), command=divide)
equal = Button(buttonFrame, text='=', bg='#1a000d', fg='#33ffff', font=('Times', 20), command=calculate)

#functional Buttons
clear = Button(buttonFrame, text='C', bg='#1a000d', fg='#33ffff', font=('Times', 20), command=clean)
period = Button(buttonFrame, text='.', bg='#1a000d', fg='#33ffff', font=('Times', 20), command=decimal_point)

#Packing Buttons into the form
#Screen of the calculator
#screenFrame.grid(row=0, column=0, columnspan=4, sticky=W+E)
#screenLabel.pack()
# screenLabel.grid(row=0, column=0, columnspan=4, sticky=W+E)
screenLabel.pack(fill=X)

#numbers
num_1.grid(row=0, column=0, sticky=W+E)
num_2.grid(row=0, column=1, sticky=W+E)
num_3.grid(row=0, column=2, sticky=W+E)

num_4.grid(row=1, column=0, sticky=W+E)
num_5.grid(row=1, column=1, sticky=W+E)
num_6.grid(row=1, column=2, sticky=W+E)

num_7.grid(row=2, column=0, sticky=W+E)
num_8.grid(row=2, column=1, sticky=W+E)
num_9.grid(row=2, column=2, sticky=W+E)

num_0.grid(row=3, column=0, columnspan=2, sticky=W+E)

#operations
addition.grid(row=0, column=3, sticky=W+E)
subtraction.grid(row=1, column=3, sticky=W+E)
multiplication.grid(row=2, column=3, sticky=W+E)
division.grid(row=3, column=3, sticky=W+E)
equal.grid(row=4, column=3, sticky=W+E)

#functional Buttons
clear.grid(row=4, column=0, columnspan=3, sticky=W+E)
period.grid(row=3, column=2, sticky=W+E)




root.mainloop()
