# Q3: Dictionary Update Function Implementation

def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if key already exists in dictionary
    if key in dct:
        print(f"Original value: {dct[key]}")
    
    # Update the dictionary with new key-value pair
    dct[key] = value
    
    # Return the updated dictionary
    return dct

# Basic test
test_dict = {'a': 1, 'b': 2}
print(f"Original dictionary: {test_dict}")

# Test with existing key
result1 = update_dictionary(test_dict, 'a', 10)
print(f"Updated dictionary: {result1}")

print()

# Test with new key
result2 = update_dictionary(test_dict, 'c', 3)
print(f"Updated dictionary: {result2}")

Answer:

Original dictionary: {'a': 1, 'b': 2}
Original value: 1
Updated dictionary: {'a': 10, 'b': 2}

Updated dictionary: {'a': 10, 'b': 2, 'c': 3}

Explanation:

First call: Key 'a' exists, prints original value 1, then updates to 10
Second call: Key 'c' is new, no print, just adds to dictionary
Returns: Updated dictionary in both cases




# Q3 Task 2: Invoke update_dictionary with specified scenarios

def update_dictionary(dct, key, value):
    """
    Create a function that updates a dictionary (dct) with a new key-value pair.
    If the key already exists in dct, print the original value, then update its value.
    Return the updated dictionary.
    """
    # Check if key already exists in dictionary
    if key in dct:
        print(f"Original value: {dct[key]}")
    
    # Update the dictionary with new key-value pair
    dct[key] = value
    
    # Return the updated dictionary
    return dct

# Task 2: Invoke function with specified scenarios
# Scenario 1: Update existing key
test_dict1 = {'name': 'John', 'age': 25}
result1 = update_dictionary(test_dict1, 'age', 30)
print(f"Scenario 1 Result: {result1}")

print()

# Scenario 2: Add new key
test_dict2 = {'x': 10, 'y': 20}
result2 = update_dictionary(test_dict2, 'z', 30)
print(f"Scenario 2 Result: {result2}")

Answer: 

Original value: 25
Scenario 1 Result: {'name': 'John', 'age': 30}

Scenario 2 Result: {'x': 10, 'y': 20, 'z': 30}

Explanation:

The update_dictionary function.

Scenario 1: Update Existing Key
Step-by-step process:

Check: Key 'age' exists in dictionary? YES
Print: "Original value: 25" (current value of 'age')
Update: dct['age'] = 30 (change 25 to 30)
Return: {'name': 'John', 'age': 30}

Scenario 2: Add New Key

Step-by-step process:

Check: Key 'z' exists in dictionary? NO
Print: Nothing (no original value to print)
Update: dct['z'] = 30 (add new key-value pair)
Return: {'x': 10, 'y': 20, 'z': 30}
