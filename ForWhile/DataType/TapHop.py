fruits=["apple","banana","orange","apple","kiwi","lemon"]

# for f in fruits:
#     print(f)
# fruit_set=set(fruits)
# print(fruit_set)
#
# fruit_set.add("durian")
# fruit_set.add("apple")
# print(fruit_set)

# s1={1,2,3,4}
# s2={3,4,5,6}
#
# u=s1.union(s2)
# print(u)
# g=s1.intersection(s2)
# print(g)
#
# h=s1-s2
# print(h)
#
# h2=s2-s1
# print(h2)



numbers =[1,2,'34',56,'57A']
print(len(numbers))
for i in numbers:
    print(i)

for i in range(len(numbers)):
    print(numbers[i])

numbers.append(123)
numbers.remove(2)
print(numbers)
s=sum([i for i in numbers if isinstance(i,int)])
print(f"Tổng ={s}")