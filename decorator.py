def decor(f):
    def wrap(name):
        if name != "Delvin":
            raise ValueError("Invalid username")
        print(f"{name} is verified, loading....")
        return f(name)
    return wrap

@decor
def log_in(name):
    print("successfully logged in")
log_in("Delvin")


def positive_wrap(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input has to be a positive value")
        else:
            print("Calculating...Please Hold On")
        return func(x)
    return wrapper

@positive_wrap
def calculate(x):
    return x**2

print(calculate(10))


@positive_wrap
def calculate_cube(x):
    return x**3

print(calculate_cube(3))
            