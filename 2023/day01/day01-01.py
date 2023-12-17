class File:
    def __init__(self, path):
        self.path = path
        self.file = open(path, "r")
        self.codes = self.file.read().splitlines()


codes = File("2023/day01/input.txt").codes

nums = []
for i in codes:
    num = "".join(filter(str.isdigit, i))
    nums.append(num)

nums2 = []
for i in nums:
    x = int(i[0] + i[-1])
    nums2.append(x)

result = 0
for i in range(len(nums2)):
    result += nums2[i]

print(result)