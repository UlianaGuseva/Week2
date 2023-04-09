from math import pi
import turtle
class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius
        self.diametr = radius * 2
    @classmethod
    def from_diametr(cls, diametr: float):
        new_circle = cls(diametr /2)
        return new_circle

    @property
    def area(self):
        area = pi * self.radius **2
        return area

    def __add__(self, other):
        radius_comb = self.radius + other.radius
        new_circle = Circle(radius_comb)
        return new_circle

    def __lt__(self, other):
        return self.radius < other.radius
    
    def __gt__(self, other):
           return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __repr__(self):
        return f'(rad: {self.radius}, diam: {self.diametr})'


c1 = Circle(2.0)
c2 = Circle.from_diametr(6.0)

print('radius', c1.radius)
print('diametr', c1.diametr)

print('circle area ', c1.area)
print('circle area ', c2.area)

print('radius', c2.radius)
print('diametr', c2.diametr)

c3 = c1+c2
print(c3.radius)


print(c3>c1)

circles = [c3,c2,c1]
circles.sort()

print(circles[0].radius)
print(circles[-1].radius)

print(circles)

# turtle.circle(c3.radius ** 3)
t = turtle.Turtle()

t.circle(c3.radius ** 3)
turtle.exitonclick()