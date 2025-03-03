"""
Kiểm tra số đẹp
"""
chuoi=input()
complex_list=eval(chuoi)
integer_list=[]
sum=0

for i in complex_list:
    if type(i) is int:
        integer_list.append(i)
        sum+=i
print(integer_list)
print(sum)