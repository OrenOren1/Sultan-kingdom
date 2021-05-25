import random

import utils


def generate_number (difficulty):

    secretnum = int(random.randint(1, difficulty + 1))
    return secretnum


def get_guess_from_user (difficulty):
    error = True
    while error :
        try:
            bet = int(input(print(f"please place your bet: 0 to {difficulty}")))

            if (bet > 0) and (bet < (difficulty+1)):# check if in range

                return bet               #getting a guess number from user
            else:
                print ("bad choice ")
                error = True

        except ValueError:
            print ("enter a valid number ")
        except TypeError:
            print("enter a valid number ")


def compare_results (bet, secret):
    if bet == secret:
        return True
    else:
        return False


def play_game(level):

    utils.screen_cleaner()
    print("welcome to Guess Game - ")
    span = 100
    error = True
    # what if additional 100 levels will be added? make more generic solution-done
    if level == 1:
        difficulty = span/5
    elif level == 2:
        difficulty = 2*span/5
    elif level == 3:
        difficulty = 3*span/5
    elif level == 4:
        difficulty = 4*span/5
    elif level == 5:
        difficulty = span

    secret = int(generate_number(difficulty))
    bet = int(get_guess_from_user(difficulty))
    trofies = compare_results(secret, bet)
    if trofies:
        print(f"the number is  {secret} nice job!! ")
        win = True
    else:
        print(f"the number is  {secret} maybe next time!! ")
        win = False
    print(trofies)
    return win


"""difficulty=2 #manual playing
flag = 'y'
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
print('thank you for playing!')
"""