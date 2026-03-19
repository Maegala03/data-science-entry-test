# Q4: String Reverse Function Implementation

def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check if s is actually a string
    if not isinstance(s, str):
        return None
    
    # Reverse the string using slicing
    reversed_string = s[::-1]
    
    # Return the reversed string
    return reversed_string

# Basic test
test_string = "hello"
result = string_reverse(test_string)
print(f"Original: {test_string}")
print(f"Reversed: {result}")

# Additional test
test_string2 = "Python"
result2 = string_reverse(test_string2)
print(f"Original: {test_string2}")
print(f"Reversed: {result2}")


Answer: 
Original: hello
Reversed: olleh
Original: Python
Reversed: nohtyP

Explanation:
s[::-1] - Python slicing syntax that reverses the string
Type checking - ensures input is a string
Returns None if input is not a string
Simple and efficient - uses Python's built-in slicing




# Q4: String Reverse Function Implementation

def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check if s is actually a string
    if not isinstance(s, str):
        return None
    
    # Reverse the string using slicing
    reversed_string = s[::-1]
    
    # Return the reversed string
    return reversed_string

# Task 2: Invoke function with specified scenario
# Scenario: "Hello World"
scenario = string_reverse("Hello World")
print(f"Result: {scenario}")


Answer: 

dlroW olleH

Explanation:

The string_reverse function:

Validates input - checks if s is actually a string
Uses slicing - s[::-1] to reverse the string
Returns result - gives back the reversed string

Input: "Hello World" (11 characters)
Character positions:
Position: 0 1 2 3 4 5 6 7 8 9 10
Original: H e l l o   W o r l d

Slicing [::-1]: Reads from end to beginning
Reversed: d l r o W   o l l e H
Position: 10 9 8 7 6 5 4 3 2 1 0

