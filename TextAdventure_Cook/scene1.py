'''
Implements the scenes to the main.
'''

import scene2


def scene1(name):
    '''
    Scene 1 out of 3 scenes. Gives you a backround and gives you 3 choices to choose from.
    '''
    print('Welcome,', name + ', to the world of Julamnia.')
    print(name, 'is walking in the ominous forest when suddenly they see a Florax,\n'
            'a friendly green being, come towards them. What should they do?')
    repeat = 'y'
    while repeat =='y':
        choice = input(' 1 - Run away. \n 2 - Fight. \n 3 - Stay. \n').lower()
    
        if(choice=='1'):
            print(name, 'runs away from the forest and the florax cries.\n',
                  name, 'is so distraught by the Floraxes crying that they \n',
                  'trip, fall and break their nose.\n')
            repeat = input('Would you like to try again? (y/n) >> ').lower()
            
        elif choice=='2':
            print('You pull out your sword and start you fight the Florax but he over'
                 'powers you and kills you in just a few seconds.')
            input('Would you like to try again? (y/n) >> ').lower()
            
        elif choice=='3':
            print(name, 'stays and the Florax starts talking, but it is merely a whisper. He says, "Come with me young one."',
                  name, 'decides to trust him. They follow him deeper into the ominous forest.')
            print('')
            scene2.scene2(name)
            break
        elif choice == 'quit':
            print('Thanks for playing!')
            break
        else:
            print('ENTER THE CORRECT CHOICE!')
            choice = input(' 1 - Run away \n 2 - Fight. \n 3 - Stay. \n ')
            