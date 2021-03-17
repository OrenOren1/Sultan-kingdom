from os import system, name
import os
    # import sleep to show output for some time period
from time import sleep
SCORES_FILE_NAME='scores.txt'
BAD_RETURN_CODE=1

def screen_cleaner ():


    # define our clear function

    def clear():

        # for windows
        if name == 'nt':
            os.system('cls')

            # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

            # print out some text



    # sleep for 2 seconds after printing output
    sleep(2)

    # now call function we defined above
    clear()
