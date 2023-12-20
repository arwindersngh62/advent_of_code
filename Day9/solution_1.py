from pathlib import Path
from numpy import diff, abs


data_file_path = Path(__file__).parent.resolve()/"data.txt"

with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()
new_line = [1]
all_sum = 0
for line in all_data:
    new_line = [int(item) for item in line.split(" ")]
    last_elements = []
    #while bool([k for k in new_line if k!=0]):
    while bool([k for k in new_line if k!=0]):
        last_elements.append(new_line[-1])
        new_line = diff(new_line)
    all_sum+=sum(last_elements)
    
print(all_sum)