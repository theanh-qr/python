print("Nhap vao day so cua ban dc canh nhau boi khoang trang: ");
dayGiaTri = input()
dayDanhSachGT = dayGiaTri.split() #Nhap vao  tung so theo danh sach
try:  #Canh kiem tra du lieu xem co dung k
	danhSachSo = map(int,dayDanhSachGT) #Chuyen thanh danh sach
	tongDaySo = sum(danhSachSo) #Tinh tong cua chuoi do
	print("Tong cua day so la: ",tongDaySo)
except: #truong hop du lieu k hop le
	print("Du lieu k hop le!!!")
