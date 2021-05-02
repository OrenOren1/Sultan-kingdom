import sys
import os
from os import path


def add_score(difficulty, score=0):

    cwd = os.getcwd()

    POINTS_OF_WINNING = (difficulty * 3) + 5

    file_name = 'scores.txt'
    if os.path.isfile(f"{file_name}"):
        my_file = open(f"{cwd}\\score\\{file_name}", 'r+')
        current_score = my_file.read()
        my_file.seek(0)
        score = int(POINTS_OF_WINNING) + int(current_score)
    else:
        my_file = open(f"{cwd}\\score\\{file_name}", "w+")
        my_file.seek(0)
        my_file.write('0')
        score = int(POINTS_OF_WINNING)

    my_file.write(f"{score}")
    print(f'{POINTS_OF_WINNING} points been added to score file')
    my_file.seek(0)

