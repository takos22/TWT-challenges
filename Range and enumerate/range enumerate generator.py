def erange(*args):
    if len(args) == 0:
        raise TypeError("erange expected 1 arguments, got 0")
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

    i = start
    while (i < stop) if step > 0 else (i > stop):
        yield i
        i += step


def numerate(elements, start=0):
    for i in erange(start, len(elements)):
        yield (i, elements[i])


print(list(range(10)))
print(list(erange(10)))
print(list(range(1,11)))
print(list(erange(1,11)))
print(list(range(0,30,5)))
print(list(erange(0,30,5)))

print(list(enumerate("test 10")))
print(list(numerate("test 10")))
print(list(enumerate(["test",10])))
print(list(numerate(["test",10])))
print(list(enumerate(("test",10))))
print(list(numerate(("test",10))))