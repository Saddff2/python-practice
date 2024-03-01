class Shape:
    my_var = 10
    def __init__(self, color, x_position, y_position, ):
        self.color = color
        self.position = (x_position, y_position)
        
    def my_function(self, z ):
        return self.my_var*z
    
    def change_color(self, new_color):
        self.color = new_color
        return self.color
        

class Circle(Shape):
    
    def __init__ (self, radius, color, x_position, y_position):
        super().__init__(color, x_position, y_position)
        self.radius = radius
        
        
my_circle = Circle(radius=5, color='red', x_position=5, y_position=8)

print(my_circle.change_color('green'))


class Triangle(Shape):
    
    def __init__ (self, color, x_position, y_position, shape):
        super().__init__(color, x_position, y_position)
        self.shape = shape
        

my_triangle = Triangle(color='yellow', x_position=10, y_position=25, shape='even')
before = my_triangle.color



print(my_triangle.change_color('triangled'))
_name