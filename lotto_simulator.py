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
            if 50 > user_selection > 0:
                list_of_user_numbers.append(user_selection)
                break
        except (ValueError, TypeError):
            print("You have to put a number.")

list_of_user_numbers.sort()
print(f"\n Here are your numbers: \n {list_of_user_numbers} \n")

numbers_selected_by_machine = [random.randint(1, 49) for i in range(6)]
numbers_selected_by_machine.sort()

print(f'''... and here are the numbers picked by the machine!
{numbers_selected_by_machine}
''')