'''
Text Adventure
Samantha Cook
5/9/2023
Python II
'''

import help_desk
import scene1
import scene2


word  = input('Type "quit" to exit, "help" for help, or "start" to play the game >> ').lower()
if word == 'help':
    help_desk.help()
    repeat = 'y'
    while repeat == 'y':
        name = input('What is your name? >> ').upper()
        scene1.scene1(name)
        repeat = input('Would you like to repeat the game again? (y/n) >> ')
elif word == 'quit':
    print('Thanks for playing!')
elif word == 'start':
    repeat = 'y'
    while repeat == 'y':
        name = input('What is your name? >> ').upper()
        scene1.scene1(name)
        repeat = input('Would you like to repeat the game again? (y/n) >> ')
else:
    word = input('Enter a vaild choice(quit or help) >>')


    

