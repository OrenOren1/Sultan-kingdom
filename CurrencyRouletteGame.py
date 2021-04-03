import random

import numpy as np
#import requests

import utils


def get_money_interval(difficulty,amount):
    def get_currency():   # function gets currency from fixer api
        url = "http://data.fixer.io/api/latest?access_key=a0acec42aa450def2898a65959bfbb13"  # want a challenge? make
        # sure the secret is not stored in the code. in general this is big no no in real life

        payload = {}
        headers = {'Cookie': '__cfduid=df7f1dca850e801bd0e6db4c6e4978fe31613740352'}

        response = requests.request("GET", url, headers=headers, data=payload)
        package_json = response.json()

        a = round(package_json['rates']['ILS'], 2)
        return a

    currency = get_currency()
    money = amount*currency
    start = int(amount*currency - (5 - difficulty))
    stop = int(amount*currency + (5 - difficulty))

    return money, start, stop


def get_guess_from_user(amount):
    uguess = False
    while not uguess:
        try:
            uguess = int(input(print(f"please guess how much ILS is {int(amount)} USD\n")))

        except ValueError:
            uguess = False
            print("cannot enter str or null\n")

    return uguess


def play_game(difficulty):

    utils.screen_cleaner()
    result = 0
    print("welcome to currency guess game")
    amount = float(random.randint(1, 100))
    interval = get_money_interval(difficulty,amount)

    guess = get_guess_from_user(amount)

    shekel = int(interval[0])
    print(f"{amount} USD is {shekel} ILS\n\n ")

    if np.float16(guess) in np.float16(np.arange(interval[1],interval[2],0.1)):
        result = True
        win = True
    else:
        result = False
        win = False
    if result:

        print("you won!!")

    else:
        print("you lost ,try again!!")
    return win


"""
if __name__ == "__main__":
    difficulty = 3
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