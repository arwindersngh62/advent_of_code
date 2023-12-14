from pathlib import Path

data_file_path = Path(__file__).parent.parent.resolve()/"data_file.txt"

def get_power_set(game_sets):
    game_dict = {"red": 1,"blue": 1, "green": 1 }
    for game_set in game_sets:
        for show in game_set.split(","):
            show_split = show.strip().split(" ")
            color = show_split[1]
            number = int(show_split[0])
            if game_dict[color] < number:
                game_dict[color] = number
        
    power = 1
    for value in game_dict.values():
        power = power * value
    return power

power_sum = 0

with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()
    for datum in all_data:
        is_game_possible = False
        split_at_colon = datum.split(":")
        game_meta = split_at_colon[0]
        all_game_sets = split_at_colon[1].split(";")
        power_sum+=get_power_set(all_game_sets)    
            
print(power_sum)
        

