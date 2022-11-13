from tkinter import*
from textblob import TextBlob

root = Tk()
root.title("SPELLING CHECKER")
root.geometry("1000x300")
root.config(bg="#DAE6F6")

#===== CREATING FUNTION =====
def Check():
    word = enter_text.get()
    check = TextBlob(word)
    right = str(check.correct())

    cs = Label(root, text="Correct Spelling is: ", font=("Vijaya", 23, "bold"), bg="#DAE6F6", fg="#364971")
    cs.place(x=70, y=230)

    spell.config(text=right)

#===== TITLE =====
heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#DAE6F6", fg="#364971")
heading.pack(pady=(40, 0))

#===== ENTRY FIELD =====
enter_text = Entry(root, justify=CENTER, width=45, font=("Vijaya", 22), bg="White", border=2)
enter_text.pack(pady=10)
enter_text.focus()

#===== BUTTON =====
button = Button(root, text="Check Spelling", font=("Trebuchet MS", 20, "bold"), fg="White", bg="Red", command=Check)
button.pack()

#===== DISPLAY SPELLING =====
spell = Label(root, font=("Vijaya", 25, "bold"), bg="#DAE6F6", fg="#364971")
spell.place(x=360, y=230)

root.mainloop()