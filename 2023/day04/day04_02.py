import re


class TxtFile:
    def __init__(self, path):
        self.path = path
        with open(self.path, "r", encoding="utf-8") as file:
            self.contents = file.read().splitlines()


class Card:
    cards = []  # Card objects
    total_cards = None

    def __init__(self, winning_numbers, numbers):
        self.winning_numbers = winning_numbers  # set
        self.numbers = numbers  # set
        self.iterations = 1
        Card.cards.append(self)

    def update_iterations(self):
        index = Card.cards.index(self)
        hits = 0
        for number in self.winning_numbers:
            if number in self.numbers:
                hits += 1
                card_to_be_changed = Card.cards[index + hits]
                card_to_be_changed.iterations += 1

    def check_card(self):
        for i in range(self.iterations):
            self.update_iterations()
        return

    def count_cards(self):
        Card.total_cards = 0
        for card in Card.cards:
            Card.total_cards += card.iterations
        return


def get_numbers_for_card(separated_card_string):
    numbers = set()
    for number in re.findall(r"\d+", separated_card_string):
        numbers.add(number)
    return numbers


input_data = TxtFile("2023/day04/input.txt").contents

for card in input_data:
    numbers_list = card.split(":").pop().split("|")
    winning_numbers = get_numbers_for_card(numbers_list[0])
    numbers = get_numbers_for_card(numbers_list[1])
    Card(winning_numbers, numbers)

for card in Card.cards:
    card.check_card()

Card.count_cards(Card)
print(Card.total_cards)
