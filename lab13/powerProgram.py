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
import time
import json
import os

def read_power_data(filename):
    # Validate and read power data from a JSON file
    assert isinstance(filename, str), "Filename must be a string"
    assert os.path.exists(filename), "File does not exist"

    with open(filename, 'r') as file:
        data = json.load(file)
        assert 'array' in data, "Key 'array' is missing in the JSON file."
        power_data = data['array']
        assert isinstance(power_data, list), "The value of 'array' must be a list."
        assert all(isinstance(i, int) for i in power_data), "All elements in the array must be integers."

    return power_data

def calculate_max_average(power_data, subarray_size):
    # Calculate the maximum average of a subarray of the specified size using a sliding window
    assert isinstance(power_data, list), "Power data must be a list"
    assert all(isinstance(i, int) for i in power_data), "Power data must contain integers"
    assert isinstance(subarray_size, int), "Subarray size must be an integer"
    assert subarray_size > 0, "Subarray size must be greater than zero"
    assert len(power_data) >= subarray_size, "Subarray size is larger than the dataset"

    current_sum = sum(power_data[:subarray_size])  # Initial sum of the first subarray
    max_average = current_sum / subarray_size
    best_subarray = power_data[:subarray_size]

    for i in range(subarray_size, len(power_data)):
        # Update the sum by removing the first element of the previous subarray and adding the next element
        current_sum = current_sum - power_data[i - subarray_size] + power_data[i]
        assert current_sum >= 0, "Sum calculation error"
        
        current_average = current_sum / subarray_size
        if current_average > max_average:
            max_average = current_average
            best_subarray = power_data[i - subarray_size + 1:i + 1]

    return max_average, best_subarray

while True:
    try:
        # Prompt user for file name and subarray size
        filename = input("Enter the name of the file containing power data: ")
        power_data = read_power_data(filename)  # Load power data from the file

        subarray_size = int(input("Enter the size of the subarray: "))

        max_average, best_subarray = calculate_max_average(power_data, subarray_size)  # Calculate results

        print(f"Maximum average: {max_average}")  # Display the maximum average
        print(f"Best subarray: {best_subarray}")  # Display the subarray corresponding to the maximum average

        time.sleep(3)  # Wait for 3 seconds before restarting the loop

    except AssertionError as e:
        print(f"Error: {e}. Please try again.")
    except ValueError:
        print("Invalid input. Subarray size must be an integer. Please try again.")
