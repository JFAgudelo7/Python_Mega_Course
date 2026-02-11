#Keyword Arguments
"""
A **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments
"""


"""
Indefinite Number of Keyword Arguments (E)
Enter the correct parameters inside find_sum() so that the output of the code is 9.
"""


def find_sum(**kwargs):
    return sum(kwargs.values())


print(find_sum(a=4, b=5))