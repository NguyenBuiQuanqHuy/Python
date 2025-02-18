

# def fibonanci(a):
#     if a<1:
#         return None
#     f1,f2=1,1
#     for f in range(a):
#         if f2>a: break
#         f1,f2=f2,f1+f2
#
#     return f1
# a=int(input())
# print(fibonanci(a))

def is_beautiful_number(n):
    # Chuyển số nguyên thành chuỗi để dễ kiểm tra từng chữ số
    num_str = str(n)

    # Duyệt qua từng cặp chữ số
    for i in range(1, len(num_str)-1):
        if num_str[i] > num_str[i + 1]:
            return False  # Nếu chữ số sau nhỏ hơn chữ số trước, không phải số đẹp

    return True  # Nếu không có cặp nào sai, số là số đẹp


# Nhập số nguyên dương
n = input()
print(is_beautiful_number(n))
