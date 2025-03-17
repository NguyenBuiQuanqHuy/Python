import math
from collections import defaultdict


class Shape:
    def getArea(self):
        raise NotImplementedError()


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


def parse_shape(input_str):
    name, values = input_str.split("[")
    values = list(map(int, values.strip("]").split(",")))
    if name == "Rectangle" and len(values) == 2:
        return Rectangle(*values)
    elif name == "Circle" and len(values) == 1:
        return Circle(*values)
    elif name == "Triangle" and len(values) == 3:
        a, b, c = sorted(values)
        if a + b > c:
            return Triangle(a, b, c)
        else:
            return Triangle(a, b, a + b - 1)
    elif name == "Square" and len(values) == 1:
        return Square(*values)
    return None


shape_inputs = [
    "Rectangle[5,10]", "Circle[7]", "Triangle[3,4,5]", "Square[6]", "Rectangle[8,3]", "Circle[4]", "Triangle[5,5,6]"
]

shapes = [parse_shape(inp) for inp in shape_inputs if parse_shape(inp) is not None]

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