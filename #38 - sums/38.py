"""
/*
 * Create a function that finds all combinations of numbers
 * from a list that sum up to the target value.
 * - The function will receive a list of positive integers
 *   and a target value.
 * - Each element from the list can only be used once
 *   to form the combinations (though there may be
 *   repeated elements in the list).
 * - Example: List = [1, 5, 3, 2],  Target = 6
 *   Solutions: [1, 5] and [1, 3, 2] (both combinations sum up to 6)
 *   (If no combinations exist, return an empty list)
 */
"""

import copy

def findCombinations(list, value, combinations=None):

    if combinations is None:
        combinations = []

    index = 0
    for _ in list:
        
        listCopy = copy.deepcopy(list)
        del listCopy[index]

        if sum(listCopy) == value:
            if listCopy not in combinations:
                combinations.append(listCopy)

        for _ in listCopy:
            findCombinations(listCopy, value, combinations=combinations)

        index += 1

    return combinations

print(findCombinations([1, 4], 6))
print(findCombinations([1, 5, 3, 2], 6))
print(findCombinations([2, 2, 3, 5, 1], 7))

