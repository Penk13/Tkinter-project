from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')

#Define the image:
my_img1 = ImageTk.PhotoImage(Image.open('pic1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('pic2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('pic3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('pic4.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('pic5.jpg'))

#Show on program:
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


#Make a list of image:
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


#Define the button function:
def forward(image_numbers):
    global my_label
    global forward_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image=image_list[image_numbers])
    forward_button = Button(root, text=">>", command=lambda :forward(image_numbers+1))
    back_button = Button(root, text="<<", command=lambda :back(image_numbers-1))

    if image_numbers == len(image_list)-1:
        forward_button = Button(root, text=">>", state=DISABLED)

    forward_button.grid(row=1, column=2)
    back_button.grid(row=1, column=0)
    my_label.grid(row=0, column=0, columnspan=3)

def back(image_numbers):
    global my_label
    global forward_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image=image_list[image_numbers])
    forward_button = Button(root, text=">>", command=lambda :forward(image_numbers+1))
    back_button = Button(root, text="<<", command=lambda :back(image_numbers-1))

    if image_numbers == 0:
        back_button = Button(root, text="<<", state=DISABLED)

    forward_button.grid(row=1, column=2)
    back_button.grid(row=1, column=0)
    my_label.grid(row=0, column=0, columnspan=3)


#Define the button:
exit_button = Button(root, text="Exit Program", command=root.quit)
forward_button = Button(root, text=">>", command=lambda: forward(1))
back_button = Button(root, text="<<", command=back, state=DISABLED)

#Show on program:
exit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2)
back_button.grid(row=1, column=0)

root.mainloop()