# Given the GPS coordinates of 4 arbitrary cities, A, B, C and D, find the shortest flight route
# between the 4 cities along the surface of the earth if your journey starts at A

# The input co-ordinates are treated as a single string so they need to put inside quotes ""
# ex: "51.5074 N, 0.1278 W"


import math

# this function calculates the distance between to points on the surface of the sphere given its co-ordinates
# using the formula given by haversine method


def haversine(coordinate_1, coordinate_2):
    R = 6372800  # Earth radius in meters
    latitude_1, longitude_1 = coordinate_1[0], coordinate_1[1]
    latitude_2, longitude_2 = coordinate_2[0], coordinate_2[1]
    alpha_1, alpha_2 = math.radians(latitude_1), math.radians(latitude_2)
    delta_alpha = math.radians(latitude_2 - latitude_1)
    delta_lambda = math.radians(longitude_2 - longitude_1)
    a = math.sin(delta_alpha / 2) ** 2 + \
        math.cos(alpha_1) * math.cos(alpha_2) * math.sin(delta_lambda / 2) ** 2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


# This function will take the 4 city co-ordinate inputs and result the out as expected
# Direction NORTH , WEST are considered positive in terms of co-ordinate system
# Direction SOUTH , EAST are considered negative in terms of co-ordinate system


def city_distance():
    coordinate_list = list()
    coordinate_city_A = input("Enter the city A co-ordinates:  ")
    coordinate_city_B = input("Enter the city B co-ordinates:  ")
    coordinate_city_C = input("Enter the city C co-ordinates:  ")
    coordinate_city_D = input("Enter the city D co-ordinates:  ")
    coordinate_list.append(coordinate_city_A)
    coordinate_list.append(coordinate_city_B)
    coordinate_list.append(coordinate_city_C)
    coordinate_list.append(coordinate_city_D)
    negative_directions = ["S", "W"]
    A = []
    B = []
    C = []
    D = []
    city_list = [A, B, C, D]
    for index, coordinate in enumerate(coordinate_list):
        for coord in coordinate.split(", "):
            if coord.split(" ")[1] in negative_directions:
                city_list[index].append(-float(coord.split(" ")[0]))
            else:
                city_list[index].append(float(coord.split(" ")[0]))

    distance_dict = {}
    distance_list = []
    city_index_dict = {
        0: "A",
        1: "B",
        2: "C",
        3: "D"
    }
    i = 1
    for city in city_list[1:]:
        distance = haversine(city_list[0], city)
        distance_dict[distance] = city_index_dict[i]
        distance_list.append(distance)
        i += 1
    distance_list.sort()
    output = "A"
    for distance in distance_list:
        output = output + " to " + distance_dict[distance]
    print(output)


if __name__ == "__main__":
    city_distance()
