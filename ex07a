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
car1.accelerate()
print("car1 speed after accelerate() is :",car1.speed)
car1.engine_running = True
car1.accelerate()
print("car1 speed after engine On and accelerate() is :",car1.speed)
print("car1 speed in mph is :",car1.speed_in_mph())      
print()
      
car2 = Car("Blue", "B2222")
car2.engine_running = True
car2.multi_accelerate(2)
car2.brake()
print("car2 speed is :",car2.speed)
print()
def object_info(c):
    print("The vehicle (", c.license_no, ") of type", type(c).__name__,
          "in", c.color, "has a speed of", c.speed)
object_info(car1)
object_info(car2)
print()
class Bus:
    def __init__(self, color = "Red", license_no = "UnReg"):
        self.license_no = license_no
        self.color = color
        self.speed = 0
    def accelerate(self):
        self.speed += 6
    def brake(self):
        self.speed = self.speed - 5
list1 = [car1, car2, Bus(license_no="U3333")]
for v in list1:
    v.accelerate()
    v.brake()
    object_info(v)
