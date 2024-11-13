import time


def speed_calc_decorator(function):
    def wrapped_function():
        time_before = time.time()
        function()
        time_after = time.time()
        time_diff = time_after - time_before
        print(f"{function.__name__} run speed: {time_diff}s")

    return wrapped_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()
