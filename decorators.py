# understand functions
def f1():
    print("Called f1")


def f2(f):
    f()


f2(f1)


# f1 is an object and can be passed through parameters

def h1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args, **kwargs)
        print("Ended")
        return val

    return wrapper

@h1
def h(a, b=9):
    print(a, b)

@h1
def add(x, y):
    return x + y


print(add(4, 5))
