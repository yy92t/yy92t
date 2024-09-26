print("Without Break")
sum = 0
number = 0
while sum <= 1000:
    sum += number
    number += 1
else:
    print("sum is now larger than 1000")
print(f"Sum is : {sum}")
print()    

print("With Break")
sum = 0
for i in range(0,1000):
    sum += i
    if sum > 1000:
        break
else:
    print("All numbers are iterated")
print(f"Sum of all numbers upto {i} is : {sum}")
print()    

# Alternative 1 (without break)
name = ""
while name != "x":
    name = input("1) Enter a name (enter x to exit) : ")
    if name != "x":
        print(f"Hello! {name}.")
else:
    print("Alternative 1 ends")
print()    

# Alternative 2 (with break)
while True:
    name = input("2) Enter a name (enter x to exit) : ")
    if name == "x":
        break
    print(f"Hello! {name}.")
else:
    print("Alternative 2 ends")
print()    

# Alternative 3 (with assignment expression)
while "x" != (name := input("3) Enter a name (enter x to exit) : ")):
    print(f"Hello! {name}.")
else:
    print("Alternative 3 ends")
print()    
