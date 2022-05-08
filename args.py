def fun(*args):
    print(type(args))
    sum = 0
    for x in args:
        sum += x
    return sum

print(fun(1, 2, 3))




