# ECOR 1042 Lab 5 - Individual submission for sort_characters_intelligence_selection function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Rami Sabouni)
__author__ = "Mohamed Elshoubky"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101306451"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-89"


# ==========================================#
# Place your sort_characters_intelligence_selection function after this line
def sort_characters_intelligence_selection(characters: list, order: str) -> list:
    """
    Retruns a list of character depending on Intelligence via Selection sort

    >>>sort_characters_intelligence_selection("X", "A")
    ...
    >>>sort_characters_intelligence_selection("X", "D")
    ...
    >>>sort_characters_intelligence_selection("X", "A")
    ...
    """

    if all('Intelligence' in character for character in characters):

        for i in range(len(characters)):
            min_index = i

            for j in range(i + 1, len(characters)):

                if ((order == "A" and characters[j]['Intelligence'] < characters[min_index]['Intelligence']) or
                        (order == "D" and characters[j]['Intelligence'] > characters[min_index]['Intelligence'])):
                    min_index = j

            characters[i], characters[min_index] = characters[min_index], characters[i]

        return characters

    else:
        print('"Intelligence" key is not present')
        return characters

# Do NOT include a main script in your submission
