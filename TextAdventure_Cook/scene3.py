def scene3(name):
    '''
    Scene 3 out of 3 scenes. Gives you a backround and gives you 2 choices to choose from.
    '''
    print(name, 'stays, curious about what is about to happen.\n'
        'However, still scared, they keep their hand on their sword. \n'
        'Then, thousands of floraxes come out of the forest, offering gifts to', name + '.')
    
    choice = input(' 1 - Accept the gifts. \n 2 - Pull out your sword. \n')
    
    repeat = 'y'
    while repeat =='y':
        if(choice=='1'):
            print(name, 'accepts the gifts and opens it. Inside there is a note saying, "YOU WON!" ')
            print('Congratulations,', name, ', for choosing all the correct answers!')
            break
        
        elif choice=='2':
            print(name, 'pulls out their sword but all the floraxes calm you down. \n'
                 'You decide to accept the gifts anyway. \n'
                 'Inside, however, is a snake! It pops out and kills you! As you are fading away you see the floraxes \n'
                 'smiling over your dying body.')
            repeat = input('Would you like to try again? (y/n) >> ').lower()
        else:
            print('ENTER THE CORRECT CHOICE!')
            choice = input(' 1 - Accept the gifts. \n 2 - Pull out your sword. \n')