from pathlib import Path
from numpy import diff, abs
from collections import namedtuple

#Reachability problem any one of the reachability algorithm would work
#I am using back tracing
data_file_path = Path(__file__).parent.resolve() / "data_test.txt"

with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()

index_of_blank = all_data.index("\n")
workflows = all_data[:index_of_blank]



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
finishing_workflows = []
workflow_dict = {}
for item in workflows:
    item_split = item.split("{")
    workflow_dict[item_split[0]] = spit_conditions(item_split[1])
    if "A" in item:
        finishing_workflows.append(item_split[0])
print(finishing_workflows)
print(workflow_dict)
    