from tkinter import*
import time

root = Tk()
root.title("DIGITAL CLOCK")
root.geometry("700x250+20+20")

root.config(bg="#081923")

#===== CLOCK FUNCTION =====
def Clock():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))

    if int(h) > 12 and int(m) > 0:
        lbl_noon.config(text="PM")
    if int(h) > 12:
        h = str((int(h)-12))

    lbl_hr.config(text=h)
    lbl_min.config(text=m)
    lbl_sec.config(text=s)

    lbl_hr.after(200, Clock)

#===== CREATING LABELS =====

    #===== HOUR =====
lbl_hr = Label(root, text="12", font=("Imprint MT Shadow", 50, "bold"), bg="#087587", fg="White")
lbl_hr.place(x=20, y=20, width=150, height=150)

lbl_hr2 = Label(root, text="HOURS", font=("Imprint MT Shadow", 20, "bold"), bg="#087587", fg="White")
lbl_hr2.place(x=20, y=180, width=150, height=50)

    #===== MINUTE =====
lbl_min = Label(root, text="59", font=("Imprint MT Shadow", 50, "bold"), bg="#008EA4", fg="White")
lbl_min.place(x=190, y=20, width=150, height=150)

lbl_min2 = Label(root, text="MINUTES", font=("Imprint MT Shadow", 20, "bold"), bg="#008EA4", fg="White")
lbl_min2.place(x=190, y=180, width=150, height=50)

    #===== SECOND =====
lbl_sec = Label(root, text="59", font=("Imprint MT Shadow", 50, "bold"), bg="#DF002A", fg="White")
lbl_sec.place(x=360, y=20, width=150, height=150)

lbl_sec2 = Label(root, text="SECONDS", font=("Imprint MT Shadow", 20, "bold"), bg="#DF002A", fg="White")
lbl_sec2.place(x=360, y=180, width=150, height=50)

    #===== NONE =====
lbl_noon = Label(root, text="AM", font=("Imprint MT Shadow", 50, "bold"), bg="#DF002A", fg="White")
lbl_noon.place(x=530, y=20, width=150, height=150)

lbl_noon2 = Label(root, text="NOON", font=("Imprint MT Shadow", 20, "bold"), bg="#DF002A", fg="White")
lbl_noon2.place(x=530, y=180, width=150, height=50)

#===== CALLING CLOCK FUNCTION =====
Clock()

root.mainloop()