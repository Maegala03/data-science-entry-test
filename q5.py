# Q5: Divisibility Check Function Implementation

def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check if both num and divisor are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return False
    
    # Check if divisor is zero (division by zero)
    if divisor == 0:
        return False
    
    # Check if num is divisible by divisor
    if num % divisor == 0:
        return True
    else:
        return False

# Basic test
result1 = check_divisibility(10, 2)
print(f"10 divisible by 2: {result1}")

result2 = check_divisibility(10, 3)
print(f"10 divisible by 3: {result2}")

result3 = check_divisibility(15, 5)
print(f"15 divisible by 5: {result3}")

Answer:
10 divisible by 2: True
10 divisible by 3: False
15 divisible by 5: True

Explanation:

num % divisor == 0 - checks if remainder is zero
Type checking - ensures both inputs are numeric (int or float)
Division by zero protection - returns False if divisor is 0
Returns boolean - True if divisible, False otherwise



# Q5 Task 2: Invoke check_divisibility with specified scenarios

def check_divisibility(num, divisor):
    """
    Create a function to check if the number (num) is divisible by another number (divisor).
    Both num and divisor must be numeric.
    Return True if num is divisible by divisor, False otherwise.
    """
    # Check if both num and divisor are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return False
    
    # Check if divisor is zero (division by zero)
    if divisor == 0:
        return False
    
    # Check if num is divisible by divisor
    return num % divisor == 0

# Task 2: Invoke function with specified scenarios
# Scenario 1: 10, 2
scenario1 = check_divisibility(10, 2)
print(f"Scenario 1 - 10 divisible by 2: {scenario1}")

# Scenario 2: 7, 3
scenario2 = check_divisibility(7, 3)
print(f"Scenario 2 - 7 divisible by 3: {scenario2}")

Answer:

Scenario 1 - 10 divisible by 2: True
Scenario 2 - 7 divisible by 3: False

Explanation:

Scenario 1: 10, 2
Calculation: 10 ÷ 2 = 5 (no remainder)
Modulo: 10 % 2 = 0
Result: True (10 is divisible by 2)
Scenario 2: 7, 3
Calculation: 7 ÷ 3 = 2.33... (remainder of 1)
Modulo: 7 % 3 = 1
Result: False (7 is not divisible by 3)


