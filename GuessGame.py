import random


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
    if bet==secret:
        return True
    else:
        return False


def play_game(level):
    print("welcome to Guess Game - ")
    error = True
    levels=int(100)
    # what if additional 100 levels will be added? make more generic solution-done
    if level == 1:
        difficulty = levels/5
    elif level == 2:
        difficulty = levels/4
    elif level == 3:
        difficulty = levels/3
    elif level == 4:
        difficulty = levels/2
    elif level == 5:
        difficulty = levels


    secret = int(generate_number(difficulty))
    bet = int(get_guess_from_user(difficulty))
    trofyis = compare_results(secret, bet)
    if trofyis:
        print (f"the number is  {secret} nice job!! ")
    else :
        print(f"the number is  {secret} maybe next time!! ")


#manual playing
"""
difficulty=2 #manual playing
flag = 'y'

while flag == str('y'):
    play_game(2)

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