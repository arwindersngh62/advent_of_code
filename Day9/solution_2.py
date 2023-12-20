from pathlib import Path
from numpy import diff, abs


data_file_path = Path(__file__).parent.resolve()/"data.txt"

with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()
new_line = [1]
all_sum = 0
def get_reverse_alternate_diff(first_elements):
    count = 0
    sum_=0
    for element in first_elements:
        sum_+=((-1)**count *element)
        count+=1
    return  sum_
for line in all_data:
    new_line = [int(item) for item in line.split(" ")]
    first_elements = []
    while bool([k for k in new_line if k!=0]):
        first_elements.append(new_line[0])
        new_line = diff(new_line)
    
    all_sum+=get_reverse_alternate_diff(first_elements)
    
print(all_sum)