import re


class txtFile:
    def __init__(self, path):
        self.path = path
        with open(self.path, "r") as file:
            self.contents = file.read().splitlines()


class Game:
    games = {}
    sum_of_powers = 0

    def __init__(self, id):
        self.id = id
        self.sets = []
        self.minimums = {"reds": None, "greens": None, "blues": None}
        self.power = None
        if self.id is not None:
            self.games["Game " + str(self.id)] = self

    def check_minimums(self):
        reds = []
        greens = []
        blues = []
        for _set in self.sets:
            reds.append(_set.reds)
            greens.append(_set.greens)
            blues.append(_set.blues)
        reds.sort()
        greens.sort()
        blues.sort()
        self.minimums["reds"] = reds[-1]
        self.minimums["greens"] = greens[-1]
        self.minimums["blues"] = blues[-1]
        return

    def check_power(self):
        reds = self.minimums["reds"]
        greens = self.minimums["greens"]
        blues = self.minimums["blues"]
        self.power = reds * greens * blues
        Game.sum_of_powers += self.power
        return


class Set:
    def __init__(self, cubes):
        self.cubes = cubes.split(",")
        self.reds = color_count("red", self.cubes)
        self.greens = color_count("green", self.cubes)
        self.blues = color_count("blue", self.cubes)


def make_dict(list):
    games_dict = {}
    x = 1
    for game in list:
        game_list = game.split(":")
        games_dict[x] = game_list[1].split(";")
        x += 1

    return games_dict


def color_count(color, cubes):
    color_count = 0
    for cube in cubes:
        if color in cube:
            nums = re.findall(r"\d", cube)
            try:
                nums[1]
                nums_string = ""
                for num in nums:
                    nums_string += "".join(num)
                nums = int(nums_string)
                color_count += nums
            except (IndexError):
                color_count += int(nums[0])
    return color_count


input_data = txtFile("2023/day02/input.txt").contents

input_dict = make_dict(input_data)

for i in range(1, len(input_dict) + 1):
    game = Game(i)
    for _set in input_dict[i]:
        game.sets.append(Set(_set))
    game.check_minimums()
    game.check_power()

for i in range(1, len(Game.games) + 1):
    print(Game.games["Game " + str(i)].minimums)
    print(Game.games["Game " + str(i)].power)

print("--------------------------------------------")
print(Game.sum_of_powers)
print("--------------------------------------------")
