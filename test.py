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
    if len(string) == 0:
        return 0
    else:
        numbers = re.split(',|\n', string)
        return sum(map(int, numbers))

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
