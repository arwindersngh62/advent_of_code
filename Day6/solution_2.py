from pathlib import Path
from math import sqrt,ceil,floor

data_file_path = Path(__file__).parent.resolve()/"data.txt"

with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()

print( )
time = int(all_data[0].split(":")[1].replace(" ", ""))
distance = int(all_data[1].split(":")[1].replace(" ", ""))


print(time)
print(distance)

def get_number_of_ways(total_time, distance):
    """Solve the quaratic equation : 
        t*(T-t) = distance
        
        where t = time for which the button is pressed
        T = total race time
        
        
    
    """
    discriminant = sqrt(total_time**2 - 4*distance)
    lower = (total_time - discriminant)/2
    upper = (total_time + discriminant)/2
    if int(10000*lower)%10000 == 0: # Its a check for weather the number is int 
        lower_l =  int(lower)+1
    else:
        lower_l = ceil(lower)
    if int(10000*lower)%10000 == 0:
        upper_l = int(upper)-1
    else:
        upper_l = floor(upper)
    print(lower, upper)
    print(lower_l, upper_l)
    return int(upper_l-lower_l+1)

def get_ways_brute_force(time, distance):
    ways = 0
    for speed in range(1, time+1):
        dist = (time-speed)*speed
        if dist> distance:
            ways+=1
    return ways
    
total_ways =1

num_of_ways = get_number_of_ways(time, distance)
print(num_of_ways)
total_ways*=num_of_ways
    
print(total_ways)