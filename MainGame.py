from Live import load_game, welcome


print(welcome('Guy'))

ask = True
while ask:
    answer = False
    parameters = load_game()


    while not answer:
        try:
            answer = input(print("do you want to play again ? y\\n"))  # all inputs are already str, no need to cast it. no need to print too. just in=input("what is your name")-done
            if answer is False :
                raise ValueError
            if answer is ('n' or 'no'): # want a challenge? make it support yes no aswell-done
                break
            if  answer == 'yes' or 'Yes' or 'y':
                answer = False
                ask = True
                break
            if answer is str('y'):

                print("awesome!! lest play")
            if answer is not (str('yes'),str('no'),str('y'),str('n')):
                raise ValueError

        except ValueError :
            print('not valid')
            answer=False
    if answer is ('n' or 'no'):
        ask=False
        print(f"thank for playing with us!")
