"""
* Create a function that simulates the weather conditions (temperature and probability of rain)
* for a fictional place over a specific number of days according to the following rules:
* - The user defines the initial temperature and the probability of rain (%).
* - Each passing day:
*   - There is a 10% chance that the temperature will increase or decrease by 2 degrees.
*   - If the temperature exceeds 25 degrees, the probability of rain the next day
*     increases by 20%.
*   - If the temperature drops below 5 degrees, the probability of rain the next day
*     decreases by 20%.
*   - If it rains (100%), the temperature of the next day decreases by 1 degree.
* - The function takes the number of days for the prediction and displays the temperature
*   and whether it will rain for all those days.
* - It also shows the maximum and minimum temperatures for that period and the number of days it will rain.
"""

import random

def climateSimulator(temperature, rainPercentage, simulationLength):

    rainyDays = 0
    temperatures = []

    for i in range(simulationLength):

        day = [temperature, f"{rainPercentage}%"]

        if i == 0:
            pass
        else:

            if random.randrange(10) == 1:
                increaseOrDecrease = random.choice(["+", "-"])
                if increaseOrDecrease == "+":
                    temperature += 2
                else:
                    temperature -= 2

            if temperature > 25:
                rainPercentage += 20
            elif temperature < 5:
                rainPercentage -= 20

            if rainPercentage >= 100:
                rainPercentage = 100
                rainyDays += 1
                temperature -= 1

            if temperature not in temperatures:
                temperatures.append(temperature)
        
        print(day)

    print(f"Maximum: {max(temperatures)}\nMinimum: {min(temperatures)}\nRainy days: {rainyDays}")


climateSimulator(25, 50, 30)