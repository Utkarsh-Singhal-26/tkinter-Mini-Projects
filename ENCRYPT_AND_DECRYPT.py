from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import base64
import os

# ===== ENCRYPT =====
def Encrypt():
    
    password = code.get()

    if password == "dark_blaze":
        
        screen1 = Toplevel()
        screen1.title("ENCRYPTED TEXT")
        screen1.geometry("400x200")
        screen1.config(bg="#ed3833")

        message = text1.get(1.0, END)
        encoded_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encoded_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPTED TEXT", font="arial", fg="White", bg="#ed3833", bd=0).place(x=10, y=10)
        text2 = Text(screen1, font=("Goudy Old Style", 15), bg="White", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=50, width=380, height=100)

        text2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror("Error", "Please Type Password.....")

    elif password != "dark_blaze":
        messagebox.showerror("Error", "Please Type Correct Password.....")
        
# ===== DECRYPT =====
def Decrypt():
    
    password = code.get()

    if password == "dark_blaze":
        
        screen2 = Toplevel()
        screen2.title("DECRYPTED TEXT")
        screen2.geometry("400x200")
        screen2.config(bg="#00bd56")

        message = text1.get(1.0, END)
        decoded_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decoded_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPTED TEXT", font="arial", fg="White", bg="#00bd56", bd=0).place(x=10, y=10)
        text2 = Text(screen2, font=("Goudy Old Style", 15), bg="White", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=50, width=380, height=100)

        text2.insert(END, decrypt)

    elif password == "":
        messagebox.showerror("Error", "Please Type Password.....")

    elif password != "dark_blaze":
        messagebox.showerror("Error", "Please Type Correct Password.....")

def Main_Screen():

    global screen
    global code
    global text1

    screen = Tk()
    screen.title("ENCRYPTION AND DECRYPTION")
    screen.geometry("375x398")

    # ===== LOGO =====
    img = Image.open("IMAGES/ENCRYPT_DECRYPT.PNG")
    img = ImageTk.PhotoImage(img)
    screen.iconphoto(False, img)

    # ===== RESET =====
    def Reset():
        code.set("")
        text1.delete(1.0, END)

    # ===== VARIABLES =====
    code = StringVar()

    # ===== LABELS =====
    Label(text="Enter Text for Encryption and Decryption", fg="Black", font=("Goudy Old Style", 16)).place(x=10, y=10)
    Label(text="Enter Secret Key for Encryption and Decryption", fg="Black", font=("Goudy Old Style", 13)).place(x=20, y=160)

    # ===== ENTRIES =====
    text1 = Text(font=("Goudy Old Style", 20), bg="White", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)
    Entry(font=("Goudy Old Style", 20), show="*", textvariable=code, bg="White", relief=GROOVE, bd=0).place(x=20, y=190, width=345, height=30)

    # ===== BUTTONS =====
    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="White", bd=0, command=Encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="White", bd=0, command=Decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="White", bd=0, command=Reset).place(x=10, y=300) 

    screen.mainloop()

Main_Screen()
