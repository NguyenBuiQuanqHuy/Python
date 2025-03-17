#Hàm lamda
sqr=lambda x:x**2
print(sqr(5))

#Hàm map
numbers=[1,2,3,4,5]
#Tạo danh sách chứa các giá trị bình phương tương ứng
#cách 1
sqare_nums=[]
for i in numbers:
    sqare_nums.append(i**2)
print(sqare_nums)
#cách 2: lis comprehension
sqare_nums2=[i**2 for i in numbers]
print(sqare_nums2)
#cách 3: hàm map
def sqare(n):
    return n**2

sqare_nums3=list(map(sqare,numbers))
print(sqare_nums3)
#cách 4: kết hợp lamda
sqare_nums4=list(map(lambda x:x**2,numbers))
print(sqare_nums4)

#hàm filter
def is_odd(n):
    return n%2 !=0
odd_number=list(filter(is_odd,numbers))
print(odd_number)

#hàm filter, lamda
odd_number=list(filter(lambda n:n%2!=0,numbers))
print(odd_number)