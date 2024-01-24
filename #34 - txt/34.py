"""
/*
Create a program capable of interacting with a TXT file.
IMPORTANT: The TXT file should NOT be uploaded as part of the submission.
Only the code should be provided.
If it doesn't exist, it should create a file named "text.txt".
The program should allow entering text through the console and saving it
on a new line each time the "Enter" key is pressed.
If the file exists, the program should give the option to either continue writing
from where it left off or erase its content and start fresh.
If the option to continue writing is selected, the program should display
the existing text in the file on the console.
*/
"""

import os

currentPath = os.getcwd()
txtPath = f"{currentPath + "\\text.txt"}"

def manipulateFile(txtPath):

    if not os.path.isfile(txtPath):

        file = open(txtPath, 'w')
        addText(txtPath)

    else:

        print("\nERROR: File already exists...")
        print("Options: [W]rite, [R]estart\n")
        userOption = input("> ")

        if userOption == "W":
            file = open(txtPath, 'r')
            fileContent = file.read()

            print(f"\nCurrent text in file:\n{fileContent}")
            addText(txtPath)

        elif userOption == "R":
            print("\nContent successfully removed from file\n")

            os.remove(txtPath)
            manipulateFile(txtPath)
        else:
            print("\nERROR: Invalid option. Exiting...")
            exit()

def addText(txtPath):

    print("\nInput mode ON, add text to file")
    print("Press [CTRL + C] to exit\n")

    file = open(txtPath, 'a')

    while True:
        file.write(input("> "))
        file.write("\n")

manipulateFile(txtPath)
