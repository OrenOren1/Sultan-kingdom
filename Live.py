import MemoryGame
import GuessGame
import CurrencyRouletteGame

def welcome (name):

    print(f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.')


def load_game():
    """
            Currency Roulette - try and guess the value of a random amount of USD in ILS
    """
    flag = bool(False)

    while not flag:
            try:
                choose_game = int(input(print("Please choose a game to play:\n\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS")))

                if 0 < choose_game < 4:

                    level = int(input(print("Please choose game difficulty from 1 to 5: ")))
                    if 0< level <6:
                        flag = bool(True)
                    else:
                        print("level not valid")
                else:
                    print("Bad choice : please choose a game from the list")
                if choose_game == 1:
                    MemoryGame.play_game(level)

                elif choose_game == 2:
                    GuessGame.play_game(level)

                elif choose_game == 3:
                    CurrencyRouletteGame.play_game(level)

            except ValueError:
                print ('please enter a valid number')


