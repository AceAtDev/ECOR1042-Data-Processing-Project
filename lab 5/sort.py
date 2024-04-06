# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Mohamed Elshoubky, Jett Miyasaki, Rehma Muzammil, Victoria Salomon"

# Update "" with your team (e.g. T102)
__team__ = "T-089"


# ==========================================#
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


# ==========================================#
# Place your sort_characters_intelligence_selection function after this line
def sort_characters_intelligence_selection(characters: list, order: str) -> list:
    """
    Retruns a list of character depending on Intelligence via Selection sort

    >>>sort_characters_intelligence_selection("X", "A")
    ...
    >>>sort_characters_intelligence_selection("X", "D")
    ...
    >>>sort_characters_intelligence_selection("X", "A")
    ...
    """

    if all('Intelligence' in character for character in characters):

        for i in range(len(characters)):
            min_index = i

            for j in range(i + 1, len(characters)):

                if ((order == "A" and characters[j]['Intelligence'] < characters[min_index]['Intelligence']) or
                        (order == "D" and characters[j]['Intelligence'] > characters[min_index]['Intelligence'])):
                    min_index = j

            characters[i], characters[min_index] = characters[min_index], characters[i]

        return characters

    else:
        print('"Intelligence" key is not present')
        return characters


#

# ==========================================#
# Place your sort_characters_health_insertion function after this line
def sort_characters_health_insertion(lst: list, word: str) -> list:
    """Precondition: word = 'A' or 'D', lst is a list of dictionaries
    Returns a sorted list of dictionaries based on the given ascending or descending input using the health value of each dictionary.
    """
    try:  # check if the word element
        word = word.capitalize()
        for i in range(1, len(lst)):
            temp = lst[i]
            key = lst[i]['Health']
            j = i - 1
            if (word == 'A'):
                while (j >= 0 and key < lst[j]['Health']):
                    lst[j + 1] = lst[j]
                    j -= 1
                lst[j + 1] = temp
            elif (word == 'D'):
                while (j >= 0 and key > lst[j]['Health']):
                    lst[j + 1] = lst[j]
                    j -= 1
            lst[j + 1] = temp
        return lst
    except KeyError:
        print("Health key not in dictionary...")
        return lst


# ==========================================#
# Place your sort_characters_armor_bubble function after this line
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


# ==========================================#
# Place your sort function after this line
def sort(dic: list, order: str, method: str):
    method = method.lower()
    order = order.capitalize()

    if method != "armor" and method != "health" and method != "intelligence" and method != "agility":
        print(f"Cannot be sorted by “{method}”, where {method} is the value of the 3rd input parameter")
        return dic

    if method == "armor":
        return sort_characters_armor_bubble(dic, order)
    if method == "health":
        return sort_characters_health_insertion(dic, order)
    if method == "intelligence":
        return sort_characters_intelligence_selection(dic, order)
    return sort_characters_agility_bubble(dic, order)
# Do NOT include a main script in your submission
