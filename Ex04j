def outer_fn1(func):
    def inner_fn():
        func()
    inner_fn()

def hello():
    print("Hello")

x = 1
outer_fn1(hello)

##

def outer_fn2():
    def inner_fn():
        print("Hi")
    return inner_fn

x = outer_fn2()
print(x)
x()
