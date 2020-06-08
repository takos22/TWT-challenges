def erange(*args):
    if len(args) == 0:
        raise TypeError("erange expected 1 arguments, got 0")
    if len(args) > 3:
        raise TypeError(f"erange expected 3 arguments, got {len(args)}")
    try:
        args = [int(i) for i in args]
    except ValueError:
        raise TypeError("all arguments must be of type 'int'")

    start = 0
    step = 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) >= 2:
        start = args[0]
        stop = args[1]
    if len(args) == 3:
        step = args[2]

    if step == 0:
        raise ValueError("step arg must not be 0")

    numbers = []
    i = start
    while (i < stop) if step > 0 else (i > stop):
        numbers.append(i)
        i += step
    return numbers


def numerate(elements, start=0):
    enumerated = []
    for i in erange(start, len(elements)):
        enumerated.append((i, elements[i]))
    return enumerated


print(list(range(10)))
print(erange(10))
print(list(range(1,11)))
print(erange(1,11))
print(list(range(0,30,5)))
print(erange(0,30,5))

print(list(enumerate("test 10")))
print(numerate("test 10"))
print(list(enumerate(["test",10])))
print(numerate(["test",10]))
print(list(enumerate(("test",10))))
print(numerate(("test",10)))