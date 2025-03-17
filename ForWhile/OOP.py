import math
from collections import defaultdict


class Shape:
    def getArea(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getArea(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


while True:
    try:
        n = int(input("Nhập số lượng hình vẽ (n > 5): "))
        if n > 5:
            break
        print("Vui lòng nhập số lớn hơn 5.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

shapes = []
for i in range(n):
    while True:
        shape_type = input(f"Nhập loại hình vẽ thứ {i + 1} (Rectangle, Circle, Triangle, Square): ").strip()
        if shape_type == "Rectangle":
            w = float(input("Nhập chiều rộng: "))
            h = float(input("Nhập chiều cao: "))
            shapes.append(Rectangle(w, h))
            break
        elif shape_type == "Circle":
            r = float(input("Nhập bán kính: "))
            shapes.append(Circle(r))
            break
        elif shape_type == "Triangle":
            a = float(input("Nhập cạnh a: "))
            b = float(input("Nhập cạnh b: "))
            c = float(input("Nhập cạnh c: "))
            if a + b > c and a + c > b and b + c > a:
                shapes.append(Triangle(a, b, c))
                break
            else:
                print("Ba cạnh không hợp lệ, vui lòng nhập lại.")
        elif shape_type == "Square":
            side = float(input("Nhập cạnh: "))
            shapes.append(Square(side))
            break
        else:
            print("Loại hình không hợp lệ, vui lòng nhập lại.")

shape_counts = defaultdict(int)
shape_max_areas = defaultdict(lambda: None)
max_area = 0
max_shape = None

for shape in shapes:
    shape_type = shape.__class__.__name__
    shape_counts[shape_type] += 1
    area = shape.getArea()
    print(f"{shape_type}: Area = {area:.2f}")

    if area > max_area:
        max_area = area
        max_shape = shape

    if shape_max_areas[shape_type] is None or area > shape_max_areas[shape_type].getArea():
        shape_max_areas[shape_type] = shape

print("\nSố lượng mỗi loại hình vẽ:")
for shape_type, count in shape_counts.items():
    print(f"{shape_type}: {count}")

print(f"\nHình vẽ có diện tích lớn nhất: {max_shape.__class__.__name__} với diện tích {max_area:.2f}")

print("\nHình vẽ có diện tích lớn nhất của mỗi loại:")
for shape_type, shape in shape_max_areas.items():
    print(f"{shape_type}: Area = {shape.getArea():.2f}")