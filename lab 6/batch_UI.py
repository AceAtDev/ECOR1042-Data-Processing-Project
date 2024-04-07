# ECOR 1042 Lab 6 - Template Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Victoria Salomon"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101324316"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-089"

#==========================================#
# Place your script for your batch_UI after this line

import load_data
import histogram
import sort

filename = input(
    "Please enter the name of the file where your commands are sorted: ")

in_file = open(filename, 'r')
lists = []

for line in in_file:
    line = line.strip().split(';')
    lists.append(line)


for one_list in lists:
    if 'L' in one_list:
        data = load_data.load_data(one_list[1], (one_list[2], one_list[3]))
    print("Data loaded")

    if "S" in one_list:
        sorted_data = sort.sort(data, one_list[1][2], one_list[1][1])
        if one_list[3] == "Y":
            print(sorted_data)
        break
    else:
        print('Data sorted')
        break

    if "H" in one_list:
        stamina = histogram.histogram(sorted_data, one_list[2][1])





