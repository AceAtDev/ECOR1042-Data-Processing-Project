# ECOR 1042 Lab 4 - Individual submission for test1 function

import check
import load_data

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Victoria Salomon"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101324316"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-089"


# ==========================================#
# Do not modify the code already provided.

def test_return_list():

    filename = 'characters-test.csv'
    # Complete the function with your test cases

    # test that character_occupation_list returns a list (3 different test cases required)
    check.equal(isinstance(
        load_data.character_occupation_list(filename, 'AT'), list), True)
    check.equal(isinstance(
        load_data.character_occupation_list(filename, 'EB'), list), True)
    check.equal(isinstance(
        load_data.character_occupation_list(filename, 'X'), list), True)

    # test that character_strength_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.character_strength_list(
        filename, (9, 20)), list), True)
    check.equal(isinstance(load_data.character_strength_list(
        filename, (8, 10)), list), True)
    check.equal(isinstance(load_data.character_strength_list(
        filename, (0, 7)), list), True)

    # test that character_luck_list returns a list (3 different test cases required)
    check.equal(isinstance(
        load_data.character_luck_list(filename, 0.8), list), True)
    check.equal(isinstance(
        load_data.character_luck_list(filename, 0.4), list), True)
    check.equal(isinstance(
        load_data.character_luck_list(filename, 0), list), True)

    # test that character_weapon_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.character_weapon_list(
        filename, 'Dagger'), list), True)
    check.equal(isinstance(load_data.character_weapon_list(
        filename, 'Short sword'), list), True)
    check.equal(isinstance(
        load_data.character_weapon_list(filename, 'X'), list), True)

    # test that load_data returns a list (6 different test cases required)
    check.equal(isinstance(load_data.load_data(
        filename, ('Occupation', 'H')), list), True)
    check.equal(isinstance(load_data.load_data(
        filename, ('Weapon', 'Handaxe')), list), True)
    check.equal(isinstance(load_data.load_data(
        filename, ('Strength', (8, 16))), list), True)
    check.equal(isinstance(load_data.load_data(
        filename, ('Luck', 0.5)), list), True)
    check.equal(isinstance(load_data.load_data(
        filename, ('X', '...')), list), True)
    check.equal(isinstance(load_data.load_data(
        filename, ('All', '...')), list), True)

    # test that calculate_health returns a list (3 different test cases required)
    check.equal(isinstance(load_data.calculate_health(
        load_data.load_data(filename, ('Weapon', 'Dagger'))), list), True)
    check.equal(isinstance(load_data.calculate_health(
        load_data.load_data(filename, ('Occupation', 'HG'))), list), True)
    check.equal(isinstance(load_data.calculate_health(
        load_data.load_data(filename, ('X', '...'))), list), True)

    check.summary()

# Do NOT include a main script in your submission
