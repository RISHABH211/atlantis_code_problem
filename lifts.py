import random


def lifts():
    """
    user floor input
    :return: string
    """

    user_position = input("Enter the user lift lobby position and the direction in which he wants to go: ")

    user_direction = user_position[-1]
    user_floor = int(user_position[:-1])

    each_lift_floor = []
    each_lift_position = []
    direction = ["D", "U", ""]
    lift_position = []

    for i in range(5):
        item = str(random.choice(range(0, 21))) + random.choice(direction)
        lift_position.append(item)

    print(f"Randomly generated lift positions: \n{lift_position}")

    for lift in lift_position:
        if lift[-1].isalpha():
            position = lift[-1]
            floor = lift[:-1]
        else:
            floor = lift
            position = ""
        each_lift_floor.append(int(floor)), each_lift_position.append(position)

    lift_gap = float("inf")
    lift_selected = ""
    for index, lift_floor in enumerate(each_lift_floor):

        # current lift is above the user and the user wants to go up , lift is also going up
        gap = user_floor - lift_floor
        if gap > 0 and each_lift_position[index] == "U" and user_direction == "U":
            if lift_gap > gap:
                lift_gap = gap
                lift_selected = f"{lift_floor}" + "U"

        # current lift is above the user and the user wants to go down , lift is also going down

        elif gap < 0 and each_lift_position[index] == "D" and user_direction == "D":
            if lift_gap > abs(gap):
                lift_gap = abs(gap)
                lift_selected = f"{lift_floor}" + "D"

        # lift is on the same floor as user in idle condition

        elif gap == 0 and each_lift_position[index] == "":
            lift_selected = f"{lift_floor}"
            break

        # current lift is below the user floor ,but its going up and user wants to go down
        elif gap > 0 and each_lift_position[index] == "U" and user_direction == "D":
            pass

        # current lift is above the user floor but its going down and user wants to go up:
        elif gap < 0 and each_lift_position[index] == "D" and user_direction == "U":
            pass

        # current lift is either above or below the user but its in idle condition:
        elif each_lift_position[index] == "":
            if lift_gap > abs(gap):
                lift_gap = abs(gap)
                lift_selected = f"{lift_floor}"
    print(lift_selected)

    # There are 2 cases to discuss at the end of the program...
    # case 1: If user wants to go down and all lifts are above user floor and going up. In that case we cannot
    # determine which lift will come down, whichever is the first lift that becomes idle.. that will come to user
    # case: 2 is reverse.. user wants to go up but all lifts are below user and going down.. same condition will occur


if __name__ == "__main__":

    lifts()
