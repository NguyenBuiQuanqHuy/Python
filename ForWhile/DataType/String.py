truyen_kieu="""
 Buồn trông cửa bể chiều hôm,

Thuyền ai thấp thoáng cánh buồm xa xa?

Buồn trông ngọn nước mới sa,

Hoa trôi man mác biết là về đâu?

Buồn trông nội cỏ rầu rầu,

Chân mây mặt đất một màu xanh xanh.

Buồn trông gió cuốn mặt duềnh,

Ầm ầm tiếng sóng kêu quanh ghế ngồi.
"""
#Đếm tổng số từ trong đoạn thơ trên
#Đếm số lần xuất hiện của từng từ

words=[w.strip() for w in truyen_kieu.split()]
print(words)
print(f"Tổng số từ={len(words)}")

# Khởi tạo biến kiểu từ điển
words_count ={}
# Xét từng từ trong ds
for w in words:
    # Nếu từ ch có trong từ điển
    # Đưa từ này vào từ điển, khơi tạo sl=1
    if w not in words_count:
        words_count[w]=1
    #Ngược lại, nếu từ đã có trong từ điển thì tổng st tăng
    else:
        words_count[w]+=1
print(words_count)

#Display result
for w in words_count:
    print(w,words_count[w])

for k,v in words_count.items():
    print(k,':',v)

#Từ nào xuất hiện nhiều nhất
sorted_dict={k:v for k,v in \
                   sorted(words_count.items(),key=lambda item: item[1],reverse=True )}
print(list(sorted_dict.items())[0])