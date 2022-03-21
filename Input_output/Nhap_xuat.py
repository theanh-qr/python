try:
	with open('input.inp','r',encoding = 'utf-8') as fileInp: # Mo file input va doc file 'r' = doc file xong bien no thanh bien fileInp
		ten = fileInp.readline().rstrip('\n') # readline la doc 1 dong va rstrip de bo ky tu xuong dong (readLines la doc nhieu dong)
		tuoi = int(fileInp.readline().rstrip('\n'))
	with open('output.out', 'wb') as fileOut: #Mo file output de ghi vao bien fileOut dung phuong thuc xu li wb
		stringToSave = '20 năm nữa, tuổi {} sẽ là  {}'.format(ten,tuoi + 20) #format la xu li chuoi sap xep chuoi theo thu tu va ky hieu bang {}
		fileOut.write(stringToSave.encode('utf8'))
except FileNotFoundError: #truong hop k tim thay file
	print("Khong tim thay file input.inp")
except:
	print("Dinh dang dau vao k hop le")		