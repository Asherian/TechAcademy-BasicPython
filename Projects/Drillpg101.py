"""Requirements:
Your script will need to use Python 3 and the OS module.
Your script will need to use the listdir() method from the OS module to
    iterate through all files within a specific directory.
Your script will need to use the path.join() method from the OS module
    to concatenate the file name to its file path, forming an absolute path.
Your script will need to use the getmtime() method from the OS module
    to find the latest date that each text file has been created or modified.
Your script will need to print each file ending with a “.txt” file
    extension and its corresponding mtime to the console.
"""

import os


path=os.listdir()
fName=os.listdir(path='C:\\TechAcademy\\Python\\Projects\\')
fPath='C:\\TechAcademy\\Python\\Projects\\'
paths=os.path.join(fPath, fName[2])
def cycle():
    for filename in os.listdir(path='C:\\TechAcademy\\Python\\Projects\\'):
        if filename.endswith('.txt'):
            print(filename)
            print(os.path.getmtime('C:\\TechAcademy\\Python\\Projects\\'))
            continue
        else:
            continue

if __name__ =="__main__":
    cycle()
