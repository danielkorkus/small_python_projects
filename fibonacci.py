"""
Fibonacci solution idea functions
"""


#----------------------------------------------------------------------
def fibonacci(num: int) -> int:
    if num in (1,2): return 1
    return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(10))


#----------------------------------------------------------------------
def fibonacci2(num: int) -> int:
    if num < 0:
        print("invalid input")
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci2(num -1) + fibonacci2(num -2)

print(fibonacci2(10))


#----------------------------------------------------------------------
def fibonacci3(num: int) -> int:
    num1, num2 = 0, 1
    for i in range(0, num):
        num1, num2 = num2, num1 + num2
    return num1

print(fibonacci3(10))


#----------------------------------------------------------------------
def fibonacci4(num: int) -> int:
    num1, num2 = 0, 1
    match "fibonacci":
        case 0:
            return 0
        case (1, 2):
            return 1
        case _:
            for i in range(0, num):
                num1, num2 = num2, num1 + num2
            return num1
        
print(fibonacci4(10))
