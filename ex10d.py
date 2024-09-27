import module3

print("Program starts")
module3.fn()
module3.x = 4
print()

print("Import module again ...")
from module3 import fn
import module3
module3.fn()
print()

print("Reload module ...")
import importlib
importlib.reload(module3)
module3.fn()
print()

print("Program ends")
