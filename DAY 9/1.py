a = {"a": int("100"), "b": int("2"), "c": int("500"), "d": int("1")}

print(sorted(a.items(), key=lambda x:x[1]))