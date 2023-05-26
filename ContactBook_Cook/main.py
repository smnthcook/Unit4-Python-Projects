'''
Contact Book
Samantha Cook
5/8/2023
Python II
'''

import file_utilities
import os
import contact_book


def manipulate_book(name):
    action = ''
    while action != 'quit':
        action = input('Create or open a contact in the contact book (quit to exit) >>')
        if action == 'add':
            person_name = input("Enter the person's name >> ")
            phone = inpiut("Enter the person's phone number >> ")
            contact_book.add_contact(person_name, phone)
        elif action == 'remove':
            person_name = input("What is the name of the person you'd like to remove from the contact book? >>")
            if contact_book.remove_contact(person_name):
                print("Successfully removed the contact.")
            else:
                print('Invaild operation')
                
#main
action = ''
while action != 'quit':
    action = input('Would you like to create or open a contact? >> ')
    if action == 'create':
        name = input('Enter the name of the contact you wish to create. >> ')
        if contact_book.create_book(name):
            print('Contact successfully created!')
        else:
            print('That contact already exists!')
    elif action == 'open':
        name = input('Enter the name of the contact you would like to open. >>')
        if contact_book.open_book(name):
            manipulate_book(name)
        else:
            print('That is an invaild operation.')
            
        

    