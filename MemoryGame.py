import random
from os import system, name
import time
from subprocess import call
import time
import sys

#difficulty=2 #manual playing
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
    UserListOfInt = []

    def check_int(check):
        if ((check == 0) or (check > 101)):
            return False
        else:
            return True

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

    return UserListOfInt


def play_game(difficulty):

    print (f"\nwelcome to Memory Game - your job is to geuss the Master {difficulty} numbers\n " )
    random = generate_sequence(difficulty)
    flag=False
    while flag==False:
        flag=input(print("press any key to start"))


    sys.stdout.write(f"and the numbers are : {random}")
    time.sleep(0.7)
    sys.stdout.write(f"and the numbers are : {random}\r")

    sys.stdout.flush()

    guess = get_list_from_user(difficulty)
    count = 0
    CheckWin = 0
    for check in random:
        count = 0
        for check2 in guess :

            if (int(check)/int(check2)==1):
                count += 1
        CheckWin = CheckWin+count


    print (f"Master combination- {random}\n")
    print(f"your guess combination- {guess}\n")

    if CheckWin == difficulty:
        print ("incredible guess !! you won ")
    else:
        print(f"you have guessed {CheckWin} numbers- you lost ")




"""flag = 'y
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