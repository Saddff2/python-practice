from math import pi



class Circle:
    def __init__(self, radius:int, color:str, x_pos:int, y_pos:int, full:bool):
        self.rad = radius
        self.col = color
        self.position = (x_pos, y_pos)
        self.full = full

    def perimeter(self):
        return 2*self.rad * pi

    def area(self):
        return pi * self.rad ** 2

    def tamir_area(self, number:int):
        return self.area()*number

    def change_y_position(self, number:int):
        self.position = (self.position[0], self.position[1]+number)
        return self.position
    def change_x_position(self, number:int):
        self.position = (self.position[0]+number, self.position[1])
        return self.position

    def __str__(self):
        return f"this is a circle with radius {self.rad} and color {self.col} and position {self.position}"


nadav = Circle(radius=1/2, color='red', x_pos=3, y_pos=4, full=True)
rotem = Circle(radius=1/3, color='d',x_pos=2, y_pos=5, full=False)
yakir = Circle(radius=1/5, color='f',x_pos=4, y_pos=3, full=False)
daniel = Circle(radius=1/8, color='g',x_pos=6, y_pos=1, full=False)
almog = Circle(radius=1/7, color='green',x_pos=8, y_pos=4, full=False)

my_circles = [nadav, rotem, yakir, daniel, almog]

for x in my_circles:
    print(x.change_x_position(5), x.change_y_position(2))

print(nadav)

class Shape:
    def __init__(self, positions:tuple, full:bool, color:str, type:str):
        self.positions = positions
        self.full = full
        self.color = color
        
class Circle1(Shape):
    def __init__(self, type:str, positions:tuple, full:bool, color:str):
        super().__init__(positions, )
        