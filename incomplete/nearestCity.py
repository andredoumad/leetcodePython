# Andre Doumad
# 200830
'''
Position: New Grad 2021

Amazon has Fulfillment Centers in multiple cities within a large geographic region. The cities are arranged on a group that has been divided up like an ordinary Cartesian plane. Each city is located at an integral(x,y) coordinate intersection. City names and locations are given in the form of three arrays: c,x, and y, which are aligned by the index to provide the city name (c[i]), and its coordinates, (x[i],y[i]).

Write an algorithm to determine the name of the nearest city that shares an x or a y coordinate with the queried city. If no cities share an x or y coordinate, return none. If two cities have the same distance to the queried city, q[i], consider the one with an alphabetically smaller name (e.e 'ab' < 'aba' < 'abb') as the closest choice.

The distance is denoted on a Euclidean plan: the difference in x plus the difference in y.

Input
the input to the function/method consists of six arguments:
numOfCities, an integer representing the number of cities;
cities, a list of strings representing the names of each city[i];
xCoordinates, a list of integers representing the X-coordinates of each city[i];
yCoordinates, a list of integers representing the Y-coordinates of each city[i];
numOfQueries, an integer representing the number of queries;
queries, a list of strings representing the names of the queried cities.

Output
Return a list of strings representing the name of the nearest city that shares either an x or a y coordinate with the queried city.

Constraints
1 ≤ numOfCities, numOfQueries ≤ 10^5
1 ≤ xCoordinates[i], yCoordinates[i] <= 10^9
1 ≤ length of queries[i] and cities[i] ≤ 10

Note
Each character of all c[i] and q[i] is in the range ascii[a-z, 0-9,-]
All city name values, c[i] are unique. All cities have unique coordinates.

Example:

Input:

numOfCities = 3
cities = ["c1", "c2", "c3"]
xCoordinates = [3,2,1]
yCoordinates = [3,2,3]
numOfQueries = 3
queries = ["c1", "c2", "c3"]

Output:

[c3, None, c1]


'''

import heapq
def nearestCityShared(numOfCities, cities, xCoordinates, yCoordinates, numOfQueries, queries):
    def distance(x1, y1, x2, y2):
        return abs(x1-y1) + abs(x2-y2)
        
    def query(numOfCities, cities, xCoordinates, yCoordinates, query):
        q_city = cities.index(query)
        q_city_coords = [xCoordinates[q_city], yCoordinates[q_city]]

        heap = []
        
        for n in range(numOfCities):
            if xCoordinates[n] == q_city_coords[0] and yCoordinates[n] == q_city_coords[1]:
                continue
            elif xCoordinates[n] == q_city_coords[0] or yCoordinates[n] == q_city_coords[1]:
                heapq.heappush(heap, [distance(xCoordinates[n], q_city_coords[0], yCoordinates[n], q_city_coords[1]), cities[n]])
        #Breaking condition
        if len(heap) == 0:
            return None
        
        #Selecting all cities with the minimum distance
        min_dist = heap[0][0]
        closest_cities = []
        while heap and heap[0][0] == min_dist:
            closest_cities.append(heapq.heappop(heap)[1].lower()) #append the city name
        
        #Unicode-based alphabetical tie breakers
        return min(closest_cities)

    return [query(numOfCities, cities, xCoordinates, yCoordinates, q) for q in queries] 

print(nearestCityShared(3, ["c1", "c2", "c3"], [3,2,1], [3,2,3], 3, ["c1", "c2", "c3"]))