# ECOR 1042 Lab 5 - Individual submission for sort_characters_agility_bubble function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Rami Sabouni)
__author__ = "Victoria Salomon"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101324316"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-089"

#==========================================#
# Place your sort_characters_agility_bubble function after this line


def sort_characters_agility_bubble(dictionaries: list, order: str) -> list:
    """Return a sorted list if "Agility" is a key in the dictionary given a determined order.

    No preconditions. 

    >>>sort_characters_agility_bubble([{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}], "A")
    [{'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB', 'Agility': 13}]
    >>>sort_characters_agility_bubble([{'Occupation': 'EB'}, {'Occupation': 'M'}], "A")
    "Agility" key is not present.
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]
    >>>sort_characters_agility_bubble([{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}], "D")
    [{'Occupation': 'H', 'Agility': 13}, {'Occupation': 'EB', 'Agility': 11}]
    """
    for dictionary in dictionaries:
        for key in dictionary:
            if 'Agility' not in dictionary:
                print('"Agility" key is not present.')
                return dictionaries

            else:

                if order == "A":

                    swap = True
                    while swap:
                        swap = False
                        for i in range(len(dictionaries) - 1):
                            if dictionaries[i]['Agility'] > dictionaries[i + 1]['Agility']:
                                aux = dictionaries[i]
                                dictionaries[i] = dictionaries[i + 1]
                                dictionaries[i + 1] = aux
                                swap = True

                elif order == "D":
                    swap = True
                    while swap:
                        swap = False
                        for i in range(len(dictionaries) - 1):
                            if dictionaries[i]['Agility'] < dictionaries[i + 1]['Agility']:
                                aux = dictionaries[i]
                                dictionaries[i] = dictionaries[i + 1]
                                dictionaries[i + 1] = aux
                                swap = True

    return dictionaries


# Do NOT include a main script in your submission
