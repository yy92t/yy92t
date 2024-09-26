class A:
    def __init__(self):
        super().__init__()
        self.avar = 1
    def method1(self): print("Running A method1()")
class B1(A):
    def __init__(self):
        super().__init__()
        self.b1var = 2
    def method1(self): print("Running B1 method1()")
    
class B2(A):
    def __init__(self):
        super().__init__()
        self.b2var = 3
    def method1(self): print("Running B2 method1()")
class C(B1, B2):
    def __init__(self):
        super().__init__()
        self.cvar = 4
    def method1(self): print("Running C method1()")
obj1 = C()
obj1.method1()
print(obj1.__dict__)
print()
print(C.__mro__)
print()
print(C.__bases__)
print(C.__base__)
print()
class D1(B1, A): pass    # OK
# class D2(A, B1): pass    # Error
print("###########")
print()
class Car:
    def show_speed(self):
        print("Showing ground speed …")
class Airplane:
    def show_speed(self):
        print("Showing air speed …")
    
class FlyingCar(Car, Airplane):
    def show_speed(self):
        Car.show_speed(self)
        Airplane.show_speed(self)
    def show_ground_speed(self):
        Car.show_speed(self)
    def show_air_speed(self):
        Airplane.show_speed(self)
fcar1 = FlyingCar()
fcar1.show_speed()
print()
fcar1.show_ground_speed()
print()
fcar1.show_air_speed() 
