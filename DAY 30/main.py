
# try:
#     file = open("a_file.txt")
#     a = {"key": "value"}
#     print(a["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Somthing")
# except KeyError as error_messege:
#     print(f"the key {error_messege} does not exist")
# else:
#     contant = file.read()
#     print(contant)
# finally:
#     raise KeyError("made up")

height = float(input("Hight: "))
weight = float(input("Weight: "))

if height >3:
    raise ValueError("height must be under 3m")

bmi = weight/ height **2

print(bmi)