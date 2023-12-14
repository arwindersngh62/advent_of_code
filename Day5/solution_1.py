from pathlib import Path

data_file_path = Path(__file__).parent.resolve()/"data.txt"

with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()

    
def parse_section(all_data, next_section_name):
    parsed_section_list = []
    for _ in range(len(all_data)):
        data = all_data.pop(0)
        if next_section_name in data:
            break
        data = data.split(" ")
        if data != ["""\n"""]:
            parsed_section_list.append(data)
    return parsed_section_list, all_data

seeds_line = all_data.pop(0)
seed_to_soil_map= []
all_data.pop(0)
all_data.pop(0)



seed_to_soil_map, all_data = parse_section(all_data, "soil-to-fertilizer map")
soil_to_fertilizer_map, all_data = parse_section(all_data, "fertilizer-to-water map")
fertilizer_to_water_map, all_data = parse_section(all_data, "water-to-light map")
water_to_light_map, all_data = parse_section(all_data, "light-to-temperature map")
light_to_temprature_map, all_data = parse_section(all_data, "temperature-to-humidity map")
temperature_to_humidity_map, all_data = parse_section(all_data, "humidity-to-location map")
humidity_to_location_map = []
for data in all_data:
    humidity_to_location_map.append(data.split(" "))   


def get_dest_if_exits(key_, map_):
    for line in map_:
        start_source = int(line[1])
        start_dest = int(line[0])
        range_ = int(line[2])
        if key_ in range(start_source, start_source+range_):
            diff = key_ - start_source
            return start_dest + diff
    return key_

location_low = None

seed_str = seeds_line.split(":")[1].split(" ")


for seed in seed_str:
    if seed == "":
        continue
    seed = int(seed)
    soil = get_dest_if_exits(seed, seed_to_soil_map)
    fertilizer = get_dest_if_exits(soil, soil_to_fertilizer_map)
    water = get_dest_if_exits(fertilizer, fertilizer_to_water_map)
    light = get_dest_if_exits(water, water_to_light_map)
    temp = get_dest_if_exits(light, light_to_temprature_map)
    humidity = get_dest_if_exits(temp, temperature_to_humidity_map)
    location = get_dest_if_exits(humidity, humidity_to_location_map)
    if location_low is None:
        location_low =  location
    if location< location_low:
        location_low = location
print(location_low)
    
    
    