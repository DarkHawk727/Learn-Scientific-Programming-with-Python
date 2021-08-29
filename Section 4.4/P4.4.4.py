import os
import sys

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']


try:
    dir_name = sys.argv[1]

except NotADirectoryError():
    print('Please use a valid directory.')

except FileNotFoundError():
    print('The requested file cannot be found')

for filename in os.listdir(dir_name):
    # filename is expected to be in the form ' data -DD-MMM-YY.txt '
    try:
        d, month , y = int(filename[5:7]), filename[8:11], int(filename [12:14])
    
    except ValueError():
        print('File is in incorrect Format')
    
    try:
        m = months.index(month.lower())+1
    
    except IndexError():
        print('Month not recognized')

    newname = 'data -20{:02d}-{:02d}-{:02d}.txt'.format(y, m, d)
    newpath = os.path.join(dir_name , newname)
    oldpath = os.path.join(dir_name , filename)
    print(oldpath , '->', newpath)
    os.rename(oldpath , newpath)

# python P4.4.4.py C:\Users\arjun\D esktop\P4.4.4_Dates\