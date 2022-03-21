from tkinter import *
from tkinter import messagebox
import math

def demle():
    tb_KQ.delete(0, END)
    arr = tb_nhap.get().split(",")
    array = []
    count = 0
    for x in arr:
        array.append(int(x))
    for i in array:
        if i % 2 != 0:
            count += 1
    tb_KQ.insert(0, count)

def sumMang():
    tb_KQ.delete(0, END)
    arr = tb_nhap.get().split(",")
    array = []
    s = 0
    for x in arr:
        array.append(int(x))
    for i in array:
        s += i
    tb_KQ.insert(0, s)

def maxMin():
    tb_KQ.delete(0, END)
    arr = tb_nhap.get().split(",")
    array = []
    for x in arr:
        array.append(int(x))
    tb_KQ.insert(0, "Max: " + str(max(array)) + " | Min: " + str(min(array)))

def timChan():
    tb_KQ.delete(0, END)
    arr = tb_nhap.get().split(",")
    array = []
    s = ""
    for x in arr:
        array.append(int(x))
    array.sort()    
    for i in array:
        if i % 2 == 0:
            s += str(i) + ","
    s = s[0:len(s) - 1]
    tb_KQ.insert(0, s)
    
def timLe():
    tb_KQ.delete(0, END)
    arr = tb_nhap.get().split(",")
    array = []
    s = ""
    for x in arr:
        array.append(int(x))
    array.sort()    
    for i in array:
        if i % 2 !=0:
            s += str(i) + ","
    s = s[0:len(s) - 1]
    tb_KQ.insert(0, s)

def timSNT():
    tb_KQ.delete(0, END)
    arr = tb_nhap.get().split(",")
    array = []
    for x in arr:
        array.append(int(x))
    array.sort()
    s = ""

    for num in range(0, len(array)):
        if all(array[num] % i != 0 for i in range(2, int(math.sqrt(array[num])) + 1)):
               s += str(array[num]) +","
        s = s[0:len(s) - 1]
        tb_KQ.insert(0, s)

mang = Tk()
mang.title("Chương trình thao tác với mảng")
# Nhập mảng vào
lb_nhap = Label(mang, text="Nhập mảng", font=("Arial" "bold"), fg="red")
lb_nhap.pack()
tb_nhap = Entry(mang, width=30)
tb_nhap.pack()
               
lb_ChucNang = Label(mang, text="Nhập mảng", font=("Arial" "bold"), fg="red")
lb_ChucNang.pack()
# button chuc nang
# btn den phan tu le
btn_demle = Button(mang, text="Đếm phần tử lẻ", fg="red", bg="#ffffff", width=25, height=2, command=demle)
btn_demle.pack()
# Tính tổng mảng
btn_TinhTong = Button(mang, text="Tính tổng mảng", fg="red", bg="#ffffff", width=25, height=2, command=sumMang)
btn_TinhTong.pack()
#tim min max trong mang
btn_maxMin = Button(mang, text="Tìm max, min cảu mảng", fg="red", bg="#ffffff", width=25, height=2, command=maxMin)
btn_maxMin.pack()
#Xuất phần tử lẻ
btn_timLe = Button(mang, text="tìm phần tử lẻ", fg="red", bg="#ffffff", width=25, height=2, command=timLe)
btn_timLe.pack()
#xuat phần tử chẵn
btn_timChan = Button(mang, text="tìm phần tử chan", fg="red", bg="#ffffff", width=25, height=2, command=timChan)
btn_timChan.pack()
#xuat các số nguyên tố
btn_tim_SNT = Button(mang, text="tìm số nguyên tố", fg="red", bg="#ffffff", width=25, height=2, command=timSNT)
btn_tim_SNT.pack()
lb_KQ = Label(mang, text="kết quả tinh toán", font=("Arial" "bold"), fg="red")
lb_KQ.pack()
tb_KQ = Entry(mang, width=30)
tb_KQ.pack()
mang.mainloop()
