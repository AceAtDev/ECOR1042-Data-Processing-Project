# ECOR 1042 Lab 3 - Individual submission for character_luck_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Mohamed Elshoubky"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101306451"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T089"

# ==========================================#
# Place your character_luck_list function after this line

import string


def character_luck_list(name_of_the_file: str, luck_limit: float) -> list[dict]:
    """
    Filters characters based on luck value.
    Returns a list of the occupation with a threshold of luck

    >>> character_data("xxx.file", 50)
    ...
    >>> character_data("xxx.file", 20)
    ...
    >>> character_data("xxx.file", 31)
    ...
    """
    try:
        with open(name_of_the_file, 'r') as file:
            lines = file.readlines()
            headers = lines[0].strip().split(',')
            luck_index = headers.index('Luck')

            # Initialize an empty list to store filtered characters
            filtered_characters = []

            # Process each line (character entry) in the file
            for line in lines[1:]:
                character_data = line.strip().split(',')
                luck_value = float(character_data[luck_index])

                # Check if luck value is less than the threshold
                if luck_value < luck_limit:
                    # Create a dictionary for this character
                    character_dict = {}
                    for i, header in enumerate(headers):
                        if header != 'Luck':
                            # Convert relevant attributes to integers
                            if header in ['Strength', 'Agility', 'Stamina', 'Intelligence', 'Personality', "Armor"]:
                                # assuming attributs will always be int
                                character_dict[header] = int(character_data[i])
                            else:
                                character_dict[header] = character_data[i]

                    # Append the character dictionary to the filtered list
                    filtered_characters.append(character_dict)

            return filtered_characters



    except FileExistsError:
        print(f"{name_of_the_file} was not found, Please make sure you have inserted the correct file name and/or"
              f"the file is with the function's folder")
        return []
