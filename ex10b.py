from module1 import *

print(__doc__)				# print docstring in main program
print()

print(Car.__doc__)
car1 = Car()
print(car1)
car1.accelerate()
print(car1.speed)
print()

a = 9
# print(_square(a))  # Error. Attribute starting with _ not imported
print()

print(a)					# print a in main program
print()

show_a()
print()

a = 9
print("After a = 9 ...")
show_a()
print()

print(b) 

print("################")
print()

from module2 import *    # module2 is imported after module1

print(b)               # b contains the value assigned in module2
print()

show_a()               # show_a() defined in module2 is called
print()

print(show_a.__module__)  # check the module show_a is from
print()

print(b)               # b contains the value assigned in module2
print()

b = 99
print("After b = 99 ....")
show_a()               # show_a() defined in module2 is called
print()

print(b)  
