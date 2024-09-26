class Car:
    designer = "Peter"
    design_awards = 0
    def __init__(self, color = "White", license_no = "UnReg"):
        self.license_no = license_no
        self.color = color
        self.engine_running = False
        self.speed = 0
    def accelerate(self):
        if self.engine_running:
            self.speed += 10
    def multi_accelerate(self, times):
        for _ in range(times):
            self.accelerate() 
    def brake(self):
        self.speed = self.speed - 5
        if self.speed < 0:
            self.speed = 0
    def speed_in_mph(self):
        return self.speed * 0.62
print("Class Car info ...")
Car.design_awards += 1
print("Designer is :",Car.designer)
print("Number of awards is :",Car.design_awards)
print()
car1 = Car()
print("car1 speed before accelerate() is :",car1.speed)
class Car:
    designer = "Peter"
    design_award = 0
    def __init__(self, color="White"):
        self.color = color
        self._speed = 0
    def accelerate(self):
        self._speed += 10
    def brake(self):
        self._speed -= 5
    def show_speed(self):
        return self._speed
        
print("Car's __dict__ :")
print(Car.__dict__)
print()
car1 = Car()
print("car1's __dict__ :")
print(car1.__dict__)
print()
print("color in car1 dict :", "color" in car1.__dict__)
print("abc in car1 dict :", "abc" in car1.__dict__)
print("value of car1 color :", car1.__dict__["color"])
print()
print("dir() with Car as argument :")
print(dir(Car))
print()
car1 = Car()
print("dir() with car1 as argument :")
print(dir(car1))
print()
print("hasattr(Car, \"designer\")", hasattr(Car, "designer"))
print("hasattr(car1, \"color\") :", hasattr(car1, "color"))
print("hasattr(car1, \"designer\") :", hasattr(car1, "designer"))
print("getattr(car1, \"designer\") :", getattr(car1, "designer"))
print()
Car.internal_code = "12345"
print("After adding Class attribute internal_code:")
print(vars(Car))
print()
car2 = Car()
car3 = Car()
car2.engine_running = False
del car3.color
print("car1's __dict__ :", vars(car1))
print("car2's __dict__ :", vars(car2))
print("car3's __dict__ :", vars(car3))
print()
car1.accelerate()
car1.brake()
print("car1.show_speed() :", car1.show_speed())
print("car1._speed", car1._speed)
