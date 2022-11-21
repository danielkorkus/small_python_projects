"""
This function calculates collatz conjecture
num test input: 3
if num is not even: n*3+1
if num is even: n/2
repeat until 1
Sample: 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
"""

def collatz(num: int) -> int:
    try:
        print(num)
        while num > 1:
            if num % 2 == 0:
                num = num // 2
                print(num)
            elif num % 2 != 0:
                num = num * 3 + 1
                print(num)
        return None
    except TypeError:
        print('Value must be numerical!')

if __name__ == '__main__':
    collatz(3)
    collatz("hello world!")



