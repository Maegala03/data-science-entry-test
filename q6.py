# Q6: Find First Negative Function Implementation

def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    # Initialize index counter
    index = 0
    
    # Use while loop to iterate through the list
    while index < len(lst):
        # Check if current element is negative
        if lst[index] < 0:
            return lst[index]  # Return first negative number found
        index += 1  # Move to next element
    
    # If no negative number found, return "No negatives"
    return "No negatives"

# Basic test
test_list1 = [1, 2, -3, 4, -5]
result1 = find_first_negative(test_list1)
print(f"List: {test_list1}")
print(f"First negative: {result1}")

print()

test_list2 = [1, 2, 3, 4, 5]
result2 = find_first_negative(test_list2)
print(f"List: {test_list2}")
print(f"First negative: {result2}")

Answer: 
List: [1, 2, -3, 4, -5]
First negative: -3

List: [1, 2, 3, 4, 5]
First negative: No negatives

Explanation:

Test Case 1: [1, 2, -3, 4, -5]
While loop finds: -3 at index 2
Returns immediately: -3 (first negative)
Doesn't continue to find -5

Test Case 2: [1, 2, 3, 4, 5]
While loop checks all elements: No negatives found
Returns: "No negatives"




# Q6 Task 2: Invoke find_first_negative with specified scenarios

def find_first_negative(lst):
    """
    Create a function that finds the first negative number in a list (lst).
    Return the first negative number if found, otherwise return "No negatives".
    Use a while loop to implement this.
    """
    # Initialize index counter
    index = 0
    
    # Use while loop to iterate through the list
    while index < len(lst):
        # Check if current element is negative
        if lst[index] < 0:
            return lst[index]  # Return first negative number found
        index += 1  # Move to next element
    
    # If no negative number found, return "No negatives"
    return "No negatives"

# Task 2: Invoke function with specified scenarios
# Scenario 1: [3, 5, -1, 7, -2, 8]
scenario1 = find_first_negative([3, 5, -1, 7, -2, 8])
print(f"Scenario 1 Result: {scenario1}")

# Scenario 2: [2, 10, 7, 0]
scenario2 = find_first_negative([2, 10, 7, 0])
print(f"Scenario 2 Result: {scenario2}")

Answer: 
Scenario 1 Result: -1
Scenario 2 Result: No negatives

Explanation:

Scenario 1: [3, 5, -1, 7, -2, 8]

Step-by-step process:

index = 0: Check lst[0] = 3 → 3 < 0? → No → increment index
index = 1: Check lst[1] = 5 → 5 < 0? → No → increment index
index = 2: Check lst[2] = -1 → -1 < 0? → Yes! → Return -1

Scenario 2: [2, 10, 7, 0]

Step-by-step process:

index = 0: Check lst[0] = 2 → 2 < 0? → No → increment index
index = 1: Check lst[1] = 10 → 10 < 0? → No → increment index
index = 2: Check lst[2] = 7 → 7 < 0? → No → increment index
index = 3: Check lst[3] = 0 → 0 < 0? → No → increment index
index = 4: 4 < len([2,10,7,0]) → 4 < 4? → No → exit loop
