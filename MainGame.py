from Live import load_game, welcome


print(welcome('Guy'))

flag = 'y'
while flag == str('y'):
    parameters = load_game()

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

print(f"thank for playing with us!")
