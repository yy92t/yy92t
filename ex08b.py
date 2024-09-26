class CarCrash(Exception):
    pass

class Car:
    def __init__(self, license_no = "UnReg"):
        self.license_no = license_no;
        self.speed = 0
    def accelerate(self):
        self.speed += 20
        if self.speed > 100:
            raise CarCrash(self.license_no, self.speed)
    def brake(self):
        self.speed -= 10

print("Traffic Simulation")
car1 = Car("AA1234")
try:
    for i in range(10):
        car1.accelerate()
except CarCrash as e:
    print("Report accident about car",e.args[0])
print()
    
print("Car Testing")
car2 = Car()
try:
    for i in range(10):
        car2.accelerate()
except CarCrash as e:
    print("Car crashed at speed",e.args[1])
print()
