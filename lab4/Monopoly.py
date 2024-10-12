# 1. Name:
#      Michael Johnson
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program asks the user several questions about their game state in Monopoly and informs them whether they can purchase a hotel on Pennsylvania Avenue and how much it will cost, depending on various conditions.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was handling all the conditional logic and ensuring that the output messages correspond correctly to each scenario.
# 5. How long did it take for you to complete the assignment?
#      About 3 hours, including testing and debugging and recording the video.

def main():
    # First essential question
    owns_green_properties = input("Do you own all the green properties? (y/n) ").lower()

    # If they don't own all the green properties, no need to ask more questions
    if owns_green_properties == 'n':
        print("You cannot purchase a hotel until you own all the properties of a given color group.")
        return

    # Ask for Pennsylvania Avenue status only if the player owns all green properties
    pennsylvania_avenue_status = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))

    # If Pennsylvania already has a hotel, no need to ask more questions
    if pennsylvania_avenue_status == 5:
        print("You cannot purchase a hotel if the property already has one.")
        return

    # Ask how many houses are available
    available_houses = int(input("How many houses are there to purchase? "))

    # Ask about Pacific and North Carolina Avenue statuses
    pacific_avenue_status = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
    north_carolina_avenue_status = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))

    # Calculate how many houses are needed (only for properties with less than 4 houses)
    needed_houses_for_pacific = max(0, 4 - pacific_avenue_status)
    needed_houses_for_nc = max(0, 4 - north_carolina_avenue_status)
    needed_houses_for_pa = max(0, 4 - pennsylvania_avenue_status)

    total_houses_needed = needed_houses_for_pacific + needed_houses_for_nc + needed_houses_for_pa

    # Check if there are enough houses available
    if total_houses_needed > available_houses:
        print("There are not enough houses available for purchase at this time.")
        return

    # Check if swapping is possible (if there’s already a hotel on Pacific or North Carolina)
    if pennsylvania_avenue_status == 4:  # Check for swapping if Pennsylvania has 4 houses
        if pacific_avenue_status == 5:
            print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
            return
        elif north_carolina_avenue_status == 5:
            print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
            return

    # If no swap is possible, calculate the cost of the hotel and houses (if any)
    available_cash = int(input("How much cash do you have to spend? "))
    house_cost = 200
    hotel_cost = 300
    total_house_cost = total_houses_needed * house_cost  # Cost of needed houses
    total_purchase_cost = total_house_cost + hotel_cost  # Total cost of houses and hotel

    # Check if the user has enough money to buy the houses and hotel
    if available_cash < total_purchase_cost:
        print(f"You do not have sufficient funds to purchase {total_houses_needed} house(s) and a hotel.")
        return

    # If there is enough cash, proceed with the house and hotel purchase
    print(f"This will cost ${total_purchase_cost}.")
    print(f"Purchase {total_houses_needed} house(s) and 1 hotel.")
    
    # Update the properties by placing houses on each one
    print(f"Put {needed_houses_for_pa} house(s) on Pennsylvania Avenue.")
    print(f"Put {needed_houses_for_nc} house(s) on North Carolina Avenue.")
    print(f"Put {needed_houses_for_pacific} house(s) on Pacific Avenue.")
    
    # Return 4 houses from Pennsylvania to the bank and place the hotel
    print("Return 4 houses from Pennsylvania to the bank.")
    print("Put 1 hotel on Pennsylvania Avenue.")

# Run the main function
if __name__ == "__main__":
    main()