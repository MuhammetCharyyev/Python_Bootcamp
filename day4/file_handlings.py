import os

path = 'files/Test.txt'

text_file = open(path, 'r') # will open a file by path and read

print( text_file.read() )


text_file.close() # close the file is mandatory

"""
print(text_file.readline())
print(text_file.readline())
print(text_file.readline()) ->read line by line
"""

print('----------------------------------')

path = 'files/Test2.txt'

text_file2 = open(path, 'w') # if you dont have a file PY will write with 'w'

text_file2.write('This is a new text file\nPython created this file') # writing a text inside the file

text_file2.close()

print('----------------------------------')

os.remove(path) # delete a file permanently
