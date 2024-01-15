"""advent of code day 5 part 1"""
import re


def process_input_data(data):
    """Processes the input data"""

    def get_seeds(data):
        local_seeds = data[0].split(":")[1].split(" ")
        local_seeds.remove("")
        seeds_list = []
        for seed in local_seeds:
            seeds_list.append(int(seed))
        local_seeds = seeds_list
        return local_seeds

    def get_next_map(data):
        def process_row(row_string):
            row = {}
            row_numbers = []
            row_numbers_string = row_string.split(" ")
            for number in row_numbers_string:
                row_numbers.append(int(number))
            row["source"] = row_numbers[1]
            row["destination"] = row_numbers[0]
            row["range"] = row_numbers[2]
            return row

        name = data[0].replace(" map:", "")
        data.pop(0)
        rows = []
        to_be_removed = []
        for item in data:
            if re.search(r"\d", item) is not None:
                rows.append(process_row(item))
                to_be_removed.append(item)
            else:
                for item2 in to_be_removed:
                    data.remove(item2)
                    to_be_removed = []
                break
        if to_be_removed:
            for item2 in to_be_removed:
                data.remove(item2)
        return {"name": name, "rows": rows}

    processed_data = {}

    while "" in data:
        data.remove("")

    processed_data["seeds"] = get_seeds(data)
    data.pop(0)
    maps_remaining = True
    while maps_remaining:
        try:
            _map = get_next_map(data)
            processed_data[_map["name"]] = _map["rows"]
        except IndexError:
            maps_remaining = False

    return processed_data

def process_seed(seed, seed_maps):
    """Processes seed through given maps"""

    def process_row(local_seed, source, destination, range_length):
        if local_seed not in range(source, source + range_length):
            return local_seed
        difference = local_seed - source
        result = destination + difference
        return result

    for _map in seed_maps.items():
        for row in _map[1]:
            original_seed = seed
            seed = process_row(
                seed,
                row["source"],
                row["destination"],
                row["range"]
            )
            if seed != original_seed:
                break

    return seed

with open(
    "/home/aaro/Documents/Code/advent-of-code/2023/day05/input.txt",
    "r",
    encoding="utf-8"
) as file:
    input_data = file.read().splitlines()

input_data = process_input_data(input_data)
seeds = input_data["seeds"]
maps = {}

for _map in input_data.items():
    if _map[0] != "seeds":
        maps[_map[0]] = _map[1]

locations = []
for i in seeds:
    locations.append(process_seed(i, maps))
locations.sort()

print(locations)
