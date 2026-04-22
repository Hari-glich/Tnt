class shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        return 0
class circle(shape):
    def __init__(self,radius):
        super().__init__("Circle")
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2         
c1=circle(10)
print(f"The area of the {c1.name} is: {c1.area()}")

def area(shape):
    return shape.area() 