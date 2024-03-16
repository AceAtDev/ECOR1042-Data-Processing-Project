# ECOR 1042 Lab 3 - Individual submission for character_strength_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Rehma Muzammil"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101268686"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T89"


# ==========================================#
# Place your character_strength_list function after this line
# ==========================================#
def character_strength_list(file_name: str, strength_range: tuple[int, int]) -> list[dict]:
    """ 
    Return a list of characters in the form of a dictionary whose strength is what is provided in the parameter.
    Return empty list if range of strength does not meet parameters.
    The dictionary keys include every attribute except strength 
    
    Preconditions: 
    Data given has no errors and has the "characters-mat.csv" format.
    strength_range input must be in the format: tuple[int, int]
    Output data has   ['Occupation', 'Strength', 'Agility', 'Stamina', 'Personality', 'Intelligence', 'Luck', 'Armor', 'Weapon']
    
    Examples: 
    >>>character_strength_list ('characters-mat.csv', (10, 20))
    [{'Occupation': 'AT', 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}],
    {other element},
    …
    ]
    >>>character_strength_list ('characters-mat.csv', (2000, 20000))
    [] #empty string is the output
    >>>character_strength_list ((10, 20))
    Traceback (most recent call last):
      Python Shell, prompt 11, line 1
    builtins.TypeError: character_strength_list() missing 1 required positional argument: 'strength_range'
    
    """

    final_list = []
    in_file = open(file_name, 'r')
    count = 0

    strength_dict = {}
    for line in in_file:
        line = line.replace("\n", "").split(",")
        if count == 0:
            titles = line
            count += 1

        else:
            strength_dict = {}
            strength_dict[titles[0]] = line[0]
            strength_dict[titles[2]] = int(line[2])
            strength_dict[titles[3]] = int(line[3])
            strength_dict[titles[4]] = int(line[4])
            strength_dict[titles[5]] = int(line[5])
            strength_dict[titles[6]] = float(line[6])
            strength_dict[titles[7]] = int(line[7])
            strength_dict[titles[8]] = (line[8])

            if strength_range[0] <= int(line[1]) <= strength_range[1]:
                final_list.append(strength_dict)

    in_file.close()
    return final_list
