# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Mohamed Elshoubky"

# Update "" with your team (e.g. T102)
__team__ = "T089"


#==========================================#
# Place your character_occupation_list function after this line


#==========================================#
# Place your character_strength_list function after this line


#==========================================#
# Place your character_luck_list function after this line
def character_luck_list(name_of_the_file: str, luck_limit: float) -> list[dict]:
    """
    Filters characters based on luck value.

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


#==========================================#
# Place your character_weapon_list function after this line


#==========================================#
# Place your load_data function after this line


#==========================================#
# Place your calculate_health function after this line
def calculate_health(characters):
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
