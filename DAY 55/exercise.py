input = eval(input())


def logging_decorator(function):
    def wrapper(*args):
        statement = f"You called {function.__name__}{args}"
        print(statement)
        print(f"It returned: {function(args[0], args[1], args[2])}")

    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(input[0], input[1], input[2])
