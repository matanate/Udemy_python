import pandas as pd

with open("file1.txt") as f1:
    f1_numbers = f1.readlines()


with open("file2.txt") as f2:
    f2_numbers = f2.readlines()


result = [int(n) for n in f1_numbers if n in f2_numbers]
print(result)
