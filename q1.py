def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Check if lst is actually a list
    if not isinstance(lst, list):
        return None
    
    # Create modified list by replacing values
    modified_list = []
    for item in lst:
        if item == find_val:
            modified_list.append(replace_val)
        else:
            modified_list.append(item)
    
    return modified_list

Complete Script (q1.py):

def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Check if both x and y are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap values using only x and y variables (no temp variable)
    x = x + y  # x now contains sum of original x and y
    y = x - y  # y now contains original x value
    x = x - y  # x now contains original y value
    
    # Print the swapped values
    print(f"x = {x}, y = {y}")
    
    return x, y

# Test cases
print("Test 1: Valid numbers")
swap(5, 15)  # Should print: x = 15, y = 5

print("\nTest 2: Invalid input")
result = swap("hello", 5)  # Should return -1
print(f"Result: {result}")



Answer:
Test 1: Valid numbers
x = 15, y = 5

Test 2: Invalid input
Result: -1

Explanation: 

Original: x = 5, y = 15
Step 1: x = 5 + 15 = 20, y = 15
Step 2: y = 20 - 15 = 5 (original x), x = 20  
Step 3: x = 20 - 5 = 15 (original y), y = 5
Result: x = 15, y = 5 (successfully swapped)

isinstance(value, type_or_types) to Checks if a value belongs to a specific data type
Returns True if it matches, False if it doesn't. 

If either x OR y is not numeric → return -1

Output:
Prints the swapped values using f-string formatting
Returns the swapped value.


Complete Script (q1.py):Task 2 ( Have inculde task 1 & 2 invokes that same swap() function) 

# Task 1: Swap Function
def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Check if both x and y are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap values using only x and y variables (no temp variable)
    x = x + y  # x now contains sum of original x and y
    y = x - y  # y now contains original x value
    x = x - y  # x now contains original y value
    
    # Print the swapped values
    print(f"x = {x}, y = {y}")
    
    return x, y

# Task 1 Test Cases
print("TASK 1: Testing swap function")
print("="*40)
print("Test 1: Valid numbers")
swap(5, 15)

print("\nTest 2: Invalid input")
result = swap("hello", 5)
print(f"Result: {result}")

# Task 2: Test with given scenarios
print("\n" + "="*50)
print("TASK 2: Testing swap function with given scenarios")
print("="*50)

print("\nScenario 1: swap('Apple', 10)")
result1 = swap("Apple", 10)
print(f"Returned value: {result1}")

print("\nScenario 2: swap(9, 17)")
result2 = swap(9, 17)
print(f"Returned value: {result2}")

Answer: 
Scenario 1: swap('Apple', 10)
Returned value: -1

Scenario 2: swap(9, 17)
x = 17, y = 9
Returned value: (17, 9)

Explanation:

Scenario 1: swap("Apple", 10)

Tests the function with mixed data types (string and integer)
"Apple" is not numeric, triggering input validation
Function returns -1 as expected for invalid input
No swapping occurs due to non-numeric data

Scenario 2: swap(9, 17)

Tests the function with valid numeric inputs (both integers)
Function performs mathematical swap successfully
Prints swapped values: "x = 17, y = 9"
Returns tuple (17, 9) containing the swapped values

Output:

Scenario 1: swap("Apple", 10)

Tests the function with mixed data types (string and integer)
"Apple" is not numeric, triggering input validation
Function returns -1 as expected for invalid input
No swapping occurs due to non-numeric data

Scenario 2: swap(9, 17)

Tests the function with valid numeric inputs (both integers)
Function performs mathematical swap successfully
Prints swapped values: "x = 17, y = 9"
Returns tuple (17, 9) containing the swapped values



