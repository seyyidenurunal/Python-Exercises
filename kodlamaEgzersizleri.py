a = int(input("A"))
b = int(input("B"))
c = int(input("C"))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print("Tanımsız")