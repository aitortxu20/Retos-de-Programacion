"""
Create a function that calculates the column number of an Excel sheet based on its name.
- Columns are designated by letters from "A" to "Z" infinitely.
- Examples: A = 1, Z = 26, AA = 27, CA = 79.
"""

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = [i for i in range(len(letters)+1)]
numbers.remove(0)


def excel_column(column_name):

    if len(column_name) == 1:

        index = letters.index(column_name)
        print(numbers[index])

    else:

        index_pos0 = letters.index(column_name[0])
        index_pos1 = letters.index(column_name[1])

        print(len(letters) * (index_pos0+1) + numbers[index_pos1])


excel_column("CA")
