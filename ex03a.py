x = input('Enter a alphanumeric character: ')

if x >= "a":
    print(x + " is a lowercase character")
elif x >= "A":
    print(x + " is a uppercase character")
else:
    print(x + " is a numeric character")

if x >= "A":
    if x >= "a":
        print(x + " is a lowercase character")
    else:
        print(x + " is a uppercase character")
else:   
    print(x + " is a numeric character")

print("Program ends")
