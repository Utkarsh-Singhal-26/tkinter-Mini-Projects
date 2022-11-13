from tkinter import*
from PIL import Image, ImageTk

root = Tk()
root.title("PHOTO CHANGER")

#===== ACCESSING IMAGES =====
my_img_1 = ImageTk.PhotoImage(Image.open("1.png"))
my_img_2 = ImageTk.PhotoImage(Image.open("2.png"))
my_img_3 = ImageTk.PhotoImage(Image.open("3.png"))
my_img_4 = ImageTk.PhotoImage(Image.open("4.png"))
my_img_5 = ImageTk.PhotoImage(Image.open("5.png"))

my_img_list = [my_img_1, my_img_2, my_img_3, my_img_4, my_img_5]

#===== IMAGE =====
my_label = Label(root, image = my_img_1)
my_label.grid(row=0, column=0, columnspan=3)

#===== STATUS BAR =====
status = Label(root, text=f"Image 1 of {len(my_img_list)}", bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

#===== BACKWARD FUNCTION =====
def backward(image_number):
    global my_label
    global btn_backward
    global btn_forward

    my_label.grid_forget()
    my_label = Label(image=my_img_list[image_number-1])
    btn_backward = Button(root, text="<<", command=lambda: backward(image_number-1))
    btn_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    status = Label(root, text=f"Image {image_number} of {len(my_img_list)}", bd=1, relief=SUNKEN, anchor=E)

    if image_number==1:
        btn_backward = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    btn_backward.grid(row=1, column=0)
    btn_forward.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

#===== FORWARD FUNCTION =====
def forward(image_number):
    global my_label
    global btn_backward
    global btn_forward

    my_label.grid_forget()
    my_label = Label(image=my_img_list[image_number-1])
    btn_backward = Button(root, text="<<", command=lambda: backward(image_number-1))
    btn_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    status = Label(root, text=f"Image {image_number} of {len(my_img_list)}", bd=1, relief=SUNKEN, anchor=E)

    if image_number==5:
        btn_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    btn_backward.grid(row=1, column=0)
    btn_forward.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

#===== BUTTONS =====
btn_backward = Button(root, text="<<", command=backward, state=DISABLED)
btn_exit = Button(root, text="Exit Program", command=root.quit)
btn_forward = Button(root, text=">>", command=lambda: forward(2))

btn_backward.grid(row=1, column=0)
btn_exit.grid(row=1, column=1)
btn_forward.grid(row=1, column=2, pady=10)

root.mainloop()
