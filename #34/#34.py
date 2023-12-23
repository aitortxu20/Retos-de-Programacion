# /*
#  * Create a program capable of interacting with a TXT file.
#  * IMPORTANT: The TXT file should NOT be uploaded as part of the submission.
#  * Only the code.
#  *
#  * - If it doesn't exist, it should create a file named "text.txt".
#  * - The program should allow entering text via the console and save it
#  *   on a new line each time the "Enter" button is pressed.
#  * - If the file exists, the program should offer the option to continue writing
#  *   from where it left off or erase its content and start fresh.
#  * - If continuing writing is selected, it should display the text already present
#  *   in the file on the console.
#  */

try:
    with open("text.txt", "r") as f:

        content = f.readlines()
        print(content)
        option = input("The file exists. Do you want to continue writing? Y/N: ")
        if option == "Y":

            with open("text.txt", "a") as f:

                text = input("Enter text to append: ")
                f.write(text)
                f.write("\n")

        else:
            with open("text.txt", "w") as f:
                text = input("Enter text to write: ")
                f.write(text)
                f.write("\n")

except FileNotFoundError:
    with open("text.txt", "w") as f:
        text = input("Enter text (exception): ")
        f.write(text)
