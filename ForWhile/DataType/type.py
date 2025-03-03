"""
Xử lý chuỗi

"""
s1="Welcome to Nha Trang city"
print(s1)
print(len(s1))
for ch in s1:
    print(ch,end=" ")
print(s1[10:])
print(s1[:5])

s2='Học tập suốt đởi.'
print(s2)
s3='The girl\'s name is Jane'
print(s3)
s4="""
Tháng Ba mùa con Trường đi lấy chồng
Mùa con An xuống mươn tắm rửa
"""
print(s4)

result = s4.find("voi")
print(result)
result =s4.replace("con","chú",1)
print(result)