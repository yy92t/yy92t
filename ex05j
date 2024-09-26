listinlist = [ [1, 2], ["a", "b", "c"] ]
print("listinlist:",listinlist)
print()
print("Getting each inner List:")
list1 = listinlist[0]
list2 = listinlist[1]
print("1st inner List:",list1)
print("2nd inner List:",list2)
print()
print("Using two sets of Index number:")
list1 = listinlist[0]
e1 = list1[0]
print("listinlist[0] and then [0] on it:",e1)
e2 = listinlist[0][0]
print("listinlist[0][0]:",e2)
print()
print("Using nested for statements:")
for inner in listinlist:
    for e in inner:
        print(e, end=" ")
print(end="\n\n")
print("Using nested for statements by iterating index:")
for outerindex in range(0,len(listinlist)):
    for innerindex in range(0,len(listinlist[outerindex])):
        print(f"[{outerindex}][{innerindex}]=>",
              listinlist[outerindex][innerindex],end=" ")
print(end="\n\n")
print("Creating a Flat List:")
flat_list = [e for ilist in listinlist for e in ilist]
print(flat_list)
