# 1. Name:
#      Michael Johnson
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program reads a JSON file containing a list of names, sorts them alphabetically using a custom selection sort algorithm, 
#      and displays the sorted list. The sorting algorithm was implemented manually to meet the assignment requirements, and assertions 
#      were added to handle potential errors such as missing keys, empty lists, and invalid data types.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was ensuring that the sorting algorithm was implemented according to my pseudocode without 
#      using Python's built-in sort functions. It required careful consideration to handle various edge cases, such as empty lists and 
#      non-string elements, which could cause errors. Adding assertions to catch these issues helped reinforce error handling but required 
#      me to think carefully about where potential errors might occur in the program's flow. Overall, translating my pseudocode directly 
#      into Python code while maintaining readability and accuracy was challenging but rewarding.
# 5. How long did it take for you to complete the assignment?
#      Approximately 3 hours, including reading the assignment instructions, writing the pseudocode, implementing the program, and debugging any issues, along with recording and publishing.


import json

# Get the filename from user input
file_name = input("What is the name of the file? ")

# Load data from JSON file
path = f"Lab08.{file_name}"
with open(path, 'r') as file:
    data = json.load(file)
    assert "array" in data, "JSON must contain an 'array' key."
    names = data["array"]

# Assert to check for an empty list
assert names, "The list is empty."

# Selection Sort
length_of_list = len(names)
unsorted_index = length_of_list - 1

while unsorted_index > 0:
    index_of_largest = 0
    for current_index in range(1, unsorted_index + 1):
        # Ensure all elements are strings
        assert isinstance(names[current_index], str), "List contains non-string elements."
        if names[current_index] > names[index_of_largest]:
            index_of_largest = current_index
    # Swap the largest element to the correct position
    names[index_of_largest], names[unsorted_index] = names[unsorted_index], names[index_of_largest]
    unsorted_index -= 1

# Display the sorted list
print("The values are:")
for name in names:
    print(f"\t{name}")