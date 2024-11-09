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