from pathlib import Path
from math import gcd

data_file_path = Path(__file__).parent.resolve()/"data.txt"

with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()
    
instructions = all_data[0].strip()
map_ = all_data[2:]
def get_output(node, instruction):
    tuple_ = map_dict[node]
    if instruction == "L":
        return tuple_[1:4]
    else:
        return tuple_[6:9]

# The number of nodes ending in A and number of nodes ending in Z being equal
# means that one starting point will always end on the same ending point which means there
# is periodicity
#TODO: Write proof of this
    

map_dict = {}
for item in map_:
    split = item.split("=")
    map_dict[split[0].strip()] = split[1].strip()

current_nodes = [k for k in map_dict.keys() if k[-1] == "A"]


step_count = 0
seen_nodes = []
periods = []
for current_node in current_nodes:
    step_count = 0
    while current_node[-1] != "Z":
        instruction = instructions[step_count%len(instructions)]
        current_node = get_output(current_node, instruction)
        step_count+=1
    periods.append(step_count)
print(periods)

# the step count when all are at Z ending nodes is the LCM of all
lcm_all = 1

for period in periods:
    lcm_all = lcm_all*period//gcd(lcm_all, period)
    
print(lcm_all)    
    