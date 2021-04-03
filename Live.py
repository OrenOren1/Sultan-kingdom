import MemoryGame
import GuessGame
import CurrencyRouletteGame
import scores



def welcome (name) :

    print("Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")


def load_game():

    POINTS_OF_WINNING = int(0)
    """
            Currency Roulette - try and guess the value of a random amount of USD in ILS
    """
<<<<<<< HEAD
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
=======

    choose = False # flag = False is enough. False is already a bool-Done
    print("Please choose a game to play:\n\n1. Memory Game - a sequence of numbers will appear for 1 second and you"
          " have to guess it back\n2. Guess Game -"
          " guess a number and see if you chose like the computer\n3. Currency Roulette - "
          "try and guess the value of a random amount of USD in ILS")
    while not choose: # better condition name can be given for readability-Done

        # fix this, developing by exceptions is not good practice. just get the input and check if it a digit or not
        choose_game = input(print("Enter game Number:"))
        if choose_game.isdigit() is True:

            if 0 < int(choose_game) < 4:
                level = False
                choose_level_flag = False
                while not choose_level_flag:
                    level = (input(print("Please choose game difficulty from 1 to 5: ")))
                    if level == '' or (level.isdigit() is False):
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
            result = MemoryGame.play_game(int(level))
            if result:
                scores.add_score(int(level))

        elif choose_game == '2':
            result = GuessGame.play_game(int(level))
            if result:
                scores.add_score(int(level))

        elif choose_game == '3':
            result = CurrencyRouletteGame.play_game(int(level))
            if result:
                scores.add_score(int(level))
>>>>>>> review-fixes

        """else   :
            choose=False
            print ('please enter a valid number')"""

