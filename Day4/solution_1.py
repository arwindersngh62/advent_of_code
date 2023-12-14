from pathlib import Path

data_file_path = Path(__file__).parent.resolve()/"data.txt"

def strip_spaces_and_make_ints(nums_string):
    temp_list =nums_string.split(" ")
    final_list = [int(i) for i in temp_list if i!=""]
    return final_list
with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()
total_points = 0

for data in all_data:
    numbers = data.split(":")[1]
    split_nums = numbers.split("|")
    winning_nums = strip_spaces_and_make_ints(split_nums[0])
    my_nums = strip_spaces_and_make_ints(split_nums[1])
    common_list = [i for i in my_nums if i in winning_nums]
    if len(common_list) > 0:
        points = 2**(len(common_list)-1)
        total_points+=points

print(total_points)
    
