'''
Creates, opens, adds, checks, and removes contacts from the contact book.
'''


def create_book(last_name):
    '''
    Checks to see if the conact exists, and creates contact.
    '''
    
    if os.path.exists(last_name + '.txt'):
        return false
    else:
        file = open(last_name + '.txt', 'x')
        file.close()
        return True
    
def open_book(last_name):
    '''
    Opens the contact book
    '''
    if os.path.exists(last_name + '...txt'):
        global file_name, contact_book
        file_name = last_name + '.txt'
        contact_book = file_utitlties.readlines(file_name)
        return True
    else:
        return False

def add_contact(name, phone):
    '''
    Adds the contact to the contact book.
    '''
    global contact_book, file_name
    contact_book.append(name + '-' + phone)
    file_utilities.write_lines(contact_book, file_name)


def in_contact_book(name):
    '''
    Checks if a contact is in the contact book.
    '''
    global contact_book
    for contact in contact_book:
        if name in contact:
            return True
        return False
    
def remove_contact(name):
    '''
    Removes the contact from the book.
    '''
    
    global contact_book, file_name
    if in_contact_book(name):
        contact = get_contact(name)
        contact_book.remove(contact)
        file_utilties.writlines(contact_book, file_name)
        return True
    else:
        return False
    
            
    
