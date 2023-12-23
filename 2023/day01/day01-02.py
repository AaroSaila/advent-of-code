import re


numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


class txtFile:
    def __init__(self, path):
        self.path = path
        with open(self.path, "r") as file:
            self.contents = file.read().splitlines()
    

class numberString:
    def __init__(self, string):
        self.string = string

    def parse_first_number(self):
        chars = re.findall("\w", self.string)
        test_string = ""
        first_number = ""
        for i in chars:
            if re.match("\d", i):
                first_number += i
                return first_number
            else:
                test_string += i
                for x in range(len(numbers)):
                    number = re.findall(numbers[x], test_string)
                    if number:
                        if number[0] in numbers:
                            first_number += str(int(x) + 1)
                            return first_number
    
    def parse_last_number(self):
        chars = re.findall("\w", self.string)
        chars_reversed = []
        test_string = ""
        for i in reversed(chars):
            chars_reversed.append(i)
        for i in chars_reversed:
            if re.match("\d", i):
                last_number = i
                return last_number
            else:
                test_string = "".join((i, test_string))
                for z in numbers:
                    if z in test_string:
                        last_number = str((numbers.index(z) + 1))
                        return last_number
        
    
def parse_numbers(string):
     string_object = numberString(string)
     parsed_string = string_object.parse_first_number() + string_object.parse_last_number()
     return parsed_string


codes = txtFile("2023/day01/input.txt").contents #["kpmrk5flx"] 

nums = []
for i in codes:
    nums.append(int(parse_numbers(i)))

result = 0
for i in nums:
    result += i

print(result)
