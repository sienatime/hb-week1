import os
from shutil import move

def main():
    list_of_files = os.listdir("original_files") # this returns a list of all the files in the direcotry

    for files in list_of_files:
        letter = files[0] # strings are lists so you can access the first character with an index of 0

        # if it doesn't exist already, make a folder with that letter
        if not os.path.exists(letter):
            os.makedirs(letter)

        move("original_files\\" + files, letter) # move the file to the directory of the letter it starts with

main()