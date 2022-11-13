from tkinter import*
from tkinter.ttk import Progressbar
from tkinter.ttk import Style

window = Tk()

#===== MAKING GEOMETRY =====
width_of_window = 427
height_of_window = 250
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)

window.geometry("%dx%d+%d+%d"%(width_of_window, height_of_window, x_coordinate, y_coordinate))
window.overrideredirect(1)

splash = Style()
splash.theme_use("clam")
splash.configure("red.Horizontal.TProgressbar", foreground="red", background="#4F4F4F")

#===== PROGRESS BAR =====
progress = Progressbar(window, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500, mode="determinate")

#===== MAIN WINDOW =====
def main_window():
    root = Tk()
    root.geometry("427x250")

    l1 = Label(root, text="ADD TEXT HERE", font=("Goudy Old Style", 24, "bold"), fg="Darkgrey", bg=None)
    l1.place(x=80, y=100)

    root.mainloop()

#===== PROGRESS =====
def bar():
    b1.config(text="", bg="#249794")
    b1.place(x=170, y=200)
    l4 = Label(window, text="Loading.....", font=("Goudy Old Style", 10), fg="White", bg="#249794")
    l4.place(x=0, y=210)

    import time

    r = 0
    for i in range(100):
        progress["value"] = r
        window.update_idletasks()
        time.sleep(0.03)
        r += 1
    window.destroy()
    main_window()

progress.place(x=10, y=235)

#===== FRAME =====
Frame(window, width=427, height=241, bg="#249794").place(x=0, y=0)
b1 = Button(window, width=10, height=1, text="Get Started", command=bar, border=0, fg="#249794")
b1.place(x=170, y=200)

#===== LABELS =====
l1 = Label(window, text="SPLASH", font=("Goudy Old Style", 18, "bold"), fg="White", bg="#249794")
l1.place(x=50, y=80)

l2 = Label(window, text="SCREEN", font=("Goudy Old Style", 18, "bold"), fg="White", bg="#249794")
l2.place(x=155, y=82)

l3 = Label(window, text="PROGRAMMED", font=("Goudy Old Style", 13), fg="White", bg="#249794")
l3.place(x=155, y=110)

window.mainloop()
