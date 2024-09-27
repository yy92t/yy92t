from module1 import __doc__ as m1doc
from module1 import Car
from module1 import _square
from module1 import show_a
from module1 import a as m1a
from module1 import b

print(m1doc)
print()

print(Car.__doc__)
car1 = Car()
print(car1)
car1.accelerate()
print(car1.speed)
print()

a = 9
print(_square(a))
print()

print(m1a)
print()

show_a()
print()

m1a = 9
print("After m1a = 9 ...")
show_a()
print()

print(b)
