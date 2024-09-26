# Error fixed by adding default value in Sub2 __init__ for var11 as mentioned in a remark
class Super1:
    def __init__(self, var11="supervalue11"):
        self.var11 = var11
        self.var12 = "supervalue12"
        self.var13 = "supervalue13"
class Sub2(Super1):
    def __init__(self, var11="supervalue11"):   # default value added
        super().__init__(var11)
        self.var21 = "subvalue21"
        self.var22 = "subvalue22"
obj1 = Super1("myvalue11")
obj21 = Sub2("myvalue11")
for attr in dir(obj21):
    if not (attr.startswith("__") and attr.startswith("__")):
        print(attr,"=",getattr(obj21,attr), end=" ")
print()
print()
obj22 = Sub2()
for attr in dir(obj22):
    if not (attr.startswith("__") and attr.startswith("__")):
        print(attr,"=",getattr(obj22,attr), end=" ")
