from tkinter import*
from PIL import ImageTk
from resizeimage import resizeimage
import qrcode

class QR_CODE:

    def __init__(self, root):

        self.root = root
        self.root.title("QR CODE GENERATOR | Developed by DARK_BLAZE".center(210))
        self.root.geometry("900x500+200+50")

        self.root.resizable(FALSE, FALSE)

        title = Label(self.root, text="QR  CODE  GENERATOR", font=("DS-Digital", 40, "bold"), bg="#053246", fg="White", anchor=W, padx=20)
        title.place(x=0, y=0, relwidth=1)

        #===== EMPLOYEE DETAILS =====

            #===== VARIABLES =====
        self.var_emp_code = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_designation = StringVar()

            #===== EMPLOYEE DETAILS FRAME =====
        emp_frame = Frame(self.root, bd=5, relief=RIDGE, bg="White")
        emp_frame.place(x=50, y=90, width=500, height=380)

            #===== EMPLOYEE DETAILS TITLE =====
        emp_title = Label(emp_frame, text="Employee Details", font=("Goudy Old Style", 20), bg="#043256", fg="White", padx=20)
        emp_title.place(x=0, y=0, relwidth=1)
        
            #===== EMPLOYEE DETAILS LABELS =====
        lbl_emp_code = Label(emp_frame, text="Employee ID", font=("Times New Roman", 15, "bold"), bg="White")
        lbl_emp_code.place(x=20, y=60)

        lbl_emp_name = Label(emp_frame, text="Name", font=("Times New Roman", 15, "bold"), bg="White")
        lbl_emp_name.place(x=20, y=100)

        lbl_emp_department = Label(emp_frame, text="Department", font=("Times New Roman", 15, "bold"), bg="White")
        lbl_emp_department.place(x=20, y=140)

        lbl_emp_designation = Label(emp_frame, text="Designation", font=("Times New Roman", 15, "bold"), bg="White")
        lbl_emp_designation.place(x=20, y=180)

            #===== EMPLOYEE DETAILS ENTRIES =====
        txt_emp_code = Entry(emp_frame, font=("Times New Roman", 15), bg="Lightyellow", textvariable=self.var_emp_code)
        txt_emp_code.place(x=200, y=60, width=250)

        txt_emp_name = Entry(emp_frame, font=("Times New Roman", 15), bg="Lightyellow", textvariable=self.var_name)
        txt_emp_name.place(x=200, y=100, width=250)

        txt_emp_department = Entry(emp_frame, font=("Times New Roman", 15), bg="Lightyellow", textvariable=self.var_department)
        txt_emp_department.place(x=200, y=140, width=250)

        txt_emp_designation = Entry(emp_frame, font=("Times New Roman", 15), bg="Lightyellow", textvariable=self.var_designation)
        txt_emp_designation.place(x=200, y=180, width=250)

        #===== BUTTONS =====

            #===== GENERATE QR CODE =====
        btn_generate = Button(emp_frame, text=" Generate QR Code", font=("Times New Roman", 18, "bold"), bg="#2196F3", fg="White", bd=5, relief=GROOVE, command=self.generate)
        btn_generate.place(x=60, y=250, width=240, height=35)

            #===== CLEAR ENTRY FIELD =====
        btn_clear = Button(emp_frame, text="Clear", font=("Times New Roman", 18, "bold"), bg="#607D8B", fg="White", bd=5, relief=GROOVE, command=self.clear)
        btn_clear.place(x=300, y=250, width=120, height=35)

        self.msg = ""
        self.lbl_msg = Label(emp_frame, text=self.msg, font=("Times New Roman", 20), bg="White")
        self.lbl_msg.place(x=0, y=310, relwidth=1)

        #===== EMPLOYEE QR CODE =====

            #===== EMPLOYEE QR CODE FRAME =====
        qr_frame = Frame(self.root, bd=5, relief=RIDGE, bg="White")
        qr_frame.place(x=595, y=90, width=260, height=380)
            
            #===== EMPLOYEE QR CODE TITLE =====
        qr_title = Label(qr_frame, text="Employee OR Code", font=("Goudy Old Style", 20), bg="#043256", fg="White", padx=20)
        qr_title.place(x=0, y=0, relwidth=1)

            #===== EMPLOYEE QR CODE IMAGE =====
        self.qr_code = Label(qr_frame, text="No QR\nAvailable", font=("Times New Roman", 15), bg="#3F51B5", fg="White")
        self.qr_code.place(x=37.5, y=100, width=190, height=190)

    #===== GENERATE QR CODE FUNCTION =====
    def generate(self):
        if self.var_emp_code.get() == "" or self.var_name.get() == "" or self.var_department.get() == "" or self.var_designation.get() == "":
            self.msg = "All Fields are Required !!!!!"
            self.lbl_msg.config(text=self.msg, fg="Red")
        else:
            qr_data = {
                "Employee ID" : self.var_emp_code.get(),
                "Name" : self.var_name.get(),
                "Department" : self.var_department.get(),
                "Designation" : self.var_designation.get(),
            }
            qr_code = qrcode.make(qr_data)
            qr_code = resizeimage.resize_cover(qr_code, [190, 190])
            qr_code.save("Emp_" + str(self.var_emp_code.get()) + ".png")
            
            self.img = ImageTk.PhotoImage(file="Emp_" + str(self.var_emp_code.get()) + ".png")
            self.qr_code.config(image=self.img)

            self.msg = "QR Generated Successfully !!!!!"
            self.lbl_msg.config(text=self.msg, fg="Green")

    #===== CLEAR ENTRY FIELD FUNCTION =====
    def clear(self):
        self.var_emp_code.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_designation.set("")

        self.msg = ""
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image="")

if __name__ == "__main__":
    root = Tk()
    obj = QR_CODE(root)
    root.mainloop()
