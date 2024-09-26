class Car:
    designer = "Peter"
    def __init__(self, color="White", license_no="Unreg"):
        self.color = color
        self.license_no = license_no
        self.speed = 0
    def __str__(self):
        return ("Car "+self.license_no+" in "+self.color+
                " with speed "+str(self.speed))
    def __repr__(self):
        return self.license_no+"("+self.color+")"
    def __lt__(self, other):
        return self.license_no < other.license_no
    def show_color(self):
        return self.color
    @classmethod
    def show_award(cls):
        print("Designer is :",cls.designer)
    @staticmethod
    def show_info():
        print("This is a class Car for creating Car objects")
    
        
car1 = Car("Red", "ZZ1111")
car2 = Car("Blue", "YY2222")
car3 = Car(license_no="KK3333")
print("car1 String :", car1)
print("car2 String :", car2)
print("car3 String :", car3)
print()
list1 = [car1, car2, car3]
print("Printing list1 before sort() :", list1)
list1.sort()
print("Printing list1 after sort():", list1)
print()
print("Performing Custom Sorting by color ... ")
list1.sort(key=Car.show_color)
print("Printing list1 after sort() with key:", list1)
print()
Car.show_award()    # Calling Class Method
Car.show_info()     # Calling Static Method
print()
print("__dict__ of Car:")
print(Car.__dict__)    # Class and Static Method can be identified through info in  values
print()
print("dir() with Car")
print(dir(Car))        # Class and Static Method are shown by name only
print()
print("Adding Instance method accelerate() :")
def fn(obj):
    obj.speed += 10
# car1.accelerate()     # Error!! 'Car' object has no attribute 'accelerate'
Car.accelerate = fn     # assign the function object fn() to accelerate of Car
car1.accelerate()   # call accelerate() will call the function object fn()
print(car1.speed)
