from pathlib import Path
from numpy import diff, abs


data_file_path = Path(__file__).parent.resolve()/"data.txt"

with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()

index_of_blank = all_data.index("\n")
workflows = all_data[:index_of_blank]
parts = all_data[index_of_blank+1:]

def spit_conditions(condition_str):
    split_cond = condition_str.split(",")
    last_cond = split_cond.pop(-1)
    cond_list = []
    first_cont_dict = {}
    for cond in split_cond:
        split = cond.split(":")
        cond_list.append((split[0],split[1]))
    last_cond = last_cond.split("}")[0]
    cond_list.append(("",last_cond))
    return cond_list

workflow_dict = {}
for item in workflows:
    item_split = item.split("{")
    workflow_dict[item_split[0]] = spit_conditions(item_split[1])

print(workflow_dict)