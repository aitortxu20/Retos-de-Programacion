"""
/*
 * Write a program capable of generating passwords randomly. 
 * You can configure the generation of passwords with the following parameters:
 * - Length: Between 8 and 16 characters.
 * - With or without uppercase letters.
 * - With or without numbers.
 * - With or without symbols.
 * (Combining all these parameters as needed)
 */
"""

import random

def chooseRandoms():
    upperLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbersList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    symbols = ['@', '#', '$', '%', '&', '*', '_', '!', '-']
    
    randomUpper = random.choice(upperLetters)
    randomNumber = str(random.choice(numbersList))
    randomSymbol = random.choice(symbols)
    
    return (randomUpper, randomNumber, randomSymbol)

def generatePassword(length = 8, upper = True, numbers = True, symbols = True):
    
    password = []
    
    if length > 16:
        print("ERROR: Maximum length is 16")
        exit()
    
    while len(password) < length:
    
        randoms = chooseRandoms()

        if random.randrange(3) == 0:
            if upper == True:
                password.append(randoms[0])
        elif random.randrange(3) == 1:
            if numbers == True:
                password.append(randoms[1])
        else:
            if symbols == True:
                password.append(randoms[2])
        
        if len(password) > length:
            password.pop()
        
    print("".join(password))
    
generatePassword(16)