# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Mohamed Elshoubky, Jett Miyasaki, Rehma Muzammil, Victoria Salomon"

# Update "" with your team (e.g. T102)
__team__ = "T089"


# ==========================================#
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
# ==========================================#
# Place your character_strength_list function after this line
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


# ==========================================#
# Place your character_luck_list function after this line
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


# ==========================================#
# Place your character_weapon_list function after this line
def character_weapon_list(file_name: str, weapon_type) -> list:
    """
    Returns a filtered list of characters based on their weapon
    """

    try:
        new_list = []  # empty list

        with open(file_name, 'r') as f:

            # get info of weapon category from first line
            read = f.readlines()
            header = read[0].strip().split(',')
            index = header.index('Weapon')

            # list comprehension
            for i in read[1:]:  # loop through all lines, except first
                line = i.strip().split(',')
                weapon_list = {}  # dictionary for selected weapon

                if line[index] == weapon_type:  # if the read line contains the weapon indicated

                    for j, h in enumerate(header):

                        if (h == 'Occupation'):
                            weapon_list[h] = str(line[j])
                        if h in ('Strength', 'Agility', 'Stamina', 'Personality', 'Intelligence',
                                 'Armor'):  # convert data type for each title
                            weapon_list[h] = int(line[j])
                        if (h == 'Luck'):
                            weapon_list[h] = float(line[j])

                    # insert selected data to new list
                    new_list.append(weapon_list)

            return new_list
    except FileNotFoundError:  # returns an empty list if file cannot be found
        print("File not Found.")
        return []


# ==========================================#
# Place your load_data function after this line
def load_data(file_name: str, filter_tuple):
    """
    Loads character data based on specified attribute and value.


    """
    try:
        # Assuming the data is stored in a CSV file with headers
        with open(file_name, 'r') as file:
            lines = file.readlines()
            headers = lines[0].strip().split(',')

            # Validate the filter_tuple
            if filter_tuple[0] not in headers:
                print("Invalid Value")
                return []

            # Initialize an empty list to store filtered characters
            filtered_characters = []

            # Process each line (character entry) in the file
            for line in lines[1:]:
                character_data = line.strip().split(',')
                character_dict = {}

                # Create a dictionary for this character
                for i, header in enumerate(headers):
                    if header != filter_tuple[0]:
                        # Convert relevant attributes to integers if needed
                        if header in ['Strength', 'Agility', 'Stamina', 'Intelligence', 'Personality', 'Armor']:
                            character_dict[header] = int(character_data[i])
                        else:
                            character_dict[header] = character_data[i]

                # Check if the filter condition matches
                if filter_tuple[0] == 'All' or character_dict.get(filter_tuple[0]) == filter_tuple[1]:
                    filtered_characters.append(character_dict)

            return filtered_characters

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []


# ==========================================#
# Place your calculate_health function after this line
def calculate_health(characters: list) -> list:
    """
    Calculates the health of characters based on the provided formula.

    """
    for character in characters:
        # Extract relevant attributes
        strength = character.get('Strength', 0)
        agility = character.get('Agility', 0)
        stamina = character.get('Stamina', 0)
        personality = character.get('Personality', 0)
        intelligence = character.get('Intelligence', 0)
        luck = character.get('Luck', 0)
        armor = character.get('Armor', 0)

        # Calculate health using the formula
        base_health = strength + agility + stamina + personality + intelligence
        luck_health = armor ** 2 * luck
        total_health = base_health + luck_health

        # Add the health attribute to the character dictionary
        character['Health'] = round(total_health, 2)  # Rounded to 2 decimal places

    return characters

# Do NOT include a main script in your submission
