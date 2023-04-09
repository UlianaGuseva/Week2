class Car:
    def __init__(self, speed):
        self.speed = speed
    def __gt__(self, other_car):
        return self.speed > other_car.speed 
    def __lt__(self, other_car):
        return self.speed > other_car.speed

car1 = Car(200)
car2 = Car(300)

print(car1 > car2) 