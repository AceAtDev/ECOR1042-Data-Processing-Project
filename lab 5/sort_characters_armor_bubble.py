# ECOR 1042 Lab 5 - Individual submission for sort_characters_armor_bubble
# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Rami Sabouni)
__author__ = "Rehma Muzammil"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101268686"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "089"

#==========================================#
# Place your sort_characters_armor_bubble function after this line


# Do NOT include a main script in your submission


def sort_characters_armor_bubble(dictionaries: list, order: str) -> list:
    """Return a list that is sorted in either ascending or descending order
    if the 'Armor' key is present in the dictionary
    
    Docstring examples: 
    >>>sort_characters_armor_bubble([{'Occupation': 'EB','Armor': 11}, {'Occupation': 'H', 'Armor': 10}], "D")
    [{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}]
    >>>sort_characters_armor_bubble([{'Occupation': 'AT','Armor': 11}, {'Occupation': 'WA', 'Armor': 10}], "A")
    [{'Occupation': 'WA', 'Armor': 10}, {'Occupation': 'AT', 'Armor': 11}]
    >>>sort_characters_armor_bubble([{'Occupation': 'EB'}, {'Occupation': 'M'}], "D")
    "Armor" key is not present.
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]
    """
    for dictionary in dictionaries:
        for key in dictionary:
            if 'Armor' not in dictionary:
                print('"Armor" key is not present.')
                return dictionaries
            else: 
                
                if order == "A":
                    
                    swap = True
                    while swap:
                        swap = False
                        for i in range(len(dictionaries) - 1):
                            if dictionaries[i]['Armor'] > dictionaries[i + 1]['Armor']:
                                aux = dictionaries[i]
                                dictionaries[i] = dictionaries[i + 1]
                                dictionaries[i + 1] = aux 
                                swap = True 
                                
                elif order == "D":
                    swap = True
                    while swap:
                        swap = False
                        for i in range(len(dictionaries) - 1):
                            if dictionaries[i]['Armor'] < dictionaries[i + 1]['Armor']:
                                aux = dictionaries[i]
                                dictionaries[i] = dictionaries[i + 1]
                                dictionaries[i + 1] = aux 
                                swap = True
                                
    return dictionaries
