'''
Rolls a 4, 6, 8, 10, 12, 20, or 100 sided di.
'''

import random

def select_dice():
    '''
    Selects the di.
    '''
    di = input('What di would you like to use? (d4, d6, d8, d10, d12, d20, d100) >> ')
    if di == 'd4':
        print('You rolled a...', d4())
    elif di == 'd6':
        print('You rolled a...', d6())
    elif di == 'd8':
        print('You rolled a...', d8())
    elif di == 'd10':
        print('You rolled a...', d10())
    elif di == 'd12':
        print('You rolled a...', d12())
    elif di == 'd20':
        print('You rolled a...', d20())
    elif di == 'd100':
        print('You rolled a...', d100())
    else:
        print('Invaild!')
    

def d4():
    '''
    Rolls a 4-sided di.
    '''
    
    dice = 0
    dice = random.randint(1, 4)
    return dice

def d6():
    '''
    Rolls a 6-sided di.
    '''
    dice = 0
    dice = random.randint(1, 6)
    return dice

def d8():
    '''
    Rolls a 8-sided di.
    '''
    dice = 0
    dice = random.randint(1, 8)
    return dice

def d10():
    '''
    Rolls a 10-sided di.
    '''
    dice = 0
    dice = random.randint(1, 10)
    return dice

def d12():
    '''
    Rolls a 12-sided di.
    '''
    dice = 0
    dice = random.randint(1, 12)
    return dice

def d20():
    '''
    Rolls a 20-sided di.
    '''
    dice = 0
    dice = random.randint(1, 20)
    return dice

def d100():
    '''
    Rolls a 100-sided di.
    '''
    dice = 0
    dice = random.randint(1, 100)
    return dice
