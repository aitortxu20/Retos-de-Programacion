# /*
#  * Create a function that simulates the weather conditions (temperature and probability of rain)
#  * of a fictional place over a specific number of days following these rules:
#  * - The initial temperature and % chance of rain are defined by the user.
#  * - Each passing day:
#  *   - 10% chance for the temperature to increase or decrease by 2 degrees.
#  *   - If the temperature exceeds 25 degrees, the probability of rain on the next day
#  *     increases by 20%.
#  *   - If the temperature drops below 5 degrees, the probability of rain on the next day
#  *     decreases by 20%.
#  *   - If it rains (100%), the temperature of the next day decreases by 1 degree.
#  * - The function receives the number of days for the forecast and displays the temperature
#  *   and whether it rains during all those days.
#  * - It will also display the maximum and minimum temperature during that period and the number of days it will rain.
#  */

import random

def weather(days, temperature, probability):
    values_list = []
    rainy_days = 0

    for i in range(1, days + 1):
        n_random = random.randrange(0, 10)
        variation = random.choice((0, 1))

        if n_random == i:
            if variation == 0:
                temperature += 2
            else:
                temperature -= 2

        if temperature > 25 and probability <= 80:
            probability += 20
        elif temperature > 25:
            probability = 100

        if temperature < 5 and probability >= 20:
            probability -= 20
        elif temperature < 5:
            probability = 0

        if probability == 100:
            temperature -= 1
            rainy_days += 1

        values_list.append((temperature, probability))
        print(f"Day {i}, temperature {temperature}, and a {probability}% chance of rain.")

    print(values_list)
    max_temp = values_list[0][0]
    min_temp = values_list[0][0]

    for temp, prob in values_list:
        if temp > max_temp:
            max_temp = temp
        if temp < min_temp:
            min_temp = temp

    print(f"The maximum temperature was {max_temp}, the minimum was {min_temp}, and it rained for {rainy_days} days.")


weather(5, -7, 60)
