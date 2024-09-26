 i = input("Enter a number of single digit : ")

    str1 = "even" if int(i) % 2 ==0 else "odd"
    print(f"The number entered is {str1}")

    match i:
        case "0"|"7":
            print("It can be used to represent Sunday")
        case "1":
            print("It can be used to represent Monday")
        case "2":
            print("It can be used to represent Tuesday")
        case "3":
            print("It can be used to represent Wednesday")
        case "4":
            print("It can be used to represent Thursday")
        case "5":
            print("It can be used to represent Friday")
        case "6":
            print("It can be used to represent Saturday")
        case _:
            print("Exiting ...")
            break
    print()                 

print("Program ends")
