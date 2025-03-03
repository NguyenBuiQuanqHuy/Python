# # Nhập chuỗi từ bàn phím
# chuoi = input("Nhập dãy từ (cách nhau bởi dấu phẩy): ")
#
# # Tách chuỗi thành danh sách các từ
# ds_tu = chuoi.split()
# print(ds_tu)
# # Sắp xếp danh sách theo thứ tự alphabet
# ds_tu.sort()
#
# # Ghép lại thành chuỗi với dấu phẩy
# ket_qua = ", ".join(ds_tu)
#
# # In kết quả
# print(ds_tu)
# print("Dãy từ sau khi sắp xếp:", ket_qua)

n=int(input())
list_of_lists=[]
for i in range(n):
    sublist=list(map(int,input().split()))
    list_of_lists.append(sublist)
print(list_of_lists)
even_num=[]
for sublist in  list_of_lists:
    for num in sublist:
        if num%2==0:
            even_num.append(num)
print(even_num)