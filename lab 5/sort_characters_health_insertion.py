# ECOR 1042 Lab 5 - Individual submission for sort_characters_health_insertion function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Rami Sabouni)
__author__ = "Jett Miyasaki"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101309152"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-089"

#==========================================#
# Place your sort_characters_health_insertion function after this line

def sort_characters_health_insertion(lst: list, word: str) -> list:
    """Precondition: word = 'A' or 'D', lst is a list of dictionaries
    Returns a sorted list of dictionaries based on the given ascending or descending input using the health value of each dictionary.
    """
    try: #check if the word element
        word = word.capitalize()
        for i in range(1, len(lst)):
                temp = lst[i]
                key = lst[i]['Health']
                j = i - 1
                if(word == 'A'):
                    while(j >= 0 and key < lst[j]['Health']):
                        lst[j+1] = lst[j]
                        j -= 1
                    lst[j+1] = temp
                elif(word == 'D'):
                    while(j >= 0 and key > lst[j]['Health']):
                        lst[j+1] = lst[j]
                        j -= 1
                lst[j+1] = temp
        return lst
    except KeyError:
        print("Health key not in dictionary...")
        return lst





# Do NOT include a main script in your submission
