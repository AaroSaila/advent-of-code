import re

class txtFile:
    def __init__(self, path):
        self.path = path
        self.contents = open(path, "r").read().splitlines()


class Line:
    lines = []  # line objects
    def __init__(self, string, id):
        def get_stars():
            stars = re.finditer("\*", self.string)
            for star in stars:
                star_object = Star(self, (star.start(), star.end()))
                self.stars.append(star_object)
            return
    

        self.id = id
        self.string = string
        self.stars = []  # Star objects
        get_stars()
        Line.lines.append(self)


class Star:
    stars = []  # Star objects
    def __init__(self, line, span):
        self.line = line  # line object
        self.span = span  # tuple
        self.ratio_nums = []  # ints
        self.ratio = 1  # Changes with method
        Star.stars.append(self)
    
    def get_ratio(self):
        # Sets the span to be scanned
        if self.span[0] == 0:
            span_to_scan = (self.span[0], self.span[1] + 1)
        elif self.span[1] == len(self.line.string):
            span_to_scan = (self.span[0] - 1, self.span[1])
        else:
            span_to_scan = (self.span[0] - 1, self.span[1] + 1)
        # Tries to check line above
        try:
            string_above = Line.lines[self.line.id - 1].string
            string_to_scan = string_above[span_to_scan[0] : span_to_scan[1]]
            scan = re.search("\d+", string_to_scan)
            if scan != None:
                self.ratio_nums.append(int(scan.group()))
        except(IndexError):
            pass
        
        # Checks own line
        string_to_scan = self.line.string[span_to_scan[0] : span_to_scan[1]]
        scan = re.search("\d+]", string_to_scan)
        if scan != None:
            self.ratio_nums.append(int(scan.group()))
            return
    
        # Tries to check line below
        try:
            string_below = Line.lines[self.line.id + 1].string
            string_to_scan = string_below[span_to_scan[0] : span_to_scan[1]]
            scan = re.search("\d+", string_to_scan)
            if scan != None:
                self.ratio_nums.append(int(scan.group()))
        except(IndexError):
            pass

        for num in self.ratio_nums:
            self.ratio *= num
        
        return


def sum_of_ratios(stars):
    sum = 0
    for star in stars:
        sum += star.ratio
    return sum


input_data = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592....."
    "......755.",
    "...$.*....",
    ".664.598.."
]

for line in input_data:
    line_object = Line(line, input_data.index(line))

for star in Star.stars:
    star.get_ratio()

print(sum_of_ratios(Star.stars))
