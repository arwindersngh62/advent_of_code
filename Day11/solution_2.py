from pathlib import Path
from numpy import diff, abs
from itertools import combinations
from copy import deepcopy


data_file_path = Path(__file__).parent.resolve() / "data.txt"

with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()
all_cols = []
for _ in range(len(all_data[0])):
    all_cols.append([])

count = 0
expanded_rows_index = []
galaxy_indices = []
for data in all_data:
    if "#" not in data:
        expanded_rows_index.append(count)
    else:
        galaxy_indices+=[[count_,count] for count_ in range(len(data)) if data[count_] == "#"]
    data_list = list(data)
    for i in range(len(data)):
        all_cols[i].append(data_list[i])
    count+=1
col_count = 0
expanded_column_index = []

for data in all_cols:
    if "#" not in data:
        expanded_column_index.append(col_count)
    col_count+=1
print(galaxy_indices) 
print(expanded_column_index[:-1])
print(expanded_rows_index)
expanded_galaxy = deepcopy(galaxy_indices)
for row in expanded_rows_index:
    for ind in range(len(galaxy_indices)):
        if  galaxy_indices[ind][1] < row:
            continue
        else:
            expanded_galaxy[ind][1]+=999999

for column in expanded_column_index[:-1]:
    for ind in range(len(galaxy_indices)):
        if galaxy_indices[ind][0] < column:
            continue
        else:
            expanded_galaxy[ind][0]+=999999
print(expanded_galaxy)
print(galaxy_indices)
paired = combinations(expanded_galaxy, 2)
total_sum = 0
for value in paired:
    distance = abs(value[0][0]-value[1][0])+abs(value[0][1]-value[1][1])
    #print(value, distance)
    total_sum+=float(distance)
print(total_sum)