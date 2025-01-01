class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        x_point = self.x + other.x
        y_point = self.y + other.y
        
        return Point(x_point, y_point)
    
    def __sub__(self, other):
        x_point = self.x - other.x
        y_point = self.y - other.y
        
        return Point(x_point, y_point)

p1 = Point(1, 2)
print(p1)

p2 = Point(3, 4)
print(p2)

p3 = Point(5, 6)
print(p3)

print(p1 + p2 + p3)
print(p2 - p1)
