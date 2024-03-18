# ECOR 1042 Lab 3 - Individual submission for character_weapon_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Jett Miyasaki"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101309152"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T089"

#==========================================#
# Place your character_weapon_list function after this line

import string #import string library

def character_weapon_list(file_name, weapon_type) -> list:
    """
    Returns a filtered list of characters based on their weapon
    """
    
    try:
        new_list = [] #empty list

        with open(file_name, 'r') as f:
            
            #get info of weapon category from first line
            read = f.readlines()
            header = read[0].strip().split(',')
            index = header.index('Weapon')

            

            #list comprehension
            for i in read[1:]: #loop through all lines, except first
                line = i.strip().split(',')
                weapon_list = {} #dictionary for selected weapon

                if line[index] == weapon_type: #if the read line contains the weapon indicated
                    
                    for j, h in enumerate(header):
                        
                        if(h == 'Occupation'):
                            weapon_list[h] = str(line[j])
                        if h in('Strength','Agility','Stamina','Personality','Intelligence','Armor'): #convert data type for each title
                            weapon_list[h] = int(line[j])
                        if(h == 'Luck'):
                            weapon_list[h] = float(line[j])

                    #insert selected data to new list
                    new_list.append(weapon_list)

            return new_list
    except FileNotFoundError: #returns an empty list if file cannot be found
        print("File not Found.")
        return []