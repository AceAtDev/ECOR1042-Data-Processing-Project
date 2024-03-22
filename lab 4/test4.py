# ECOR 1042 Lab 4 - Individual submission for test4 function

# import check module here
import check
import load_data as ld

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Mohamed Elshoubky"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101306451"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T089"


# ==========================================#
# Do not modify the code already provided.

def test_calculate_health():
    """Test calculate_health with various scenarios."""

    file_name = "characters-test.csv"
    data = ld.load_data(file_name, ("All", "All"))

    # Complete the function with your test cases

    # test that the function does not change the lenght of the list provided as input parameter (5 different test cases required)
    occ_data = ld.character_occupation_list(file_name, "AT")
    occ_expected = len(occ_data)
    check.equal(len(ld.calculate_health(occ_data)), occ_expected, f"List size ({len(occ_data)} != {occ_expected}")

    luck_data = ld.character_luck_list(file_name, 0.5)
    try:
        hd = ld.calculate_health(luck_data)
        # check.equal(len(ld.calculate_health(luck_data)), luck_expected, f"List size ({len(luck_data)}) != {luck_expected}")
    except:
        # pass the test
        check.equal(True, True)
    else:
        # fail the test
        check.equal(False, True)

    str_data = ld.character_strength_list(file_name, (4, 10))
    try:
        sd = ld.calculate_health(str_data)
    except:
        # pass the test
        check.equal(True, True)
    else:
        # fail the test
        check.equal(False, True)

    weapon_data = ld.character_weapon_list(file_name, 4)
    weapon_expected = len(weapon_data)
    check.equal(len(ld.calculate_health(weapon_data)), weapon_expected,
                f"List size ({len(weapon_data)}) != {weapon_expected}")

    all_data = ld.load_data(file_name, ("All", "All"))
    all_expected = len(ld.load_data(file_name, ("All", "All")))
    check.equal(len(ld.calculate_health(all_data)), all_expected, f"List size ({len(all_data)}) != {all_expected}")

    #
    #
    # test that the function returns an empty list when it is called whith an empty list
    check.equal(len(ld.calculate_health([])), 0, "List size != 0 ; list is not empty")

    #
    #
    # test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different
    # test cases required)


    #
    #
    # test that the Health value is properly calculated  (5 different test cases required)
    health_list = ld.calculate_health(all_data)


    check.summary()



# Do NOT include a main script in your submission
