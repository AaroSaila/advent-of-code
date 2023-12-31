class txtFile:
    def __init__(self, path):
        self.path = path
        with open(self.path, "r") as file:
            self.contents = file.read().splitlines()


class Map:
    maps = []  # Map objects

    def __init__(self):
        self.rows = []  # Row objects
        Map.maps.append(self)
    
    def create_rows(self, row):
        for row in seed_to_soil_data:
            row_list = row.split(" ")
            row_list = list_items_to_ints(row_list)
            seed_to_soil_map.rows.append(Row(row_list, seed_to_soil_map))


class Row:
    def __init__(self, row_list_ints, map_object):
        self.destination_range_start = row_list_ints[0]
        self.source_range_start = row_list_ints[1]
        self.range_length = row_list_ints[2]
        map_object.rows.append(self)


def list_items_to_ints(_list):
    new_list = []
    for item in _list:
        item = int(item)
        new_list.append(item)
    return new_list


seeds = txtFile("2023/day05/inputs/seeds.txt").contents[0].split(" ")
seed_to_soil_data = txtFile(
    "2023/day05/inputs/01_seed_to_soil_map.txt"
).contents

seed_to_soil_map = Map()



