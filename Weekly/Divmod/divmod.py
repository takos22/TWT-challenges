def divmod2(a, b):
    try:
        a = int(a)
        b = int(b)
    except:
        return ("Please input integers",)
    x = a//b
    y = a % b
    return x, y, (x, y)


a = input("a = ")
b = input("b = ")
print(*divmod2(a, b), sep="\n")
