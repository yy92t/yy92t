def fn(a, b, c=33, *x, d=44, e, f, **y):
    print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}")
    print(f"x is storing {x}")
    print(f"y is storing {y}")

fn(1,2,3,4,5,6,7,i=21,jj=22,d=11,e=12,f=13,kkk=23)
print()
fn(1,2,3,4,e=11,f=12,abc=4)
print()

###### Remarks: Examples for using "/" ############

def fn10(p1, p2, /, pk1, pk2, *, k1, k2):
    pass

def fn11(p1, p2, /, pk1, pk2=4, *, k1, k2):
    pass

def fn12(p1, p2, /, pk1=3, pk2=4, *, k1, k2):
    pass

def fn13(p1, p2=2, /, pk1=3, pk2=4, *, k1, k2):
    pass

def fn14(p1=1, p2=2, /, pk1=3, pk2=4, *, k1, k2):
    pass

def fn20(p1, p2, /, pk1, pk2=4, *args, k1=11, k2=12):
    print(f"p1={p1}, p2={p2}, pk1={pk1}, pk2={pk2}, k1={k1}, k2={k2}")
    print(f"args stores {args}")
    print()
fn20(1,2,3,4,5,6,k1=11,k2=12)
fn20(1,2,3,5,6,k1=11,k2=12)
# fn20(1,2,4,5,6,k1=11,k2=12,pk1=21)  # Error. pk1 duplicated
