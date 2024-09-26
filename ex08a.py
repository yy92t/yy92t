def fn(i, j):
    return i/j

numbers = [1, 2, 3]
try:
    a = 1
    #b = 4/0
    #c = numbers[3]
    #d = x
    #fn(1,0)
except ZeroDivisionError as ex:
    print("ZeroDivisionError handled :",ex)
except IndexError as ex:
    print("IndexError handled :",ex)
except BaseException as ex:
    print(type(ex).__name__,"handled:",ex)
else:
    print("else : No exception occured")
finally:
    print("finally : Clean up is performing")
print("Program ends")
