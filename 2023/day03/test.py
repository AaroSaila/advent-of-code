import re

a = "...*...*.....*"

b = re.finditer("\*", a)

for i in b:
    print(i.start(), i.end())