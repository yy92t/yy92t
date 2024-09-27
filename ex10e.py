import pkg1.mod1

import pkg2

from pkg3 import *

import pkg4

import sys
sys.path.insert(0,"zpkg5.zip")
import pkg5

print()
print("Program starts")
pkg1.mod1.fn()
pkg2.mod1.fn()
mod1.fn()
pkg4.mod1.fn()
pkg5.mod1.fn()
print("Program ends")
print()

print("###################")
print()
import pkg6.mod1
import pkg6.sub1.sub2.sub3.mod2
