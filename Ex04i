def outer_fn():
    b = 11
    d = 11
    e = 11
    f = 11

    def inner_fn():
        c = 111
        d = 111
        nonlocal e
        e = 111
        global f
        f = 111
        print(f"a in inner : {a}")
        print(f"b in inner : {b}")
        print(f"c in inner : {c}")
        print(f"d in inner : {d}")
        print(f"e in inner : {e}")
        print(f"f in inner : {f}")

    inner_fn()
    print(f"a in outer : {a}")
    print(f"b in outer : {b}")
    # print(f"c in outer : {c}")   # Error. not defined.
    print(f"d in outer : {d}")
    print(f"e in outer : {e}")
    print(f"f in outer : {f}")

a = 1
b = 1
f = 1
outer_fn()
print(f"a : {a}")
print(f"b : {b}")
print(f"f : {f}")
