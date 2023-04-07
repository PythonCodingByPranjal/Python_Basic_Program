#Check if the file exist in current dir or not?
import os.path
path = './for1.py'
check_file = os.path.isfile(path)
print(check_file)
