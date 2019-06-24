def get(*args):
    print(args, type(args))


get(1, 2, 4, 5, 6)
get([1, 2, 3, 4, 5, 6])
get(*[1, 2, 3, 4, 5, 6])