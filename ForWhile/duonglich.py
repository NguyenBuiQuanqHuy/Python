def fibonanci(a):
    if a<1:
        return None
    f1,f2=1,1
    while f2<=a:
        f1,f2=f2,f1+f2
    return f1
a=int(input("Nhập số a: "))
print(fibonanci(a))