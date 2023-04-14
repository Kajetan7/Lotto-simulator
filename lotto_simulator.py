#  Lotto Simulator
#  Author: Kajetan Mroske

import random

# Prints a welcome message and prompts the user to choose 6 numbers between 1 and 49.
print('''Welcome to LOTTO simulator!
You have to choose 6 numbers between 1 and 49.
Remember numbers can't repeat! \n''')

# Creates an empty list to store the user's selected numbers.
list_of_user_numbers = []

# Allows the user to input 6 unique numbers between 1 and 49.
# If the user inputs a non-integer or repeats a number, appropriate messages are printed.
for i in range(6):
    while True:
        user_selection = input("Pick number and approve with enter: ")
        try:
            user_selection = int(user_selection)
            # Checking if the number is already in the list
            if user_selection in list_of_user_numbers:
                print("You have already used that number!")
                continue
            # Checking if the number is between 1 and 49
            if user_selection > 49 or user_selection < 1:
                print("You have to pick number in between 1 and 49!")
                continue
            # If the number is valid, adding it to the list
            if 50 > user_selection > 0:
                list_of_user_numbers.append(user_selection)
                break
        # If the user enters something other than a number
        except (ValueError, TypeError):
            print("You have to put a number.")

# Sorts the user's selected numbers in ascending order and prints them.
list_of_user_numbers.sort()
print(f"\n Here are your numbers: \n {list_of_user_numbers} \n")

# Creates an empty list to store the numbers selected by the machine.
list_of_numbers_selected_by_machine = []

# Randomly selects 6 unique numbers between 1 and 49 for the machine's picks.
for i in range(6):
    while True:
        machine_choice = random.randint(1, 49)
        # Checking if the number is already in the list
        if machine_choice not in list_of_numbers_selected_by_machine:
            list_of_numbers_selected_by_machine.append(machine_choice)
            break
        continue

# Sorting the machine-selected numbers in ascending order
list_of_numbers_selected_by_machine.sort()

# Displaying the machine-selected numbers
print(f'''... and here are the numbers picked by the machine!
{list_of_numbers_selected_by_machine}
''')

# Finding the instersection of the user's numbers and the machine-selected numbers
list_of_numbers_won = set(list_of_user_numbers) & set(list_of_numbers_selected_by_machine)
number_of_numbers_won = len(list_of_numbers_won)

# Checking how many numbers the user got right and displaying the result
if number_of_numbers_won > 2:
    print(f'Congratulations! You got {number_of_numbers_won} numbers that match!')
else:
    print(f'We are really sorry, you got {number_of_numbers_won} numbers that match..')
