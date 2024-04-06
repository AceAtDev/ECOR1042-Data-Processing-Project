# ECOR 1042 Lab 6 - Template submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Mohamed Elshoubky"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101306451"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-089"

#==========================================#
# Place your histogram function after this line

import matplotlib.pyplot as plt
import numpy as np

def histogram(data: list, attribute: str) -> list:
    """
    plots if the attribute is numeric of the attribute values and returns the maximum value.
    If the attribute is categorical, it plots a bar chart of the attribute counts and returns -1.

    >>>histogram([1,2,3,4,5,6,7], "Health")
    "..."
    >>>histogram([1,3,5,7,9], "Stamina")
    "..."
    >>> histogram([2,4,6,8,10], "Stamina")
    "..."

    """
    plt.figure()
    # Check if the attribute is numeric or categorical
    if isinstance(data[0][attribute], (int, float)):
        # Numeric attribute
        # Define 20 intervals between 0 and the maximum value of the attribute
        intervals = np.linspace(0, max(item[attribute] for item in data), 20)
        # Count the number of characters that are at each level of the attribute
        counts = [sum(1 for item in data if item[attribute] >= start and item[attribute] < end) for start, end in zip(intervals[:-1], intervals[1:])]
        # Plot the histogram
        plt.bar(intervals[:-1], counts, width=np.diff(intervals), align="edge")
        plt.xlabel(attribute)
        plt.ylabel("Count")
        plt.title(f"Histogram of {attribute}")
        plt.show()
        # Return the maximum value for the given attribute
        return max(item[attribute] for item in data)
    else:
        # Categorical attribute
        # Count the number of characters for each category
        categories = list({item[attribute] for item in data})
        counts = [sum(1 for item in data if item[attribute] == category) for category in categories]
        # Plot the histogram
        plt.bar(categories, counts)
        plt.xlabel(attribute)
        plt.ylabel("Count")
        plt.title(f"Histogram of {attribute}")
        plt.show()
        # Return -1
        return -1

# Do NOT include a main script in your submission

