# ECOR 1042 Lab 4 - Individual submission for test2 function

import check 
import load_data 


# from load_data import character_occupation_list

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Rehma Muzammil"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101268686"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "89"


# ==========================================#
# Do not modify the code already provided.

def test_return_list_correct_length():
    # Complete the function with your test cases

    # test that character_occupation_list returns a list with the correct length (3 different test cases required)
    check.equal(len(load_data.character_occupation_list('characters-test.csv', "EB")), 4)
    check.equal(len(load_data.character_occupation_list('characters-test.csv', "DD")), 0)
    check.equal(len(load_data.character_occupation_list('characters-test.csv', "HG")), 4)
    # test that character_strength_list returns a list with the correct length (3 different test cases required)
    check.equal(len(load_data.character_strength_list('characters-test.csv', (8, 9))), 2)
    check.equal(len(load_data.character_strength_list('characters-test.csv', (8, 20))), 26)
    check.equal(len(load_data.character_strength_list('characters-test.csv', (100, 200))), 0)
    # test that character_luck_list returns a list with the correct length (3 different test cases required)
    check.equal(len(load_data.character_luck_list('characters-test.csv', 0.64)), 13)
    check.equal(len(load_data.character_luck_list('characters-test.csv', 0)), 0)
    check.equal(len(load_data.character_luck_list('characters-test.csv', 0.77)), 20)
    # test that character_weapon_list returns a list with the correct length(3 different test cases required)
    check.equal(len(load_data.character_weapon_list('characters-test.csv', "Dagger")), 5)
    check.equal(len(load_data.character_weapon_list('characters-test.csv', "Gun")), 0)
    check.equal(len(load_data.character_weapon_list('characters-test.csv', "Short sword")), 2)
    # test that load_data returns a list with the correct length (6 different test cases required)
    check.equal(len(load_data.load_data('characters-test.csv', ("Weapon", "Club"))), 5)
    check.equal(len(load_data.load_data('characters-test.csv', ("Occupation", "AT"))), 3)
    check.equal(len(load_data.load_data('characters-test.csv', ("Weapon", "Bomb"))), 0)
    check.equal(len(load_data.load_data('characters-test.csv', ("Occupation", "WA"))), 5)
    check.equal(len(load_data.load_data('characters-test.csv', ("Luck", 0.39))), 0)
    check.equal(len(load_data.load_data('characters-test.csv', ("Strength", (8, 9)))), 2)
    # test that calculate_health returns a list with the correct length (3 different test cases required)
    check.equal(len(load_data.calculate_health(load_data.load_data('characters-test.csv', ('Occupation','')))), 0)
    check.equal(len(load_data.calculate_health([{'Strength': 9, 'Agility': 7, 'Stamina': 9, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.33, 'Armor': 0.61, 'Weapon': 'Handaxe'}])), 1)
    check.equal(len(load_data.calculate_health([{'Strength': 0, 'Agility': 9, 'Stamina': 9, 'Personality': 5, 'Intelligence': 11, 'Luck': 0.33, 'Armor': 13, 'Weapon': 'Sword'}])), 1)
    
    check.summary()

# Do NOT include a main script in your submission
