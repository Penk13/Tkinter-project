from tkinter import *
import random

root = Tk()
root.title("Rock Scissors Papper")


rock_button = Button(root, text='ROCK', padx=20, pady=25).grid(row=1,column=0)
scissors_button = Button(root, text='SCISSORS', padx=20, pady=25).grid(row=1,column=1)
paper_button = Button(root, text='PAPPER', padx=20, pady=25).grid(row=1, column=2)

screen = Entry(root).grid(row=0,column=0,columnspan=3)
submit_button = Button(root, text='SUBMIT', padx=120, pady=40).grid(row=2,column=0,columnspan=3)

root.mainloop()