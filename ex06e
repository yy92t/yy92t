def showindex(s):
    print("s1            : ", end=" ")
    for c in s:
        print(f"{c:>3}", end=" ")
    print()
    print("Index number  : ", end=" ")
    for i in range(0,len(s)):
        print(f"{i:>3}", end=" ")   
    print()
    print("Negative Index: ", end=" ")
    for n in range(-len(s),0):
        print(f"{n:>3}", end=" ")   
    print()
s1 = "Apple Pineapple"
showindex(s1)
sub1 = "apple"
sub2 = "ine"
sub3 = "Apple"
sub4 = "ine"
sub5 = "ppl"
print()
print(f"s1.count('{sub1}') : ",s1.count(sub1))
print(f"s1.lower().count('{sub1}') : ",s1.lower().count(sub1))
print(f"s1.lower().count('{sub1}',1,-1) : ",s1.lower().count(sub1,1,-1))
print()
print(f"s1.endswith('{sub1}') : ",s1.endswith(sub1))
print(f"s1.endswith('{sub2}',0,-5) : ",s1.endswith(sub2,0,-5))
print(f"s1.endswith('{sub2}',8,-5) : ",s1.endswith(sub2,8,-5))
print()
print(f"s1.startswith('{sub3}') : ",s1.startswith(sub1))
print(f"s1.startswith('{sub2}',7) : ",s1.startswith(sub2,7))
print(f"s1.startswith('{sub2}',8) : ",s1.startswith(sub2,8))
print()
print(f"s1.find('{sub4}') : ",s1.find(sub4))
print(f"s1.find('{sub4}',6) : ",s1.find(sub4,6))
print(f"s1.find('{sub4}',12) : ",s1.find(sub4,12))
print()
print(f"s1.rfind('{sub4}') : ",s1.rfind(sub4))
print(f"s1.rfind('{sub4}',0,6) : ",s1.rfind(sub4,0,6))
print(f"s1.rfind('{sub4}',5,11) : ",s1.rfind(sub4,5,11))
print()
print(f"'{sub1}' in s1 : ",sub1 in s1)
print(f"'{sub1}' in s1[0:-1] : ",sub1 in s1[0:-1])
print(f"'{sub1}' in s1[0:-1].lower() : ",sub1 in s1[0:-1].lower())
print()
print("** The followings may cause error: **")
print(f"s1.index('{sub5}') : ",s1.index(sub5))
print(f"s1.index('{sub5}',6) : ",s1.index(sub5,6))
print()
print(f"s1.rindex('{sub5}')",s1.rindex(sub5))
print(f"s1.rindex('{sub5}',0,6) : ",s1.rindex(sub5,0,6))
############ Additional Examples for finding all occurence ##################
# method 1 uses for, count() and index()
# no error will occur since you find the number of occurence first.
print()
print("All Indexes of " + sub5 + " in " + s1 + " (method 1):", end=" ")
found = -1
for _ in range(s1.count(sub5)):
    found = s1.index(sub5, found + 1)
    print(found, end=" ")
# method 2 uses while, find() and :=
# find() is needed to prevent error since you do not know the number of occurence
print()
print("All Indexes of " + sub5 + " in " + s1 + " (method 2):", end=" ")
found = -1
while (found := s1.find(sub5, found + 1)) != -1:
    print(found, end=" ")
