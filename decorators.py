def outer(func):
    counter = 0
    def inner():
        nonlocal counter
        print("Was called " + str(counter) + " times")
        counter = counter + 1
        func()

    return inner

@outer
def do_something():
    print("do_something()")


do_something()
do_something()
do_something()
do_something()
do_something()
do_something()