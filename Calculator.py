from tkinter import *
root = Tk()
root.title("Calculator")
frame = LabelFrame(root, padx=10, pady=10)
frame.pack(padx=20, pady=20)

screen = Entry(frame, width=45, borderwidth=10)
screen.grid(row=0, column=0, columnspan=3)


#Define the button function:
def click_button(number):
    screen.insert(END,number)

def clear_button():
    screen.delete(0,END)

def add_button():
    global num
    global sign
    sign = 'add'
    num = int(screen.get())
    screen.delete(0,END)

def substract_button():
    global num
    global sign
    sign = 'substract'
    num = int(screen.get())
    screen.delete(0,END)

def multiply_button():
    global num
    global sign
    sign = 'multiply'
    num = int(screen.get())
    screen.delete(0,END)

def division_button():
    global num
    global sign
    sign = 'division'
    num = int(screen.get())
    screen.delete(0,END)

def equal_button():
    num2 = int(screen.get())
    if sign == 'add':
        screen.delete(0,END)
        screen.insert(0, num + num2)
    elif sign == 'substract':
        screen.delete(0,END)
        screen.insert(0, num - num2)
    elif sign == 'multiply':
        screen.delete(0,END)
        screen.insert(0, num * num2)
    elif sign == 'division':
        screen.delete(0,END)
        screen.insert(0, num / num2)


#Define the button:
button_1 = Button(frame, text="1", padx=40, pady = 20, command=lambda: click_button(1))
button_2 = Button(frame, text="2", padx=40, pady = 20, command=lambda: click_button(2))
button_3 = Button(frame, text="3", padx=40, pady = 20, command=lambda: click_button(3))

button_4 = Button(frame, text="4", padx=40, pady = 20, command=lambda: click_button(4))
button_5 = Button(frame, text="5", padx=40, pady = 20, command=lambda: click_button(5))
button_6 = Button(frame, text="6", padx=40, pady = 20, command=lambda: click_button(6))

button_7 = Button(frame, text="7", padx=40, pady = 20, command=lambda: click_button(7))
button_8 = Button(frame, text="8", padx=40, pady = 20, command=lambda: click_button(8))
button_9 = Button(frame, text="9", padx=40, pady = 20, command=lambda: click_button(9))

button_0 = Button(frame, text="0", padx=40, pady = 20, command=lambda: click_button(0))
button_add = Button(frame, text="+", padx=25, pady = 10, command=add_button)
button_substract = Button(frame, text="-", padx=25, pady = 10, command=substract_button)

button_equal = Button(frame, text="=", padx=39, pady = 20, command=equal_button)
button_multiply = Button(frame, text="*", padx=26, pady = 10, command=multiply_button)
button_division = Button(frame, text="/", padx=25, pady = 10, command=division_button)

button_clear = Button(frame, text="Clear", padx=130, pady = 20, command=clear_button)



#Show the button
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_substract.grid(row=4, column=2)

button_equal.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_division.grid(row=5, column=2)

button_clear.grid(row=6, column=0, columnspan=3)

root.mainloop()