# ECOR 1042 Lab 6 - Template for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Rehma Muzammil"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101268686"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T089"

#==========================================#
# Place your curve_fit function after this line


# Do NOT include a main script in your submission

import numpy as np

def curve_fit(data: list[dict], attribute: str, n: int) -> str:
    """
    Return the equation of a curve that best fits the average of health
    Preconditions:
    The dictonaries must already contain the "Health" key and the order must be between 1 and 5
    """
    info_list = {}

    for i in data:
        if i[attribute] not in info_list.keys():
            info_list[i[attribute]] = [i["Health"]]
        else:
            info_list[i[attribute]].append(i["Health"])

    x = []
    y = []
    for key, values in info_list.items():
        avg_health = sum(values) / len(values)
        x.append(key)
        y.append(avg_health)

    x = np.array(x)
    y = np.array(y)

    if len(x) > n + 1:
        degree = n
    else:
        degree = len(x) - 1

    coeffs = np.polyfit(x, y, degree)
    equation = "y = "
    for i in range(degree, -1, -1):
        coef = round(coeffs[degree - i], 2)
        if coef != 0:
            if i == 0:
                equation += f"{coef}"
            elif i == 1:
                equation += f"{coef}x + "
            else:
                equation += f"{coef}x^{i} + "

    return equation.rstrip(' + ')
