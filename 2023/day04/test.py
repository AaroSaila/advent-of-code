import re

a = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"

b = a.split(":").pop().split("|")

print(b)