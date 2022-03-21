from tkinter import *
from tkinter import messagebox
from math import sqrt

def gPT():
    a = float(tb_Nhap_A.get())
    b = float(tb_Nhap_B.get())
    c = float(tb_Nhap_C.get())
    print("Giai phuong trinh bac 2: ax^2 + bx + c = 0")
    tb_x1.delete(0, END)
    tb_x2.delete(0, END)
    if a == 0:
        if b == 0:
            if c == 0:
                messagebox.showinfo("Thong bao","Phuong trinh vo so nghiem")
            else:
                messagebox.showinfo("Thong bao","Phuong trinh vo nghiem")
                #print("Phuong trinh vo nghiem!")
        else:
            if c == 0:
                tb_x1.insert("0")
                #print("Phuong trinh co 1 nghiem x = 0")
            else:
                tb_x1.insert(-c/b)
                #print("Phuong trinh co 1 nghiem x = ",-c/b)
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            messagebox.showinfo("Thong bao","Phuong trinh vo nghiem")
            #print("Phuong trinh vo nghiem!")
        elif delta == 0:
            tb_x1.insert(-b/(2 * a))
            #print("Phuong trinh co 1 nghiem X= ",-c/b)
        else:
            x1 = float((-b - sqrt(delta)) / (2 * a))
            x2 = float((-b + sqrt(delta)) / (2 * a))
            tb_x1.insert(0, x1)
            tb_x2.insert(0, x2)
            #print("Phuong trinh co 2 nghiem phan biet !")
            #print("x1 = ",float((-b - sqrt(delta)) / (2 * a)))
            #print("x2 = ",float((-b + sqrt(delta)) / (2 * a)))
# Tao ra 1 from moi
#<ten from> = Tk()
gpt = Tk()
# Tieu de
gpt.title("Giai phuong trinh bac 2")
# tao va add control vao from
# tao control: <ten control> = <kieu control><ten from>,(thuoc tinh 1),tt 2)
# Add control: <ten control>.pack()
lb_Nhap = Label(gpt,text="Nhap cac he so",font=("Arial" "bold"), fg="red")
lb_Nhap.pack()
#Nhap ho so A
lb_Nhap_A = Label(gpt,text="Nhap A",font=("Arial" "bold"))
lb_Nhap_A.pack()
tb_Nhap_A = Entry(gpt,width=30,font=("Consolas",12))
tb_Nhap_A.pack()
#Nhap ho so B
lb_Nhap_B = Label(gpt,text="Nhap B",font=("Arial" "bold"))
lb_Nhap_B.pack()
tb_Nhap_B = Entry(gpt,width=30,font=("Consolas",12))
tb_Nhap_B.pack()
#Nhap ho so C
lb_Nhap_C = Label(gpt,text="Nhap C",font=("Arial" "bold"))
lb_Nhap_C.pack()
tb_Nhap_C = Entry(gpt,width=30,font=("Consolas",12))
tb_Nhap_C.pack()
#Ket qua
lb_KQ = Label(gpt, text="Ket qua",font=("Arial" "bold"), fg="red")
lb_KQ.pack()
# x1
lb_x1 = Label(gpt, text="X1: ")
lb_x1.pack()
tb_x1 = Entry(gpt, width=30, font=("Consolas",12))
tb_x1.pack()
# x2
lb_x2 = Label(gpt, text="X2: ")
lb_x2.pack()
tb_x2 = Entry(gpt, width=30, font=("Consolas",12))
tb_x2.pack()
# button
btn_tinh = Button(gpt, text="Tinh", fg="red",
                bg="#ffffff", width=25, height=3, command=gPT)
btn_tinh.pack()
#dung form lai de xem
gpt.mainloop()            
