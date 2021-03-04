import MemoryGame
import GuessGame
import CurrencyRouletteGame


def welcome (name) :

    print(f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.')


def load_game():
    """
            Currency Roulette - try and guess the value of a random amount of USD in ILS
    """
    choose = False
    #flag = False # flag = False is enough. False is already a bool done

    #while not flag: # better condition name can be given for readability
    print("Please choose a game to play:\n\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    while not choose:
            #try:
                # fix this, developing by exceptions is not good practice. just get the input and check if it a digit or not

        choose_game = input(print("insert game number"))
        if choose_game.isdigit() is False:

            print('bad choise, please insert game from list')
            choose = False
        elif 0 < int(choose_game) < 4:

            level = int(input(print("Please choose game difficulty from 1 to 5: ")))
            if 0 < level < 6:
                if choose_game == '1':
                    choose = True
                    MemoryGame.play_game(level)

                elif choose_game == '2':
                    choose = True
                    GuessGame.play_game(level)

                elif choose_game == '3':
                    choose = True
                    CurrencyRouletteGame.play_game(level)
            else:
                print("level not valid")
    return


        #except ValueError:
         #   print ('please enter a valid number')


