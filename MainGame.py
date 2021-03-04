from Live import load_game, welcome


print(welcome('Maor'))

flag = 'y'
while flag == str('y'):
    parameters = load_game()

    try:
        while True:
            flag = str(input(print("do you want to play again ? y\\n")))  # all inputs are already str, no need to cast it. no need to print too. just in=input("what is your name")

            if flag == str('n'): # want a challenge? make it support yes no aswell
                break
            elif flag == str('y'):
                break
    except ValueError :
        print('not valid')

        flag = 'y'

print(f"thank for playing with us!")
