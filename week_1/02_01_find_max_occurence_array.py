def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for i in range(len(string)):
        if string[i].isalpha():
            array_index = ord(string[i]) - 97
            alphabet_occurrence_array[array_index] += + 1

    max_num_index = 0
    for i in range(1, len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[i] > alphabet_occurrence_array[max_num_index]:
            max_num_index = i
    most_occur = chr(max_num_index + 97)
    return most_occur


print(find_alphabet_occurrence_array("hello my name is sparta"))
