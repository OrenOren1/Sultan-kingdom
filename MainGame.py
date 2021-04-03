from Live import load_game, welcome


print(welcome('Guy'))

again = False
while True:

    parameters = load_game()

    while True:
        try:
            again = input("do you want to play again ? y\\n")

            Fl = again[0].lower()

            if again is not Fl in ['yesno']:  # want a challenge? make it support yes no aswell-done
                print('Please answer with yes or no!')
            elif again == 'no' or again == 'n':
                again = 'n'
                break
            elif again == 'y' or again == 'yes':
                again = 'y'
                break
        except IndexError:
            print("invalid choice")
    if again == 'n':
        print('thank you for playing!')
        break

"""
while True:
     query = input('Do you love cute owls?')
     Fl = query[0].lower()
     if query == '' or not Fl in ['y','n']:
        print('Please answer with yes or no!')
     else:
        break"""