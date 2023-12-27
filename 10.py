# 10 . Explore the OOPS concepts.
# Create a Person class with attributes name and age. Implement a method that prints a greeting
# with the person's name and age.
# Create a Shape class with a method area. Implement subclasses Circle and Rectangle with
# their own implementations of the area method.
# Person class
# import math
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
print(person1.name) 
person2.say_hello()

class Shape:
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width  
        self.height = height 
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  

    def area(self):
        return 3.14 * self.radius ** 2  
    
shapes = [Rectangle(4, 5), Circle(7)]  
for shape in shapes:
    print(shape.area()) 