import module1

print(module1.__doc__)
print()

print(module1.Car.__doc__)
car1 = module1.Car()
print(car1)
car1.accelerate()
print(car1.speed)
print()

a = 9
print(module1._square(a))
# print(math.sqrt(a))   # Error module math not imported
print()

print(module1.a)
print()

module1.show_a()
print()

module1.a = 9
print("After module1.a = 9 ...")
module1.show_a()
print()

print(module1.b)
# print(b)                # Error. Must specify "module1."
print()

print("##################")
print()

print(dir(module1))				# find attributes in the module
print()

print("Accessing b:")
print(hasattr(module1, "b"))		# check if an attributes exist in the module
print(getattr(module1, "b"))     # same as  module1.b
print()

print("Accessing _square:")
print(hasattr(module1, "_square"))
fn = getattr(module1, "_square")   # same as  fn = module1._square
print(fn(7))
print()
