dict1 = {"a":1, "b":2, "c":3}
print("dict1:",dict1)
k = dict1.keys()
print("Using k i.e. dict1.keys():")
print(k)
print(type(k))
print()
dict1["d"] = 4
print("After change in dict1:",k)
dict2 = {"a":1, "b":2, "c":3}
print("dict2:",dict2)
v = dict2.values()
print("Using v i.e. dict2.values():")
print(v)
print(type(v))
print()
dict2["d"] = 4
print("After change in dict2:",v)
print("Checking 3 in v:",3 in v)
print("Checking 5 in v:",5 in v)
print("max(v):",max(v))
print("sum(v):",sum(v))
print()
dict3 = {"a":1, "b":2, "c":3}
print("dict3:",dict3)
i = dict3.items()
print("Using i i.e. dict3.items():")
print(i)
print(type(i))
dict3["d"] = 4
print("After change in dict3:",i)
dict4 = {k:v+10 for (k,v) in i if v > 2}
print("dict4 created from i:",dict4)
targetvalue = 3
list1 = [k for (k,v) in i if v == targetvalue]
print("Keys having targetvalue in i: ",list1) 
######### Additional Reference ###############
print()
dict9 = {"a":1, "b":2, "c":3, "cc":3, "ccc":3}
print("dict9:",dict9)
targetvalue = 3
# The following uses dict9 instead of dict3 in our notes
list2 = []
for k,v in dict9.items():
    if v == targetvalue:
        list2.append(k)
print("Find ALL keys with targetvalue using for iteration:",list2)
for k,v in dict9.items():
    if v == targetvalue:
        result1 = k
        break
print("Find any key with targetvalue using for iteration:",result1)
keylist = list(dict9.keys())
valuelist = list(dict9.values())
tindex = valuelist.index(3)
result2 = keylist[tindex]
print("Find any key with targetvalue using key and value Lists:",result2)
