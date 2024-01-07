# /*
#  * Create a function that calculates the column number in an Excel sheet
#  * based on its name.
#  * - Columns are designated by letters from "A" to "Z" infinitely.
#  * - Examples: A = 1, Z = 26, AA = 27, CA = 79.
#  */

def excel_column_to_number(column):
    letters = {chr(i): i - 64 for i in range(65, 91)}
    result = 0

    for i in range(len(column)):
        letter = column[len(column) - 1 - i]
        result += letters[letter] * (26 ** i)

    return result

print(excel_column_to_number("A"))
print(excel_column_to_number("Z"))
print(excel_column_to_number("AA"))
print(excel_column_to_number("BFP"))


