
def new(x):
    def b(fuc):
        def c():
            return fuc()+10+x
        return c
    return b

@new(100)
def a():
    return 10

print(a())