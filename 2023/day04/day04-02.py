import re

class txtFile:
    def __init__(self, path):
        self.path = path
        with open(self.path, "r") as file:
            self.contents = file.read().splitlines()


input_data = txtFile("2023/day04/example.txt").contents

print(input_data)