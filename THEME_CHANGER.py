from tkinter import*
from PIL import ImageTk

root = Tk()
root.title("THEME CHANGER")
root.geometry("400x600")

root.config(bg="White")

button_mode = True

#===== CREATING FUNCTION =====
def Customize():
    global button_mode

    if button_mode:
        button.config(image=off, bg="Black", activebackground="Black")
        root.config(bg="Black")
        button_mode = False

    else:
        button.config(image=on, bg="White", activebackground="White")
        root.config(bg="White")
        button_mode=True

#===== ACCESSING IMAGES =====
on = ImageTk.PhotoImage(file="IMAGES/LIGHT_MODE.png")
off = ImageTk.PhotoImage(file="IMAGES/DARK_MODE.png")

#===== BUTTON =====
button = Button(root, image=on, bd=0, bg="White", activebackground="White", command=Customize)
button.pack(padx=50, pady=50)

root.mainloop()