mylist1 = [1, "aaa", False]
x, y, z = mylist1
print(x,y,z)
print()
mylist2 = [1, "aaa", False, 3.0]
x, *y, z = mylist2
print(x)
print(y)
print(z)
print()
fn = lambda x : x ** 2
print(fn(3))
print()
mylist3 = [1, 2, 3, 4, 5]
flist1 = list(filter(lambda x : x % 2 == 0, mylist3))
print(flist1)
for i in filter(lambda x : x % 2 == 0, mylist3):
    print(i, end=" ")
print()
flist2 = [ x for x in filter(lambda x : x % 2 == 0, mylist3) ]
print(flist2)
print()
mlist1 = list(map(lambda x : x ** 2, mylist3))
print(mlist1)
for i in map(lambda x : x ** 2, mylist3):
    print(i, end=" ")
print()
mlist2 = [ x for x in map(lambda x : x ** 2, mylist3) ]
print(mlist2)
