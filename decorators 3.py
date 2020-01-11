def repeat(n):
    def deco(func):
        def inner():
            for i in range(0,n):
                func()
        return inner
    return deco
@repeat(5)
def do_something():
    print("do_something() was called")

do_something()