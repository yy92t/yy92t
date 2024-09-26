class Vehicle:
    def __init__(self):
        self._speed = 0
class Car(Vehicle):
    __designer = "Peter"
    design_award = 0
    def __init__(self, color="White", license_no="Unreg"):
        super().__init__()
        self.color = color
        self.license_no = license_no
    def __repr__(self):
        return self.license_no
    def show_designer(self):
        print("Designer of Car is ",self.__designer)
    def accelerate(self):
        self._speed += 10
    def brake(self):
        self._speed -= 5
    def show_speed(self):
        return self._speed
        
class RacingCar(Car):
    __designer = "John"
    racing_won = 0
    def __init__(self, spoiler_color="Red", color="Red", license_no="Unreg"):
        super().__init__(color, license_no)
        self.spoiler_color = spoiler_color
    def show_designer(self):
        print("Designer of RacingCar is ",self.__designer)
    def accelerate(self):
        if self._speed >= 30:
            self._turbo_accelerate()
        else:
            super().accelerate()
    def _turbo_accelerate(self):
        self._speed += 15
print("## class Car info ...")
print(Car.__dict__)
print()
print(dir(Car))
print()
print(Car.__base__)
print()
print(Car.__mro__)
print()
print("## class RacingCar info ...")
print(RacingCar.__dict__)
print()
print(dir(RacingCar))
print()
print(RacingCar.__base__)
print()
print(RacingCar.__mro__)
print()
Car.design_award += 1
RacingCar.__base__.design_award += 1
print("Awards for Car :", Car.design_award)
print("Awards for RacingCar :", RacingCar.design_award)
RacingCar.racing_won += 10
print("Racing Won for RacingCar :", RacingCar.racing_won)
print()
car1 = Car("Black", "CC1111")
rcar2 = RacingCar(license_no="RR2222")
car1.show_designer()
rcar2.show_designer()
print("rcar2._Car__designer :",rcar2._Car__designer)
print()
print("## Car object info :")
print(car1.__dict__)
print()
print(dir(car1))
print()
print("## RacingCar object info :")
print(rcar2.__dict__)
print()
print(dir(rcar2))
print()
print("############")
print()
print(car1,"IS-A Vehicle :",isinstance(car1, Vehicle))
print(car1,"IS-A Car :",isinstance(car1, Car))
print(car1,"IS-A RacingCar :",isinstance(car1, RacingCar))
print()
print(rcar2,"IS-A Vehicle :",isinstance(rcar2, Vehicle))
print(rcar2,"IS-A Car :",isinstance(rcar2, Car))
print(rcar2,"IS-A RacingCar :",isinstance(rcar2, RacingCar))
print()
print(car1,"speed before accelerating :",car1.show_speed())
print(rcar2,"speed before accelerating :",rcar2.show_speed())      
print()
car1.accelerate()
car1.accelerate()
car1.accelerate()
rcar2.accelerate()
rcar2.accelerate()
rcar2.accelerate()                  
print(car1,"speed after accelerating 3 times :",car1.show_speed())
print(rcar2,"speed after accelerating 3 times :",rcar2.show_speed())      
print()
car1.accelerate()
rcar2.accelerate()                  
print(car1,"speed after accelerating one more time :",car1.show_speed())
print(rcar2,"speed after accelerating one more time :",rcar2.show_speed())
