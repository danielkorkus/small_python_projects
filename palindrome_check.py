# This script checks if word is a palindrome and loops 3 times until one is provided

input_counter = 0

while input_counter != 3:
    user_input = input('Enter a word: ')
    if user_input[0::].upper() == user_input[::-1].upper():
        print(f"The word {user_input} is a palindrome")
        break
    else:
        print(f"The word {user_input} is not a palindrome")
        input_counter += 1
