tuple1 = ()
tuple12 = 1, 2, 3, 4, 5, 6
tuple13 = "How", "are", "you"
tuple14 = 1, "Two", 3.0
tuple15 = 3.14,
tuple21 = tuple()
tuple22 = tuple("Hello")
tuple23 = tuple([s for s in "Hello"])    # A tuple from a list
# tuple12[0] = 0    # Error. Element cannot be changed
vowels = ("a", "e", "i", "o", "u")
print(vowels)
print("Total number of elements in vowels :",len(vowels))
print()
i = vowels.count("e")
print("Number of e in vowels : ",i)
if (i > 0):
    print("e is first found in Index : ",vowels.index("e"))
print()    
j = vowels.count("k")
print("Number of k in vowels : ",j)
if ("k" in vowels):
    print("k is first found in Index : ",vowels.index("k"))
print()    
text1 = "tuple is a built-in immutable sequence"
print("For the text : \"" + text1 + "\"")
for c in vowels:
    print("Number of ",c," in text1 is : ",text1.count(c))
print()
list1 = ["car", "ship", "bus", "car", "train"]
print("Enumerate result for list1",list1,"is :")
for t in enumerate(list1):
    print(t[0],"=>",t[1], sep="", end="  ")     
