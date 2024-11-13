def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

def calculate(**kwargs):
    for key, value in kwargs.items():
         
print(add(1, 2, 3, 10))
print(calculate(add=3, multiply=5))