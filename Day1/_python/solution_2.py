from pathlib import Path

data_file_path = Path(__file__).parent.parent.resolve()/"data_file.txt"

def join_numbers_list(numbers_list):
    temp_num = ""
    temp_num = numbers_list[0] + numbers_list[-1]
    return int(temp_num)


all_digits_list = []

def check_and_return_lowest_index(datum, word, digit):
    lowest_word_index = datum.find(word)
    lowest_digit_index = datum.find(digit)
    if lowest_word_index + lowest_digit_index <-2:
        return -1
    if lowest_word_index == -1:
        return lowest_digit_index
    if lowest_digit_index == -1:
        return lowest_word_index
    return min(lowest_word_index, lowest_digit_index)
            
def check_and_return_highest_index(datum, word, digit):
    highest_word_index = datum.rfind(word)
    highest_digit_index = datum.rfind(digit)
    if highest_word_index + highest_digit_index <-2:
        return -1
    if highest_word_index == -1:
        return highest_digit_index
    if highest_digit_index == -1:
        return highest_word_index
    return max(highest_word_index, highest_digit_index)

numbers_to_words = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9",
    "zero":"0"
}



with open(data_file_path, "r") as data_file:
    all_data = data_file.readlines()
    numbers_list = []
    
    for datum in all_data:
        lowest_index = -1
        lowest_digit = ""
        highest_index = -1
        highest_digit = ""
        for word,digit in numbers_to_words.items():
            temp_lowest_index = check_and_return_lowest_index(datum, word, digit)
            temp_highest_index = check_and_return_highest_index(datum, word, digit)
            if temp_lowest_index != -1:
                if lowest_index != -1:
                    if lowest_index > temp_lowest_index:
                        lowest_index = temp_lowest_index
                        lowest_digit = digit
                else:
                    lowest_index = temp_lowest_index
                    lowest_digit = digit
            if temp_highest_index != -1:
                if highest_index != -1:
                    if highest_index < temp_highest_index:
                        highest_index = temp_highest_index
                        highest_digit = digit
                else:
                    highest_index = temp_highest_index
                    highest_digit = digit
            

        numbers_list.append(int(lowest_digit+highest_digit))
        
print(sum(numbers_list))
