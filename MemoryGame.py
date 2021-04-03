import random
from os import system, name
import time
from subprocess import call
import time
import sys

<<<<<<< HEAD
#difficulty=2 #manual playing
=======
<<<<<<< Updated upstream
#difficulty=5 # manual Playing 1/2
import utils
=======
# difficulty=5 # manual Playing 1/2
>>>>>>> Stashed changes


>>>>>>> review-fixes
def clear():
    # check and make call for specific operating system
    _ = system('clear')


def generate_sequence(difficulty):

    Start = 1
    Stop = 101
    RandomListOfIntegers = [random.randint(Start, Stop) for iter in range(difficulty)]
    return RandomListOfIntegers


def get_list_from_user(difficulty):
    start = 1
    stop = 101
    user_list_of_int = [False] * int(difficulty)  # create array

    def check_int(check):
        if check == 0 or check > 101:
            return False
        else:
            return True

<<<<<<< HEAD
    UserListOfInt = [False] * int(difficulty) #create array
    num=0
    while UserListOfInt[num] is False and num<difficulty:
        try:
            UserListOfInt[num] = int(input(print(f"please enter your guess between 1-101: ({num + 1}/{difficulty})")))

            while not check_int(UserListOfInt[num]):
                print('guess is out of range')
                UserListOfInt[num] = int(input(print(f"please enter your guess between 1-101: ({num + 1}/{difficulty})")))
            if check_int(UserListOfInt[num]):
                num += 1
            if num ==difficulty:
                break
        except ValueError:

            print("str of null entered  please try again")
            UserListOfInt[num]=False
=======
    user_list_of_int = [False] * int(difficulty)  # create array
    num = 0
    fill_array = False
    while not fill_array:
        check_str = False
        while not check_str:
            user_list_of_int[num] = input(print(f"please enter your guess between 1-101: ({num + 1}/{difficulty})"))
            if user_list_of_int[num] == '':
                print("str of null entered  please try again")
            elif not user_list_of_int[num].isdigit():
                print("str of null entered  please try again")
            else:
                check_str = True

        if not check_int(int(user_list_of_int[num])):
            print('guess is out of range')

        else:
            if num < difficulty-1:
                num += 1
            else:
                fill_array = True
>>>>>>> review-fixes

    return user_list_of_int


def play_game(difficulty):

<<<<<<< Updated upstream
    utils.screen_cleaner()
    print(f"\nwelcome to Memory Game - your job is to geuss the Master {difficulty} numbers\n " )
    random = generate_sequence(int(difficulty))
    flag = False
    while flag is False:
        flag = input(print("press any key to start"))
=======
    print(f"\nwelcome to Memory Game - your job is to geuss the Master {difficulty} numbers\n ")
    random = generate_sequence(int(difficulty))
    flag = False
    while flag is False:
        flag=input(print("press any key to start"))

>>>>>>> Stashed changes

    sys.stdout.write(f"and the numbers are : {random}")
    time.sleep(0.7)
    sys.stdout.write(f"and the numbers are : {random}\r")

    sys.stdout.flush()
    utils.screen_cleaner()
    guess = get_list_from_user(difficulty)
    count = 0
<<<<<<< HEAD
    CheckWin = 0
    for check in random:
        count = 0
        for check2 in guess :

            if (int(check)/int(check2)==1):
                count += 1
        CheckWin = CheckWin+count
=======
    check_win = 0
    for check in random:
        count = 0
        for check2 in guess:
>>>>>>> review-fixes

            if int(check) == int(check2):
                count = + 1
        check_win = check_win+count

    print (f"Master combination- {random}\n")
    print(f"your guess combination- {guess}\n")

<<<<<<< HEAD
    if CheckWin == difficulty:
        print ("incredible guess !! you won ")
=======
    if check_win == difficulty:
        print("incredible guess !! you won ")
        win = True
>>>>>>> review-fixes
    else:
        print(f"you have guessed {check_win} numbers- you lost ")
        win = False

<<<<<<< HEAD


"""flag = 'y
=======
    return win

"""flag = 'y' #manual playing 2/2
>>>>>>> review-fixes
while flag == str('y'):
    play_game(difficulty)

    try:
        while True:
            flag = str(input(print("do you want to play again ? y\\n")))

            if flag == str('n'):
                break
            elif flag == str('y'):
                break
    except ValueError :
        print('not valid')

        flag = 'y'
print('thank you for playing!')"""