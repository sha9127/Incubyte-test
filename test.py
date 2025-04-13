"""
Scenario 1

Create a simple String calculator with a method signature like this:

int add(string numbers)
Input: a string of comma-separated numbers
Output: an integer, sum of the numbers
Examples:

Input: “”, Output: 0
Input: “1”, Output: 1
Input: “1,5”, Output: 6

"""
import re

def add(string):
    if not string:
        return 0

    # Checking for delimeter
    if string.startswith("//"):
        parts = string.split("\n", 1)
        delimiter = parts[0][2:]  # getting the delimeter after //
        numbers_str = parts[1]
        delimiter_pattern = re.escape(delimiter)
    else:
        numbers_str = string
        delimiter_pattern = ",|\n"

    numbers = list(map(int, re.split(delimiter_pattern, numbers_str)))

    # Checking for negative numbers
    negatives = [n for n in numbers if n < 0]
    if negatives:
        raise Exception(f"negative numbers not allowed: {','.join(map(str, negatives))}")

    return sum(numbers)

print(add(''))
print(add('1'))
print(add('1,5'))

"""
scenario 2 (Allow the add method to handle any amount of numbers.)
"""

print(add('1,2,3,4,5'))
print(add('1,2,3,4,5,6,7,8,9,10'))
print(add('1,-2,-3,9,-3'))


"""
Scenario 3
Allow the add method to handle new lines between numbers (instead of commas). ("1\n2,3" should return 6)

-for this we have to modify our original function to handle \n
"""

print(add("1\n2,3"))

"""
Scenario 4
To change the delimiter, the beginning of the string will contain a separate line that looks like this: "//[delimiter]\n[numbers…]". For example, "//;\n1;2" where the delimiter is ";" should return 3.

"""

print(add("//;\n1;2"))

"""
Scenario 5

Calling add with a negative number will throw an exception: "negative numbers not allowed <negative_number>".

If there are multiple negative numbers, show all of them in the exception message, separated by commas.
"""

print(add('1,-2,-3,9,-3'))
print(add("//;\n1;-2"))

