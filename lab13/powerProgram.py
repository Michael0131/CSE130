# 1. Name:
#      Michael J.
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
#      This program processes power data from a JSON file, calculates the maximum average power for subarrays of a given size, and validates user inputs.
# 4. What was the hardest part? Be as specific as possible.
#      Handling multiple edge cases (e.g., file format validation, invalid JSON structures, and incorrect subarray sizes) while maintaining clear and efficient code was challenging.
# 5. How long did it take for you to complete the assignment?
#      3 hours.
import json
import os

def read_power_data(filename):
    # Validate and read power data from a JSON file
    assert isinstance(filename, str), "Filename must be a string"
    assert os.path.exists(filename), "File does not exist n Error file must be JSON"

    with open(filename, 'r') as file:
        data = json.load(file)
        assert 'array' in data, "Key 'array' is missing in the JSON file."
        power_data = data['array']
        assert isinstance(power_data, list), "The value of 'array' must be a list."
        assert all(isinstance(i, int) for i in power_data), "All elements in the array must be integers."

    return power_data

def calculate_average(power_data, subarray_size):
    # Calculate the average power of a subarray of the specified size
    assert isinstance(power_data, list), "Power data must be a list"
    assert all(isinstance(i, int) for i in power_data), "Power data must contain integers"
    assert isinstance(subarray_size, int), "Subarray size must be an integer"
    assert subarray_size > 0, "Subarray size must be greater than zero"
    assert len(power_data) >= subarray_size, "Subarray size is larger than the dataset"

    total_sum = sum(power_data[:subarray_size])  # Sum of the first subarray
    average = total_sum / subarray_size

    return average

try:
    # Prompt user for file name and subarray size
    filename = input("Enter the name of the file containing power data: ")
    power_data = read_power_data(filename)  # Load power data from the file

    subarray_size = int(input("Enter the size of the subarray: "))

    average_power = calculate_average(power_data, subarray_size)  # Calculate the average

    print(f"Average power: {average_power}")  # Display the average power

except AssertionError as e:
    print(f"Error: {e}")
except ValueError:
    print("Invalid input. Subarray size must be an integer.")


