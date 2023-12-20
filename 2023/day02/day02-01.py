import re


maximums = {"blues": 14, "reds": 12, "greens": 13}

possibles = 0
impossibles = 0
possible_games = []


class txtFile:
    def __init__(self, path):
        self.path = path
        self.contents = open(path, "r").read().splitlines()


class Game:
    def __init__(self, id):
        self.id = id
        self.sets = []
        self.possible = True


class Set:
    def __init__(self, cubes):
        self.cubes = cubes.split(",")
        self.reds = color_count("red", self.cubes)
        if (color_count("blue", self.cubes) > maximums["blues"] or 
            color_count("red", self.cubes) > maximums["reds"] or
            color_count("green", self.cubes) > maximums["greens"]):
            self.possible = False
        else:
            self.possible = True


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
                nums = re.findall("\d", cube)
                try:
                    nums[1]
                    nums_string = ""
                    for num in nums:
                        nums_string += "".join(num)
                    nums = int(nums_string)
                    color_count += nums
                except(IndexError):
                    color_count += int(nums[0])
    return color_count


games_list = txtFile("2023/day02/input.txt").contents

games = make_dict(games_list)

for i in range(1, len(games) + 1):
    game = Game(i)
    for x in range(len(games[i])):
        set_object = Set(games[i][x])
        game.sets.append(set_object)
    for _set in game.sets:
        if _set.possible == False:
            game.possible = False
    if game.possible:
        possibles += 1
        possible_games.append(game.id)
    else:
        impossibles += 1

sum_of_possible_game_ids = 0
for id in possible_games:
    sum_of_possible_game_ids += id

print("imposibles: " + str(impossibles) + "\n" + "possibles: " + str(possibles))
print("possible games: ", possible_games)
print("sum of impossible game ids", sum_of_possible_game_ids)
