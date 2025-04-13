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

def add(string):
    if len(string)==0:
        return 0
    else:
        return sum(list(map(int,string.split(','))))

print(add(''))
print(add('1'))
print(add('1,5'))

