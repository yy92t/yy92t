class Super1:
    cvar = 1
    def __init__(self):
        self.ivar = 1
        self.__method()
    def __method(self):
        print("Running Super1 method...")
    method = __method          # Added for External Access
class Sub2(Super1): 
    cvar = 2
    def __init__(self):
        super().__init__()
        self.ivar = 2
        self.__method()
    def __method(self):
        print("Running Sub2 method...")
    method = __method          # Added for External Access
def show_custom(t): 
    customvar = {var:getattr(t,var) for var in dir(t) if "var" in var}
    print(customvar)
    custommethod = [m for m in dir(t) if "method" in m]
    print(custommethod)
    print() 
    
obj1 = Super1()
print()
show_custom(Super1)
show_custom(obj1)
obj2 = Sub2()
print()
show_custom(Sub2)
show_custom(obj2)
