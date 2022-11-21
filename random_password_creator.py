#This script creates a random 16 chars password for user
from random import randrange

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = lower_case.upper()
numbers = "123456789"
special_symbols = "!@#$%^&*()_+=<>,./';:{}[]"
combination = []

while len(combination) != 4:   # appends 4 x 4 chars to list => 16 chars in total
    combination.append(lower_case[randrange(0,len(lower_case))] +
                    upper_case[randrange(0,len(upper_case))] +
                    numbers[randrange(0,len(numbers))] +
                    special_symbols[randrange(0,len(special_symbols))])

password = "".join(combination)
print(password)
