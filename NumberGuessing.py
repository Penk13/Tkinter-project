from tkinter import *
import random

root = Tk()
root.title("Number Guessing")
root.geometry("500x500")

key = random.randint(0,100)


#Function
def submit():
    try:
        int(guess.get())
        if guess.get() == key:
            print("You Win!")
        elif guess.get() < key:
            print("It is higher than ", guess.get())
        elif guess.get() > key:
            print("It is lower than ", guess.get())
        else:
            print(int(guess.get()))
    except:
        print('Please enter a number between 0-100')


#Define
guess_label = Label(root,text="Your Guess : ")
guess = Entry(root,text='Guess the Number!')
guess.insert(END,'enter your number')
submit_button = Button(root,text="SUBMIT",command=submit)

screen = Entry(root,width=50)


#Show
guess_label.grid(row=0, column=0)
guess.grid(row=0, column=1)
submit_button.grid(row=0, column=2)
screen.grid(row=1, column=0, columnspan=3)



root.mainloop()