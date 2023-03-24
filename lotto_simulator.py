#  Lotto Simulator
#  Author: Kajetan Mroske

import random


print('''Welcome to LOTTO simulator!
You have to choose 6 numbers between 1 and 49.
Remember numbers can't repeat! \n''')

list_of_user_numbers = []
for i in range(6):
    while True:
        user_selection = input("Pick number and approve with enter: ")
        try:
            user_selection = int(user_selection)
            if user_selection in list_of_user_numbers:
                print("You have already used that number!")
                continue
            if user_selection > 49 or user_selection < 1:
                print("You have to pick number in between 1 and 49!")
                continue
            if 50 > user_selection > 0:
                list_of_user_numbers.append(user_selection)
                break
        except (ValueError, TypeError):
            print("You have to put a number.")

list_of_user_numbers.sort()
print(f"\n Here are your numbers: \n {list_of_user_numbers} \n")


list_of_numbers_selected_by_machine = []
for i in range(6):
    while True:
        machine_choice = random.randint(1, 49)
        if machine_choice not in list_of_numbers_selected_by_machine:
            list_of_numbers_selected_by_machine.append(machine_choice)
            break
        continue

list_of_numbers_selected_by_machine.sort()

print(f'''... and here are the numbers picked by the machine!
{list_of_numbers_selected_by_machine}
''')

list_of_numbers_won = set(list_of_user_numbers) & set(list_of_numbers_selected_by_machine)
number_of_numbers_won = len(list_of_numbers_won)
if number_of_numbers_won > 2:
    print(f'Congratulations! You got {number_of_numbers_won} numbers that match!')
else:
    print(f'We are really sorry, you got {number_of_numbers_won} numbers that match..')
