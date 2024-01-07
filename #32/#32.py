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


