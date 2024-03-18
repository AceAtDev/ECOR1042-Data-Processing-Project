# ECOR 1042 Lab 3 - Individual submission for character_occupation_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Victoria Salomon"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101324316"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-089"

#==========================================#
# Place your character_occupation_list function after this line


def character_occupation_list(file_name: str, occupation: str) -> list[dict]:
    """Return the list of characters given certain occupation.
    >>>character_occupation_list('character-mat.csv', 'AT')
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}, ...]
    >>>character_ocupation_list('character-mat.csv', 'XXXX')
    []
    >>>character_ocupation_list('character-mat.csv', 'H')
    [{'Strength': 16, 'Agility': 12, 'Stamina': 3, 'Personality': 6, 'Intelligence': 15, 'Luck': 0.22, 'Armor': 11, 'Weapon': 'Dagger'}, ...]
    """

    with open(file_name, "r") as inp_file:
        header_line = True
        player_list = []

        for line in inp_file:
            row = line.strip().split(',')

            if header_line:
                keys = row
                header_line = False

            else:
                if row[0] == occupation:
                    row_dict = {}
                    row_dict[keys[1]] = int(row[1])
                    row_dict[keys[2]] = int(row[2])
                    row_dict[keys[3]] = int(row[3])
                    row_dict[keys[4]] = int(row[4])
                    row_dict[keys[5]] = int(row[5])
                    row_dict[keys[6]] = float(row[6])
                    row_dict[keys[7]] = int(row[7])
                    row_dict[keys[8]] = row[8]
                    player_list.append(row_dict)

    inp_file.close()
    return player_list


# Do NOT include a main script in your submission
