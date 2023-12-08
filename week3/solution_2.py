from pathlib import Path
import itertools

data_file_path = Path(__file__).parent.resolve()/"data.txt"
special_characters = "!@#$%^&*()-+?_=,<>/"

def get_number_and_indices(line):
    """Return all the numbers found in the string and all the their surrounding indices

    Returns:
        List: Contains a tuple of form
        (number, (tuple of adjacent rows), (tuple of adjacent columns))
    """
    temp_num = ""
    number = ""
    column_id =0
    collecting_num = False
    final_list = []
    for letter in line:
        if letter.isdigit():
            if not collecting_num:
                collecting_num=True
                lower_id = column_id-1
            temp_num+=letter
        else:
            if collecting_num:
                number = temp_num
                temp_num = ""
                final_list.append((number,lower_id, column_id))
                collecting_num = False
        column_id+=1
        
    return final_list
        
def generate_full_indices(tuple_index_limits):
    number = tuple_index_limits[0]
    columns = tuple_index_limits[1]
    rows = tuple_index_limits[2]
    row_list = [rows[0], rows[1]]
    columns_list = list(range(columns[0], columns[1]+1))
    all_coords = list(itertools.product(columns_list, row_list))
    extras = ((columns[0],rows[0]+1),(columns[1], rows[0]+1))
    all_coords+=extras
    return (number, all_coords)

def get_symbol_indices(line):
    column = 0
    all_symbol = [] 
    for letter in line:
        if letter in special_characters:
            all_symbol.append((letter, column))
        column+=1
    return all_symbol
      
      
def get_part_numbers(all_chars, all_symbols):
    total_sum = 0
    all_parts = 0
    for number_tuple in all_chars:
        number = number_tuple[0]
        surrounding_coords = number_tuple[1]
        for surrounding_coord in surrounding_coords:
            if surrounding_coord in all_symbols:
                total_sum+=int(number)
    print(total_sum)
                
with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()
    row_num = 0
    all_chr_list = []
    all_symbol_coords = []
    for datum in all_data:
        temp_num_and_rows = get_number_and_indices(datum)
        symbol_coords = get_symbol_indices(datum)
        if len(symbol_coords)>0:
            for item in symbol_coords:
                column = item[1]
                all_symbol_coords.append((column, row_num))
        if len(temp_num_and_rows)>0:
            low_row = row_num-1
            high_row =  row_num+1
            for item in temp_num_and_rows:
                full_tuple = (item[0],(item[1], item[2]),(low_row, high_row))
                full_coords = generate_full_indices(full_tuple)
                all_chr_list.append(full_coords)
        row_num+=1
    get_part_numbers(all_chr_list, all_symbol_coords)
    #print(all_chr_list, all_symbol_coords)