import re


class TxtFile:
    def __init__(self, path):
        self.path = path
        with open(self.path, "r", encoding="utf-8") as file:
            self.contents = file.read().splitlines()


class Card:
    cards = []  # Card objects

    def __init__(self, index, winning_numbers, numbers):
        self.index = index
        self.winning_numbers = winning_numbers
        self.numbers = numbers
        Card.cards.append(self)


def get_numbers_for_card(separated_card_string):
    numbers = set()
    for number in re.findall(r"\d+", separated_card_string):
        numbers.add(number)
    return numbers


input_data = TxtFile("2023/day04/example.txt").contents

print(input_data)
