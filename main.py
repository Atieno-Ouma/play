# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#task
points=int(input('please enter your points'))

prize_name=['wooden_rabbit','no prize','wafer-thin_mint','penguin']
    if points<=50:
     prize = prize_name[0]
    elif points>=51 and points<=150:
     prize=prize_name[1]
    elif points>=151 and points<=180:
     prize = prize_name[2]
    elif points >= 181 and points <= 200:
     prize = prize_name[3]
    else:
     print('Invalid Points.Please reenter valid points')
message='You have won the {} Prize'.format(prize_name)
print(message)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
 if
     