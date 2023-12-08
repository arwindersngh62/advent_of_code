from pathlib import Path

data_file_path = Path(__file__).parent.parent.resolve()/"data_file.txt"

def join_numbers_list(numbers_list):
    temp_num = ""
    temp_num = numbers_list[0] + numbers_list[-1]
    return int(temp_num)


all_digits_list = []

with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()
    
    for one_data in all_data:
        one_num_list = [digit for digit in one_data if digit.isdigit()]
        one_digit = join_numbers_list(one_num_list)
        all_digits_list.append(one_digit)
     
print(sum(all_digits_list))