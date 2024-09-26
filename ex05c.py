list1 = [1, 3, 5, 6, 4, 2]
print("len(list1) :")
print(len(list1))
print()
print("Iterate using len() :")
for n in range(0,len(list1)):
    print(n,"=>",list1[n],sep="",end=" ")
print("\n")
list1s = sorted(list1)
print("After sorted(), original list : ",list1)
print("After sorted(), new sorted list : ",list1s)
print()
print("list(enumerate(list1)) :")
print(list(enumerate(list1)))
print()
print("Sum of list1 : ",sum(list1))
print("Max of list1 : ",max(list1))
print("Min of list1 : ",min(list1))
print()
list5 = [4>3, 6>3, 1, " "]
print("list5 all True : ",all(list5))
list6 = [4<3, 6>3, 0, "", False]
print("list6 any True : ",any(list6))
empty_list = []
print("all() for Empty List : ",all(empty_list))
print("any() for Empty List : ",any(empty_list))
