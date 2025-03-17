"""
 Viết ct quản lý ds các hình tròn trong mặt phẳng
 Mỗi hình tròn có các dữ liệu sau:
    Tâm là 1 điểm trong mặt phẳng
    Bán kính là số thực dương

Tạo 1 ds n hình tròn:
    Tâm hình tròn có khoảng cách từ tâm đến góc tọa độ lớn nhất
    Liệt kê tát cả các tập hình tròn giao nhau
"""
import numpy as np
class Point:
    def __init__(self,x,y):
        self.X = x
        self.Y = y
    def Distance(self,p):
        return np.sqrt((self.X-p.X)**2 + (self.Y-p.Y)**2)
p0=Point(0,0)
p1=Point(3,4)

d=p0.Distance(p1)
print("Distance",d)