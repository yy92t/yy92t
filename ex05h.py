dict1 = {}                                              
dict2 = {"Vincent":10000, "Peter":30000, "Mary":20000}
dict3 = {"a":1, 3:"string1", (1,2,3):1, False:1}
dict4 = {x: x**2 for x in (2,3,4)}
dict11 = dict()
dict12 = dict(Vincent=10000, Peter=30000, Mary=20000)
list1 = [("Vincent", 10000), ("Peter", 30000), ("Mary", 20000)]
dict13 = dict(list1)              
keylist = ["Vincent", "Peter", "Mary"]
valuelist = [10000, 30000, 20000]
dict14 = dict(zip(keylist,valuelist))
keylist = ["Vincent", "Peter", "Mary"]
dict15 = dict.fromkeys(keylist, 0)
print(dict1)   # Change this to print any dict created above
print()       
print("dict2 :",dict2)
dict2["Peter"]=33333
print("After dict2[\"Peter\"]=33333:",dict2)
dict2["John"]=44444
print("After dict2[\"John\"]=44444:",dict2)
print()
print()
dict21 = {x: x+10 for x in range(-1,3)}
print("dict21:",dict21)
print("len(dict21):",len(dict21))
print("list(enumerate(dict21)):",list(enumerate(dict21)))
print("sorted(dict21):",sorted(dict21))
print("sum(dict21):",sum(dict21))
print("max(dict21):",max(dict21))
print("min(dict21):",min(dict21))
print()
print()
dict31 = {"Vincent":10000, "Peter":30000, "Mary":20000, "John":10000}
print("dict31:",dict31)
print()
print("dict31[\"Vincent\"]:",dict31["Vincent"])
print("dict31.get(\"Vincent\"):",dict31.get("Vincent"))
print()
print("dict31[\"Vincent\"]:",dict31["Vincent"])        
# print(dict31["Charles"])      # Error. Key not exist
print("dict31.get(\"Charles\"):",dict31.get("Charles"))
print()
print("dict31.pop(\"Peter\"):",dict31.pop("Peter"))
# print(dict31.pop("Charles"))  # Error. Key not exist
print("dict31.pop(\"Charles\",\"not found\"):",
      dict31.pop("Charles","not found"))
print("After pop():",dict31)
print()
print("dict31.setdefault(\"Mary\",22222):",dict31.setdefault("Mary",22222))
print("dict31.setdefault(\"Peter\",33333):",dict31.setdefault("Peter",33333))
print("After setdefaul():",dict31)
print()
print("dict31.popitem():",dict31.popitem())
print("After popitem:",dict31)
print()
dict32 = {"Ann":4000, "Paul":5000}
dict31.update(dict32)
print("After update():",dict31)
