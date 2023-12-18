from pathlib import Path

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
print(instructions)
map_dict = {}
for item in map_:
    split = item.split("=")
    map_dict[split[0].strip()] = split[1].strip()

first_output = get_output("AAA", instructions[0])
step = 1
while first_output!="ZZZ":
    first_output = get_output(first_output, instructions[step%len(instructions)])
    step+=1

print(step)