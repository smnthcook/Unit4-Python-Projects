

import scene3

def scene2(name):
    '''
    Scene 2 out of 3 scenes. Gives you a backround and gives you 2 choices to choose from.
    '''
    print(name,'hears the sound of crushing leaves as they walk further and further into the forest. \n'
        'Suddenly, the green being stops and turns around. He says something you cannot quite understand. Something in another language. \n',
        name, 'asks, "What?" when red eyes appear all around', name + '. They feel something bad is gonna happen.')
    
    repeat = 'y'
    while repeat =='y':
        choice = input(' 1 - Stay. \n 2 - Run away. \n')
    
        if(choice=='1'):
            scene3.scene3(name)
            break
        elif choice=='2':
            print(name, 'tries to run away, but the floraxes stop them.\n',
                  name, 'screams "Get out of my way!" The floraxes do not answer.\n',
                  'Then, the floraxes give them flowers and lets them pass. But,', name, 'falls down a pit.')
            repeat = input('Would you like to try again? (y/n) >> ').lower()
        else:
            print('ENTER THE CORRECT CHOICE!')
            choice = input(' 1 - Stay. \n 2 - Run away. \n')