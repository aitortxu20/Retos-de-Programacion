# /*
#  * Create a function that calculates the meeting point of two objects in motion
#  * in two dimensions.
#  * - Each object consists of an xy coordinate and a displacement speed
#  *   (displacement vector) per unit of time (also in xy format).
#  * - The function will receive the starting coordinates of both objects and their speeds.
#  * - The function will calculate and display the point at which they meet and the time it takes to reach it.
#  * - The function must consider that the objects may not meet.
#  */

# d = √((x2 - x1)² + (y2 - y1)²)

import math
from sympy import symbols, Eq, solve

point_a = [0, 0]
speed_a = [2, 2]
point_b = [3, 3]
speed_b = [-2, -2]

t = symbols('t')
eq_x = Eq(point_a[0] + speed_a[0] * t, point_b[0] + speed_b[0] * t)
eq_y = Eq(point_a[1] + speed_a[1] * t, point_b[1] + speed_b[1] * t)

sol = solve((eq_x, eq_y), (t))

if sol:
    intersection_time = sol[t]
    intersection_position = (point_a[0] + speed_a[0] * intersection_time,
                             point_a[1] + speed_a[1] * intersection_time)
    print("Intersection time:", intersection_time)
    print("Intersection position:", intersection_position)
else:
    print("The vectors do not intersect.")

def collision(a, speed_a, b, speed_b):
    distance = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    distance2 = distance
    new_pos_a = [a[0], a[1]]
    new_pos_b = [b[0], b[1]]
    time = 0

    while distance2 > 0 and distance2 <= distance:
        new_pos_a[0] = (new_pos_a[0] + speed_a[0])
        new_pos_a[1] = (new_pos_a[1] + speed_a[1])
        new_pos_b[0] = (new_pos_b[0] + speed_b[0])
        new_pos_b[1] = (new_pos_b[1] + speed_b[1])
        time += 1

        distance2 = math.sqrt((new_pos_a[0] - new_pos_b[0])**2 + (new_pos_a[1] - new_pos_b[1])**2)

        if distance2 == 0.0:
            print(f"They collided at ({new_pos_a[0]}, {new_pos_a[1]}) and took {time} time units")
        elif distance2 > distance:
            print("The objects will never collide")
            print(time-1)
            break
        elif distance2 == distance:
            print("The objects move in parallel")
            break


collision(point_a, speed_a, point_b, speed_b)
