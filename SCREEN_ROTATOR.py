from tkinter import*
from PIL import ImageTk
import rotatescreen

root = Tk()
root.title("SCREEN ROTATOR")
root.geometry("500x500")
root.config(bg="#54C5D1")

root.resizable(False, False)

#===== IMAGE =====
photo = ImageTk.PhotoImage(file="SCREEN.png")
my_image = Label(image=photo)
my_image.place(x=0, y=0, width=500, height=500)

#===== CREATING FUNCTION =====
def Screen_Rotation(enter):
    screen = rotatescreen.get_primary_display()
    if enter == "up":
        screen.set_landscape()
    elif enter == "right":
        screen.set_portrait_flipped()
    elif enter == "down":
        screen.set_landscape_flipped()
    elif enter == "left":
        screen.set_portrait()

#===== CREATING BUTTON =====
Button(root, text="UP", command=lambda: Screen_Rotation("up"), bg="White", font=("arial 18"), width=5, bd=0).place(x=215, y=95)

Button(root, text="RIGHT", command=lambda: Screen_Rotation("right"), bg="White", font=("arial 18"), width=5, bd=0).place(x=354, y=230, width=76)

Button(root, text="DOWN", command=lambda: Screen_Rotation("down"), bg="White", font=("arial 18"), width=5, bd=0).place(x=215, y=360)

Button(root, text="LEFT", command=lambda: Screen_Rotation("left"), bg="White", font=("arial 18"), width=5, bd=0).place(x=74, y=230, width=70)

root.mainloop()
