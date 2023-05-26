'''
Implements simplified verisons of the readlines() and writelines() functions.
'''

import os

def read_lines(file_path):
    '''
    Return a list of all the entries in the file
    with the new line character automatically removed.
    If the file doesn't exist, a blank list is returned.
    Also, any numerica calues will be converted to the
    appropriate type. 
    '''
    entries = []
    if os.path.exists(file_path):
        file = open(file_path, 'r')
        for entry in file:
            entry = entry.strip()
            if entry.isnumeric():
                entries.append(int(entry))
            elif is_float(entry):
                entries.append(float(entry))
            else:
                entries.append(entry)
        file.close()
    return entries
        

def write_lines(entries, file_path, mode='w'):
    '''
    Write all the entries in the list to the file
    such that each entry is on a seperate line.
    "Mode" can only be 'w' or 'a'. 
    '''
    file = open(file_path, mode)
    for entry in entries:
        file.write(str(entry) + '\n')
    file.close()
    

def is_float(value):
    '''
    Checks if a string is a float.
    '''
    try:
        float(value)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    
    file_path = 'test.txt'

    #test string
    write_lines(['a', 'b', 'c', 'd'], file_path)
    print(read_lines(file_path))

    #test integers
    write_lines([1, 2, 3, 4], file_path)
    print(read_lines(file_path))

    # Test floats
    write_lines([1.1, 2.2, 3.3, 4.0], file_path)
    print(read_lines(file_path))
    
    os.remove(file_path)
