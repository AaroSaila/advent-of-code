import re

class txtFile:
    def __init__(self, path):
        self.path = path
        self.contents = open(path, "r").read().splitlines()


class Line:
    lines = []  # line objects
    def __init__(self, string, id):
        def make_stars():
            star_list = []
            stars = re.finditer(r"\*", self.string)
            for star in stars:
                star_span = (star.start(), star.end())
                star_object = Star(self, star_span)
                star_list.append(star_object)
            
            return star_list
        
        def make_numbers():
            number_list = []
            numbers = re.finditer(r"\d+", self.string)
            for number in numbers:
                number_value = int(number.group())
                if number.start() == 0:
                    number_span = range(number.start(), number.end() + 1)
                else:
                    number_span = range(number.start() - 1, number.end() + 1)
                number_object = Number(self, number_value, number_span)
                number_list.append(number_object)

            return number_list

    
        self.id = id
        self.string = string
        self.stars = make_stars()
        self.numbers = make_numbers()
        Line.lines.append(self)


class Star:
    stars = []  # Star objects
    def __init__(self, line, span):
        self.line = line  # line object
        self.span = span  # range
        self.ratio_nums = []  # ints
        self.ratio = 1  # Changes with method
        Star.stars.append(self)
    
    def get_ratio(self):
        def append_adjacent_numbers_of_line(line):
            numbers = line.numbers
            for number in numbers:
                star_adjacent_to_number = (self.span[0] or self.span[1]) in number.span
                if star_adjacent_to_number:
                    self.ratio_nums.append(number.value)
            return


        def calculate_ratio():
            star_has_exactly_two_adjacent_nums = len(self.ratio_nums) == 2
            if star_has_exactly_two_adjacent_nums:
                for number in self.ratio_nums:
                    self.ratio *= number
            return

        # Tries to check line above
        try:
            line_above = Line.lines[self.line.id - 1]
            append_adjacent_numbers_of_line(line_above)
            
        except(IndexError):
            pass

        # Checks own line
        own_line = self.line
        append_adjacent_numbers_of_line(own_line)
        
        # Tries to check line below
        try:
            line_below = Line.lines[self.line.id + 1]
            append_adjacent_numbers_of_line(line_below)

        except(IndexError):
            pass

        calculate_ratio()

        return

class Number:
    numbers = [] # Number objects
    def __init__(self, line, value, span):
        self.line = line  # line object
        self.value = value  # int
        self.span = span  # range
        Number.numbers.append(self)


def sum_of_ratios():
    sum = 0
    for star in Star.stars:
        if star.ratio != 1:
            sum += star.ratio
    return sum


input_data = txtFile("2023/day03/input.txt").contents

for line in input_data:
    line_object = Line(line, input_data.index(line))

for star in Star.stars:
    star.get_ratio()

print(sum_of_ratios())
