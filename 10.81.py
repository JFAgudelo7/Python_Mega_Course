#Non-Keyword Arguments

"""
Average Function (E)
Define a function that takes an indefinite number of numbers as arguments and returns their average.
If I called your function with foo(10, 20, 30, 40) it should return the 25, the average of those numbers.
"""


def foo(*args):
    return sum(args) / len(args)

print(foo(10, 20, 30, 40))

"""
Indefinite Number of Strings Processed (E)
Define a function that takes an indefinite number of strings as parameters and returns a list containing all the strings
 in UPPERCASE and sorted alphabetically. For example, if I called your function with foo("snow", "glacier", "iceberg") 
 it should return ["GLACIER", "ICEBERG", "SNOW"].
"""

def foo2(*args):
    sorted_ = []
    for arg in args:
        sorted_.append(arg.upper())
    return sorted(sorted_)

print(foo2("snow", "glacier", "iceberg"))