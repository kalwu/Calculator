from tkinter import *
root = Tk()
# mylabel1 = Label(root, text = "Hi")
# mylabel2 = Label(root, text = "Bellend")
#
# mylabel1.grid(row = 0, column = 0)
# mylabel2.grid(row = 1, column = 0)

ent = Entry(root, width = 45, borderwidth = 3)
ent.grid(row = 0, column = 0, columnspan = 3, padx = 5, pady = 5)

number = None

def buttonClick(num):
    global number
    numbers = ent.get()
    if numbers.find("+") != -1:
        numbers = numbers.replace("+", "")
        ent.delete(0, END)
        newnumber = int(str(numbers) + str(num))
        ent.insert(0, newnumber)
    else:
        ent.delete(0, END)
        newnumber = int(str(numbers) + str(num))
        ent.insert(0, newnumber)


def buttonClear():
    ent.delete(0, END)
    global number
    number = None
    return number

def buttonPlus():
    global number
    num = ent.get()
    num = int(num)
    ent.delete(0, END)
    ent.insert(0, "+")

    if number is None:
        number = num
    else:
        number += num
    return number


def buttonEqual():
    global number
    buttonPlus()
    ent.delete(0, END)
    ent.insert(0, number)
    number = None
    return number

butt1 = Button(root, text='1', padx = 40, pady = 20, command = lambda: buttonClick(1))
butt2 = Button(root, text='2', padx = 40, pady = 20, command = lambda: buttonClick(2))
butt3 = Button(root, text='3', padx = 40, pady = 20, command = lambda: buttonClick(3))
butt4 = Button(root, text='4', padx = 40, pady = 20, command = lambda: buttonClick(4))
butt5 = Button(root, text='5', padx = 40, pady = 20, command = lambda: buttonClick(5))
butt6 = Button(root, text='6', padx = 40, pady = 20, command = lambda: buttonClick(6))
butt7 = Button(root, text='7', padx = 40, pady = 20, command = lambda: buttonClick(7))
butt8 = Button(root, text='8', padx = 40, pady = 20, command = lambda: buttonClick(8))
butt9 = Button(root, text='9', padx = 40, pady = 20, command = lambda: buttonClick(9))
butt0 = Button(root, text='0', padx = 40, pady = 20, command = lambda: buttonClick(0))
buttPlus = Button(root, text='+', padx = 40, pady = 20, command = buttonPlus)
buttEqual = Button(root, text = "=", padx = 40, pady = 52, command = buttonEqual)
buttClear = Button(root, text = "Clear", padx = 80, pady = 20, command = buttonClear)

butt1.grid(row = 3, column = 0)
butt2.grid(row = 3, column = 1)
butt3.grid(row = 3, column = 2)

butt4.grid(row = 2, column = 0)
butt5.grid(row = 2, column = 1)
butt6.grid(row = 2, column = 2)

butt7.grid(row = 1, column = 0)
butt8.grid(row = 1, column = 1)
butt9.grid(row = 1, column = 2)

butt0.grid(row = 4, column = 0)
buttPlus.grid(row = 4, column = 1)
buttEqual.grid(row = 4, column = 2, rowspan = 2)

buttClear.grid(row = 5, column = 0, columnspan = 2)


root.mainloop()

