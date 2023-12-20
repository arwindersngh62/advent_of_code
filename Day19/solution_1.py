from pathlib import Path
from numpy import diff, abs
from collections import namedtuple


data_file_path = Path(__file__).parent.resolve() / "data.txt"

with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()

index_of_blank = all_data.index("\n")
workflows = all_data[:index_of_blank]
parts = all_data[index_of_blank + 1 :]
part_tuple = namedtuple("part", ("x", "m", "a", "s"))


def spit_conditions(condition_str):
    split_cond = condition_str.split(",")
    last_cond = split_cond.pop(-1)
    cond_list = []
    for cond in split_cond:
        split = cond.split(":")
        cond_list.append((split[0], split[1]))
    last_cond = last_cond.split("}")[0]
    cond_list.append(("", last_cond))
    return cond_list


workflow_dict = {}
for item in workflows:
    item_split = item.split("{")
    workflow_dict[item_split[0]] = spit_conditions(item_split[1])


def get_value_for_attr(part_attr):
    return part_attr.split("=")[1]


all_parts_tuple_list = []
for i in parts:
    split_part = i.split(",")
    new_part = {
        "x": get_value_for_attr(split_part[0]),
        "m": get_value_for_attr(split_part[1]),
        "a": get_value_for_attr(split_part[2]),
        "s": get_value_for_attr(split_part[3].split("}")[0]),
    }
    all_parts_tuple_list.append(new_part)
print("all parsing done")


def check_condition(value, sign, value_to_compare):
    if sign == ">":
        #print(f"check: {value} greater than {value_to_compare}")
        return int(value)>int(value_to_compare)
    if sign == "<":
        #print(f"check: {value} less than {value_to_compare}")
        return int(value)<int(value_to_compare)
    if sign == "=":
        #print(f"check: {value} equal than {value_to_compare}")
        return int(value)==int(value_to_compare)
    
def apply_workflow(part, workflow):
    for node in workflow:
        condition = node[0]
        if condition == "":
            return node[1]
        variable = condition[0]
        sign = condition[1]
        value_to_compare = condition[2:].split("}")[0]
        result = check_condition(part[variable],sign,  value_to_compare)
        if result:
            return node[1]


accepted_parts = []
first_workflow = workflow_dict["in"]
for part_ in all_parts_tuple_list:
    result = apply_workflow(part_, first_workflow)
    while result not in ("A", "R"):
        result = apply_workflow(part_, workflow_dict[result])
    if result == "A":
        accepted_parts.append(part_)
print("accepted parts calculated")
total_sum = 0
for part in accepted_parts:
    sum_ = sum([int(value) for value in part.values()])
    total_sum+=sum_
    
print(total_sum)