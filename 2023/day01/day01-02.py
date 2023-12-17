import re


numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def parse_numbers(string):
    chars = re.findall("\w", string)
    test_string = ""
    new_string = ""
    for i in chars:
        if re.match("\d", i):
            new_string += i
        else:
            test_string += i
            for x in range(len(numbers)):
                number = re.findall(numbers[x], test_string)
                if number:
                    if number[0] in numbers:
                        new_string += str(int(x) + 1)
                        test_string = ""
    
    return new_string


class File:
    def __init__(self, path):
        self.path = path
        self.file = open(path, "r")
        self.codes = self.file.read().splitlines()


codes = File("2023/day01/input.txt").codes
""" [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
] """

nums = []
for i in codes:
    nums.append(parse_numbers(i))

nums2 = []
for i in nums:
    x = int(i[0] + i[-1])
    nums2.append(x)


result = 0
for i in range(len(nums2)):
    print(nums2[i])
    result += nums2[i]

print(result)
