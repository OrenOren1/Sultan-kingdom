import MemoryGame
import GuessGame
import CurrencyRouletteGame

def welcome (name):

    print(f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.')


def load_game():
    """
            Currency Roulette - try and guess the value of a random amount of USD in ILS
    """

    choose = False # flag = False is enough. False is already a bool-Done
    print("Please choose a game to play:\n\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    while not choose: # better condition name can be given for readability-Done

        # fix this, developing by exceptions is not good practice. just get the input and check if it a digit or not
        choose_game = input(print("Enter game Number:"))
        if choose_game.isdigit() is True:

            if 0 < int(choose_game) < 4:
                level = False
                choose_level_flag = False
                while not choose_level_flag:
                    level = (input(print("Please choose game difficulty from 1 to 5: ")))
                    if level == '' or (level.isdigit() == False):
                        print("str of null entered  please try again")
                    else:
                        if int(level) > 5:
                            print("level not valid")
                            choose_level_flag = False
                        else:
                            choose_level_flag = True
            else:
                print("Bad choice : please choose a game from the list")
                choose = False
            choose = True
        if choose_game == '1':
            MemoryGame.play_game(int(level))

        elif choose_game == '2':
            GuessGame.play_game(int(level))

        elif choose_game == '3':
            CurrencyRouletteGame.play_game(int(level))
        """else   :
            choose=False
            print ('please enter a valid number')"""

