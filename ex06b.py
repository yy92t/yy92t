s = "abcdefg"
print("Iterating s   : ", end=" ")
for c in s:
    print(c, end="  ")   # printing each character
print()
print("Index number  : ", end=" ")
for i in range(0,len(s)):
    print(i, end="  ")   
print()
print("Negative Index:", end=" ")
for n in range(-len(s),0):
    print(n, end=" ")   
print()
print("s[0]: ",s[0])
print("s[6]: ",s[6])
print("s[-3]: ",s[-3])
# print(s[7])  # IndexError: string index out of range
print()
print("s[1:4]: ",s[1:4])
print("s[3:]: ",s[3:])
print("s[::2]: ",s[::2])
print("s[-2:1:-1]: ",s[-2:1:-1])
print()
print("len(s): ",len(s))
print("min(s): ",min(s))
print("max(s): ",max(s))
print("List from sorted(s): ",sorted(s))
print("List from list(reversed(s)): ",list(reversed(s)))
print()
print("Using +:")
s1 = "abc"
s2 = "def"
n1 = 123
print(s1 + s2)
print(s1 + str(n1))
# print(s1 + n1)            # TypeError
print()
print("Using *:")
s1 = "abc"
n1 = 2
n2 = 3
n3 = 0
print(s1 * n1)
print(n2 * s1)
print(s1 * n3)          # Create an empty String
# print(s1 * 1.2)       # TypeError
print()
print("Using join():")
print(",".join(["def", "xyz"]))     # using , as separator
print(" ".join(["def", "xyz"]))     # using space as separator
print(",".join("def"))          # using , as separator
s = "xyzabcdefg"
print("".join(sorted(s)))       # no separator
print("".join(reversed(s)))     # no separator
# print("".join("def", "xyz"))              # TypeError
############# Additional Reference ##############
print()
print("Joining elements including non-String:")
list1 = ["aa", "bb", 3, "dd"]
# print(" ".join(list1))          # Type Error
list2 = []
for e in list1:
    list2.append(str(e))
print("Using iterating and str(): " + " ".join(list2))
print("Using join() with map() : " +" ".join(map(str, list1)))
