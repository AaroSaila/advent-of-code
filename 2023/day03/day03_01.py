import re


class txtFile:
    def __init__(self, path):
        self.path = path
        with open(self.path, "r") as file:
            self.contents = file.read().splitlines()


class Line:
    lines = []  # line objects

    def __init__(self, string, id):
        def get_numbers():
            numbers = re.findall(r"\d+", self.string)
            for number in numbers:
                number_object = Number(self, number)
                self.numbers.append(number_object)
            return

        self.id = id
        self.string = string
        self.numbers = []  # Number objects
        get_numbers()
        Line.lines.append(self)


class Number:
    numbers = []  # Number objects

    def __init__(self, line, value):
        def get_span():
            iters = re.finditer(r"\d+", self.line.string)
            for i in iters:
                if i.group() == self.value:
                    return (i.start(), i.end())

        self.line = line  # line object
        self.value = value  # number
        self.span = get_span()
        self.part_number = False  # /True
        Number.numbers.append(self)

    def check_if_part_number(self):
        def check_strings():
            # Sets the span to scan from string
            if self.span[0] == 0:
                span_to_scan = (self.span[0], self.span[1] + 1)
            elif self.span[1] == len(self.line.string):
                span_to_scan = (self.span[0] - 1, self.span[1])
            else:
                span_to_scan = (self.span[0] - 1, self.span[1] + 1)
            # Tries to check line above
            try:
                string_above = Line.lines[self.line.id - 1].string
                string_to_scan = string_above[span_to_scan[0]:span_to_scan[1]]
                if re.search(r"[^\d.]", string_to_scan) is not None:
                    self.part_number = True
                    return
            except (IndexError):
                pass

            # Checks own line
            string_to_scan = self.line.string[span_to_scan[0]:span_to_scan[1]]
            if re.search(r"[^\d.]", string_to_scan) is not None:
                self.part_number = True
                return

            # Tries to check line below
            try:
                string_below = Line.lines[self.line.id + 1].string
                string_to_scan = string_below[span_to_scan[0]:span_to_scan[1]]
                if re.search(r"[^\d.]", string_to_scan) is not None:
                    self.part_number = True
                    return
            except (IndexError):
                pass

            return

        check_strings()

        return


def sum_part_numbers(numbers):
    result = 0
    for number in numbers:
        if number.part_number:
            result += int(number.value)
    return result


input_data = txtFile("2023/day03/input.txt").contents

for line in input_data:
    line = Line(line, input_data.index(line))

for number in Number.numbers:
    number.check_if_part_number()

print(sum_part_numbers(Number.numbers))
