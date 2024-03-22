# ECOR 1042 Lab 4 - Individual submission for test3 function

#import check module here
import check

#import load_data module here
import load_data

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Jett Miyasaki"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101309152"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-089"

#==========================================#
#Do not modify the code already provided.
file = 'characters-test.csv'

def test_return_correct_dict_inside_list():

    #Complete the function with your test cases
    
    #test that character_occupation_list returns a correct dictionary inside the list (3 different test cases required)
    check.equal(list(load_data.character_occupation_list(file, 'AT')[0].keys()), list(load_data.character_occupation_list(file, 'AT')[-1].keys()))
    check.equal(list(load_data.character_occupation_list(file, 'DB')[0].keys()), list(load_data.character_occupation_list(file, 'AT')[-1].keys()))
    check.equal(list(load_data.character_occupation_list(file, 'EB')[0].keys()), list(load_data.character_occupation_list(file, 'H')[-1].keys()))
    
    #test that character_strength_list returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(list(load_data.character_strength_list(file, (5,12))[0].keys()), list(load_data.character_strength_list(file, (5,12))[-1].keys()))
    check.equal(list(load_data.character_strength_list(file, (5,12))[0].keys()), list(load_data.character_strength_list(file, (0,12))[-1].keys()))
    check.equal(list(load_data.character_strength_list(file, (10,54))[0].keys()), list(load_data.character_strength_list(file, (1,20))[-1].keys()))
    
    #test that character_luck_list returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(list(load_data.character_luck_list(file, 0.51)[0].keys()), list(load_data.character_luck_list(file, 0.51)[-1].keys()))
    check.equal(list(load_data.character_luck_list(file, 0.51)[0].keys()), list(load_data.character_luck_list(file, 0.90)[-1].keys()))
    check.equal(list(load_data.character_luck_list(file, 2.0)[0].keys()), list(load_data.character_luck_list(file, 2.0)[-1].keys()))
    
    
    #test that character_weapon_list returns a correct dictionary inside the list (3 different test cases required)

    check.equal(list(load_data.character_weapon_list(file, 'Staff')[0].keys()), list(load_data.character_weapon_list(file, 'Staff')[-1].keys())) #compare same list of dictionary
    check.equal(list(load_data.character_weapon_list(file, 'Staff')[0].keys()), list(load_data.character_weapon_list(file, 'Longsword')[-1].keys())) #compare diffents lists of dictionary
    check.equal(list(load_data.character_weapon_list(file, 'Dagger')[0].keys()), list(load_data.character_weapon_list(file, 'Club')[-1].keys())) #compare null lists of dictionary

    
    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
    check.equal(list(load_data.load_data(file, ('Occupation', 'H'))[0].keys()), list(load_data.load_data(file, ('Occupation', 'H'))[-1].keys()))
    check.equal(list(load_data.load_data(file, ('Luck', 0.8))[0].keys()), list(load_data.load_data(file, ('Luck', 0.8))[-1].keys()))
    check.equal(list(load_data.load_data(file, ('Strength', (10,54)))[0].keys()), list(load_data.load_data(file, ('Strength', (10,54)))[-1].keys()))
    check.equal(list(load_data.load_data(file, ('Occupation', 'AT'))[0].keys()), list(load_data.load_data(file, ('Occupation', 'AT'))[-1].keys()))
    check.equal(list(load_data.load_data(file, ('All', 'Axe'))[0].keys()), list(load_data.load_data(file, ('All', 'Axe'))[-1].keys()))
    check.equal(list(load_data.load_data(file, ('Weapon', 'Staff'))[0].keys()), list(load_data.load_data(file, ('Weapon', 'Staff'))[-1].keys()))
    

    
    #test that calculate_health returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(list(load_data.calculate_health([{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 5, 'Intelligence': 4, 'Luck': 0.4, 'Armor': 5}])[0].keys()), list(load_data.calculate_health([{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 5, 'Intelligence': 4, 'Luck': 0.4, 'Armor': 5}])[-1].keys()))
    check.equal(list(load_data.calculate_health([{'Occupation': 'H', 'Strength': 10, 'Agility': 3, 'Stamina': 6, 'Personality': 3, 'Intelligence': 2, 'Luck': 0.44, 'Armor': 3}])[0].keys()), list(load_data.calculate_health([{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 5, 'Intelligence': 4, 'Luck': 0.4, 'Armor': 5},{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 5, 'Intelligence': 4, 'Luck': 0.4, 'Armor': 5}])[-1].keys()))
    check.equal(list(load_data.calculate_health(load_data.load_data(file, ('Occupation','H')))[0].keys()), list(load_data.calculate_health(load_data.load_data(file, ('Occupation','H')))[-1].keys()))
    
    check.summary()
# Do NOT include a main script in your submission
