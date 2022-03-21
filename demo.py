#lấy toàn bộ nội dung của thư viện decimal
#tu decimal import moi thu vao va moi thu la *
from decimal import*

#lay toi da 30 chu so phan nguyen va phan thap phan

getcontext().prec = 30

f=10/3
print(f)
#python phan biet chu hoa chu thuong
d=Decimal(10)/Decimal(3)
print(d)

#phan so trong python
from fractions import*

frac = Fraction(6,9)
print(frac)

#so phuc trong pyton
c = complex(2,5)
print(c)
#lay phan thuc
print(c.real)
#lay phan ao
print(c.imag)
