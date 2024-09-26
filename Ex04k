def my_decorator(func):
    def inner_fn(value):
        print("****")
        func(value)
        print("****")
    return inner_fn

@my_decorator
def square(value):
    print(f"The square of {value} is {value**2}")

@my_decorator
def square_root(value):
    print(f"The square root of {value} is {value**(1/2)}")

x = 4
# square = my_decorator(square)
# square_root = my_decorator(square_root)
square(x)
print()
square_root(x)
