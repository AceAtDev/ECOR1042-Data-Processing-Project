# ECOR 1042 Lab 4 - Individual submission for test4 function

#import check module here
import check
#import load_data module here
import test_load_data
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = ""

# Update "" with your student number (e.g., 100100100)
__student_number__ = ""

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = ""

#==========================================#
#Do not modify the code already provided.

def test_calculate_health():
    """Test calculate_health with various scenarios."""
    # Test data
    test_data = [
        [{'Occupation': 'Knight', 'Luck': 7, 'Strength': 10, 'Weapon': 'Sword'}],
        [{'Occupation': 'Mage', 'Luck': 5, 'Strength': 8, 'Weapon': 'Staff'}],
        [{'Occupation': 'Rogue', 'Luck': 9, 'Strength': 6, 'Weapon': 'Dagger'}],
    ]

    # Test case 1: calculate_health should not change the size of the list.
    original_size = len(test_data)
    calculate_health(test_data)
    check.equal(len(test_data), original_size, "Test 1: List size should remain the same")

    # Test case 2: The number of keys in each dictionary should increase only by one
    for character in test_data:
        check.equal(len(character), 5, "Test 2: Number of keys should increase by one")

    # Test case 3: The value for Health should be properly calculated.
    # Assuming the health calculation formula here. Replace it with the actual formula.
    for character in test_data:
        expected_health = character['Luck'] * character['Strength']  # Replace with actual formula
        check.equal(character['Health'], expected_health, "Test 3: Health should be properly calculated")

    # Test cases for missing keys
    missing_keys_data = [
        [{'Luck': 7, 'Strength': 10, 'Weapon': 'Sword'}],  # Missing 'Occupation'
        [{'Occupation': 'Knight', 'Strength': 10, 'Weapon': 'Sword'}],  # Missing 'Luck'
        [{'Occupation': 'Knight', 'Luck': 7, 'Weapon': 'Sword'}],  # Missing 'Strength'
        [{'Occupation': 'Knight', 'Luck': 7, 'Strength': 10}],  # Missing 'Weapon'
        [{'Occupation': 'Knight', 'Luck': 7, 'Strength': 10, 'Weapon': 'Sword'}],  # All keys present
    ]

    for i, character in enumerate(missing_keys_data, start=4):
        original_size = len(character)
        calculate_health(character)
        check.equal(len(character), original_size + 1, f"Test {i}: Number of keys should increase by one")
        # Assuming the health calculation formula here. Replace it with the actual formula.
        expected_health = character.get('Luck', 0) * character.get('Strength', 0)  # Replace with actual formula
        check.equal(character['Health'], expected_health, f"Test {i}: Health should be properly calculated")

    # Test case for empty list
    empty_list = []
    calculate_health(empty_list)
    check.equal(len(empty_list), 0, "Test 9: Empty list should remain empty")

    check.summary()
    #Complete the function with your test cases
    
    #test that the function does not change the lenght of the list provided as input parameter (5 different test cases required)
    
    #test that the function returns an empty list when it is called whith an empty list
    
    
    #test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)
    
    
    #test that the Health value is properly calculated  (5 different test cases required)
    
    
   
    
    check.summary()


# Do NOT include a main script in your submission
