from pathlib import Path

data_file_path = Path(__file__).parent.parent.resolve()/"data_file.txt"

def is_set_impossible(game_set):
    game_dict = {"red": 12,"blue": 14, "green": 13 }
    for show in game_set.split(","):
        show_split = show.strip().split(" ")
        color = show_split[1]
        number = show_split[0]
        if game_dict[color] < int(number):
            return True
        
    return False

impossible_game_sum = 0

with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()
    for datum in all_data:
        is_game_possible = False
        split_at_colon = datum.split(":")
        game_meta = split_at_colon[0]
        all_game_sets = split_at_colon[1].split(";")
        for game_set in all_game_sets:
            if is_set_impossible(game_set):
                is_game_possible = False
                break
            is_game_possible = True
        if is_game_possible:
            impossible_game_sum+=int(game_meta.split(" ")[1])            
            
print(impossible_game_sum)
        

