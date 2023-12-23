# /*
#  * Create a function that finds all Pythagorean triples
#  * less than or equal to a given number.
#  * - You should search for information on what a Pythagorean triple is.
#  * - The function only takes the maximum number that can
#  *   appear in the triple.
#  * - Example: Triples less than or equal to 10 are
#  *   formed by (3, 4, 5) and (6, 8, 10).
#  */

def pythagoreanTriples(max_number):
    resultList = []
    for num in range(1, max_number + 1):
        num_squared = num ** 2
        for n in range(1, num - 1):
            for n2 in range(1, num - 1):
                if n**2 + n2**2 == num_squared:
                    triplet = (n, n2, num)
                    resultList.append(triplet)
    return resultList


result = pythagoreanTriples(int(input("Enter a number ")))

print(result)
