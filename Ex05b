def show(inputlist):
    count = 0
    for e in inputlist:
        print(f"{count}=>{e} ", end="")
        count += 1
    else:
        if count == 0:
            print("List is empty", end="")
    print(end="\n\n")
list2 = ["Apple", "Orange"]
print("After creating list2:")
show(list2)
list2[0] = "Banana"
print("After list2[0] = \"Banana\":")
show(list2)
list2.append("Mango")
print("After list2.append(\"Mango\"):")
show(list2)
list2.insert(1,"Coconut")
print("After list2.insert(1,\"Coconut\"):")
show(list2)
r1 = list2.remove("Orange")
print("After list2.remove(\"Orange\"):")
print("Object returned by remove():",r1)
show(list2)
r2 = list2.pop(0)
print("After list2.pop(0):")
print("Object returned by pop():",r2)
show(list2)
list3 = ["Pineapple", "Strawberry"]
list2.extend(list3)
print("After list2.extend(list3):")
show(list2)
list2.clear()
print("After list2.clear():")        
print(list2)
show(list2)
str9 = "How are you"
list9a = []
list9b = []
list9c = []
list9a.extend(str9)
list9b += str9
# list9c = list9c + str9   # + only supports two List objects
print(list9a)
print(list9b)
