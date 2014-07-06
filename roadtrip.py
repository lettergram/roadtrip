# Written by Austin Walters for vacation roadtrip algorithm

from random import randint

maxDistance = 270

# Optimal Gas Stoppages
def minimizeStoppingTime(gasStations):
    
    # Base Case
    optimalPathCost = [0]
    previousStation = [0]

    for i in range(1, len(gasStations)):
   
        optimalPathCost.append(999999999)
        previousStation.append(i)

        for j in range(0, i - 1):

            # Calculate penalty points from j to potential station
            penalty = optimalPathCost[j]
            penalty += penaltyFunction(gasStations[j], gasStations[i]);

            # Check to make sure we have enough gas & minimize penalty
            if optimalPathCost[i] > penalty and penalty >= 0:
                optimalPathCost[i] = penalty
                previousStation[i] = j

    # This part just traces the least penalizing path 
    # Starting from the finish to the start
    station = len(previousStation) - 1
    optimizedPath = []
    while station > 0:
        optimizedPath.append(station)
        station = previousStation[station]
    optimizedPath.append(gasStations[0])

    return optimizedPath

# Penalization Function
def penaltyFunction(sourceStation, destinationStation):
    pen = sourceStation - destinationStation + maxDistance
    return pen * pen * pen


# Generates Gas Stations at Random Mile Markers
def generateGasStations(startLoc, endLoc):
    gasStations = [0, endLoc]
    for i in range(startLoc, endLoc, maxDistance):
        divisor = randint(2, 50)
        for j in range(i, i + maxDistance, maxDistance / divisor):
            gasStations.append(randint(i + j, i + j + maxDistance) % 2907)
    return sorted(gasStations)


# Distance from New York to San Francisco, just for kicks                                         
gasStationMileMarker = generateGasStations(0, 2908)
optimizedPath =  minimizeStoppingTime(gasStationMileMarker)
stop = 0

for i in reversed(optimizedPath):
    str = "Stop #%2d" % (stop)
    str += " at Gas Station #%4d " % i
    str += "located at mile marker %4d" % (gasStationMileMarker[i])
    print str
    stop+=1
