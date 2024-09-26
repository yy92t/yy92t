def fn1():
    i = 1
    print("Statement before 1st yeild")
    yield i
    i += 1
    print("Statement before 2nd yeild")
    yield i
    i += 1
    print("Statement before 3rd yeild")
    yield i
    print("Statement before 4th yeild")
    
i = fn1()
print(f"next(i) returns {next(i)}")
print(f"next(i) returns {next(i)}")
print(f"next(i) returns {next(i)}")
# print(f"next(i) returns {next(i)}")  # StopIteration error.
print()

def squares(end):
    if end < 2:
        return
    for i in range(1,end):
        yield i ** 2

i = squares(4)
x = next(i, None)
while x != None:
    print(x)
    x = next(i, None)
else:
    print("No more values from i")
print()

i = squares(0)
print(next(i, None))
print()

for i in squares(4):
    print(i)
print()

for i in squares(0):
    print(i)
print()
