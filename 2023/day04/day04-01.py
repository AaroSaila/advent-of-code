import re

class txtFile:
    def __init__(self, path):
        self.path = path
        with open(self.path, "r") as file:
            self.contents = file.read().splitlines()
    

class Card:
    cards = []
    sum_of_points = 0
    def __init__(self, string):
        def get_numbers(number_string):
            numbers = set()
            for number in re.findall("\d+", number_string):
                numbers.add(number)
            return numbers
        
        def calculate_points():
            for winning_number in self.winning_numbers:
                if winning_number in self.numbers and self.points == 0:
                    self.points += 1
                elif winning_number in self.numbers and self.points != 0:
                    self.points *= 2
            return


        self.string = string
        self.all_numbers = self.string.split(":").pop().split("|")  # list
        self.winning_numbers = get_numbers(self.all_numbers[0])  # set
        self.numbers = get_numbers(self.all_numbers[1])  # set
        self.points = 0
        calculate_points()
        Card.cards.append(self)

    def calculate_sum_of_points(self):
        for card in Card.cards:
            Card.sum_of_points += card.points
        return


input_data = txtFile("2023/day04/input.txt").contents
# txtFile("2023/day04/example.txt").contents


for string in input_data:
    Card(string)

Card.calculate_sum_of_points(Card)
print(Card.sum_of_points)
