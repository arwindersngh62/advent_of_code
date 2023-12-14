from pathlib import Path

data_file_path = Path(__file__).parent.resolve()/"data.txt"

def strip_spaces_and_make_ints(nums_string):
    temp_list =nums_string.split(" ")
    final_list = [int(i) for i in temp_list if i!=""]
    return final_list
with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()
total_points = 0
card_number = 0
card_copies_dict = {}
for data in all_data:
    card_number+=1
    if card_number in card_copies_dict.keys():
        card_copies_dict[card_number]+=1
        current_card_copies = card_copies_dict[card_number]
    else:
        card_copies_dict[card_number] = 1
        current_card_copies = 1 
    numbers = data.split(":")[1]
    split_nums = numbers.split("|")
    winning_nums = strip_spaces_and_make_ints(split_nums[0])
    my_nums = strip_spaces_and_make_ints(split_nums[1])
    common_list = [i for i in my_nums if i in winning_nums]
    if len(common_list) > 0:
        for i in range(1,len(common_list)+1):
            next_card_num = card_number+i
            if not (next_card_num in card_copies_dict.keys()):
                card_copies_dict[next_card_num] = current_card_copies
            else:
                card_copies_dict[next_card_num]+=current_card_copies                
print(card_copies_dict)
print(sum(card_copies_dict.values()))

    
