class txtFile:
    def __init__(self, path):
        self.path = path
        with open(self.path, "r") as file:
            self.contents = file.read().splitlines()


codes = txtFile("2023/day01/input.txt").contents

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
