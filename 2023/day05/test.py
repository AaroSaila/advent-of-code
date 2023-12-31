a = ["one", "two", "three"]
b = [1, 2, 3]

c = dict()

for i in range(len(a)):
    c[a[i]] = b[i]

print(c)