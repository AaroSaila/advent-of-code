class txtFile:
    def __init__(self, path):
        self.path = path
        with open(self.path, "r") as file:
            self.contents = file.read().splitlines()


class Map:
    maps = []  # Map objects

    def __init__(self, row_data):
        def process_row_data(row_data):
            rows = []
            for row in row_data:
                rows.append(Row(row))
            return rows
        
        self.rows = process_row_data(row_data)  # Row objects
        Map.maps.append(self)

    def source_to_destination(self, seed):
        for row in self.rows:
            source_start = row.source_range_start
            source_end = source_start + row.range_length
            destination_start = row.destination_range_start
            if seed < source_start or seed > source_end:
                pass
            else:
                seed = destination_start + (seed - source_start)
        return seed


class Row:
    def __init__(self, row_list_ints):
        self.destination_range_start = row_list_ints[0]
        self.source_range_start = row_list_ints[1]
        self.range_length = row_list_ints[2]


def get_data_from_contents(contents):
    for _string in contents:
        contents[contents.index(_string)] = _string.split(" ")
    for _list in contents:
        for number_string in _list:
            _list[_list.index(number_string)] = int(number_string)
    return contents


def get_data(path):
    data = get_data_from_contents(txtFile(path).contents)
    return data


def process_seeds(seeds):
    for seed in seeds:
        seeds[seeds.index(seed)] = int(seed)
    return


seeds = txtFile("2023/day05/inputs/seeds.txt").contents[0].split(" ")
process_seeds(seeds)
seed_to_soil_data = get_data(
    "2023/day05/inputs/01_seed_to_soil_map.txt"
)
soil_to_fertilizer_data = get_data(
    "2023/day05/inputs/02_soil_to_fertilizer_map.txt"
)
fertilizer_to_water_data = get_data(
    "2023/day05/inputs/03_fertilizer_to_water_map.txt"
)
water_to_light_data = get_data(
    "2023/day05/inputs/04_water_to_light_map.txt"
)
light_to_temperature_data = get_data(
    "2023/day05/inputs/05_light_to_temperature_map.txt"
)
temperature_to_humidity_data = get_data(
    "2023/day05/inputs/06_temperature_to_humidity_map.txt"
)
humidity_to_location_data = get_data(
    "2023/day05/inputs/07_humidity_to_location_map.txt"
)

print(seeds)

seed_to_soil_map = Map(seed_to_soil_data)
print(seed_to_soil_map.source_to_destination(seeds[0]))
