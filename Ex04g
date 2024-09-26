def fn():
    # print(a)  # Error. use a before making it global
    # b += 1    # Error. read b before assignment to b
    # c = 33    # OK. but all c within the function becomes local
    global a;
    a = 11
    print(f"a in fn() = {a}")
    b = 22
    print(f"b in fn() = {b}")
    print(f"c in fn() = {c}")

a = 1
b = 2
c = 3
fn()
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
