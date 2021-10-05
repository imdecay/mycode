#!/usr/bin/env python3

round = 0
answer = ""

while round < 3 and answer != 'Brian':
    round += 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______"').title()
    if answer == 'Brian':
        print('Correct!')
    elif answer == 'Shrubbery':
        print('You said the magic word, and the duck came down!')
        break
    elif round == 3:
        print('You failed to guess it - better luck next time')
    else:
        print('Nope - try again')


