#Khai bao thu vien
import random
mk = str(random.randint(1,9999))
ok =" "
while ok !=mk:
      ok = str(random.randint(1,9999))
      print(ok)
      if ok==mk:
      print("Mat khau tim duoc la: "+mk)
      input()
