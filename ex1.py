import os
from shutil import move

def main():
    list_of_files = os.listdir("original_files") # this returns a list of all the files in the direcotry

    # makes directories for all of the letters of the alphabet
    for i in range(ord('a'), ord('z')+1): # range of 97-122
        if not os.path.exists(chr(i)):
            os.makedirs(chr(i))

    for files in list_of_files:
        letter = files[0] # strings are lists so you can access the first character with an index of 0
        move("original_files\\" + files, letter) # move the file to the directory of the letter it starts with

main()