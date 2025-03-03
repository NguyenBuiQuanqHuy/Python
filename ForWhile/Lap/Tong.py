# Viết ct tính tổng các số đã nhập, bấm 0 để dừng
# Tính TBC các số đã nhập
tong  = 0
count = 0
while True:
    try: # khối lệnh có khả năng xảy ra lỗi
        n=int(input("Nhập 1 số nguyên (Nhập 0 để dừng): "))
        if n == 0:
            break
        else:
            tong += n
            count+=1
    except: # Xử lý khi có lỗi
        print("Dữ liệu ko hợp lệ")
        pass
print(f"Tổng các số đã nhập={tong}")
print(f"TBC các số đã nhập={tong/count}")
