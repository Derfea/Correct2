def outer(func):
    cached = {}
    def inner(x):
        if x in cached:
            return cached[x]
        result = func(x)
        cached[x] = result
        return result

    return inner 

@outer
def calculate_something(x):
    print("calculate_something(" + str(x) + ")")
    return x * x

print(calculate_something(5))
print(calculate_something(5))