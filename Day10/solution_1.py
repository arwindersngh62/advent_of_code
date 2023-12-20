from pathlib import Path
from numpy import diff, abs


data_file_path = Path(__file__).parent.resolve()/"data.txt"

with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()