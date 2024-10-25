# 1. Name:
#      Michael Johnson
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program reads a sorted list from a JSON file and uses binary search to check if a user-specified item is in the list, 
#      displaying whether it was found.
# 4. Algorithmic Efficiency
#      The binary search algorithm has an efficiency of O(log n), as it halves the search space each iteration, making it 
#      much faster than linear search for sorted lists.
# 5. What was the hardest part? Be as specific as possible.
#      Implementing binary search iteratively without recursion or `in()` was challenging, especially setting up loop 
#      conditions and handling edge cases. Understanding string comparisons also required attention.
# 6. How long did it take for you to complete the assignment?
#      About 1 1/2 hours between writing the code and making the video.

import json

fileName = input("What is the name of the File? ")
target = input("what name are we looking for? ")

found = False
path = f"Lab06.{fileName}"
with open(f"{path}", 'r') as file:
    data = json.load(file)
    words = data['array']

start = 0
end = len(words) - 1

while start <= end:
    mid = (start + end) // 2
    if words[mid] == target:
        found = True
        print("Target found.")
        break
    elif target < words[mid]:
        end = mid - 1
    else:
        start = mid + 1
if not found:
    print("Target not found.")
