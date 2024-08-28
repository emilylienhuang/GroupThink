'''
Welcome to our grid functions! These functions perform the grid operations.
'''
import numpy as np
from AgentHB import *
import random




# this function populates the grid takes in N, the NxN size parameter of the grid
def initializeGrid(N):
    #create an empty grid to store our agent objects
    grid = np.empty((N+2,N+2), dtype=object)

    #populate the grid with generic empty agent objects or houses
    for i in range(N+2):
        for j in range(N+2):
            #generic construction
            grid[i][j] = AgentHB()

            # set the location of each agent
            grid[i][j].row = i
            grid[i][j].column = j
    return grid



'''
Now, it's time to populate the grid. We will "flip a coin"
to see #1 if an agent will even exist there and #2 what action they will have if they exist.
'''


def populateGrid(grid, N, pct_empty, active_inactive_split, t, global_utility):
     #grid should be coming in as N+2xN+2

     # we want to pad the sides of the grid so there will be no out of bounds errors.
    for i in range(1,N +1):
        for j in range(1,N +1):

            #set the location of the agent on the grid
            grid[i][j].row = i
            grid[i][j].column = j

            #our coin flip to see if an agent will exist in a spot.
            agent_exists = random.random()
            if (agent_exists > pct_empty):
                grid[i][j].populated = True
                # we are going to add an agent because the likelihood of it existing is higher than not
                choose_active = random.random()

                if(choose_active <= active_inactive_split):
                    # here, we add an active agent
                    grid[i][j].active = 1
                else:
                    # otherwise we add an inactive party
                    grid[i][j].active = 0
    # finally, we want to initialize each agent's attributes for neighbors and degree
    populateDegreeAndNeighbors(grid, N, t, global_utility)


# this function populates the degrees,neighbors, and cross type of each node upon grid population
def populateDegreeAndNeighbors(grid, N, t, global_utility):

    # iterate over the squares of the grid for each agent found calculate its degree and neighbors
    for i in range(1,N+2):
        for j in range(1,N+2):
            num_degrees = 0

            if (grid[i][j].populated == True):
                # if a grid slot is populated, iterate over its neighbors
                    for row in range(i-1,i+2):
                        for column in range(j-1, j+2):
                            # index over the 8 slots on the grid around a given point
                            if (i == 0 or j == 0 or i >= N + 1 or j >= N + 1):
                                #don't include OOB
                                break
                            if (not (row == i and column == j)):
                                if (grid[row][column].populated == True):
                                    #if the neighbor is populated up the degrees
                                    num_degrees+=1
                                    grid[i][j].neighbors.append(grid[row][column])


            grid[i][j].degree = num_degrees


# translates a (N+2)x(N+2) padded grid to a 2D numpy array.
def gridToArray(grid):
    N = len(grid[0]) - 2
    # NOTE: excluding the padding to the graph
    array = np.zeros((N,N))
    for i in range(1, N+2):
        for j in range(1,N+2):
            if (grid[i][j].populated == True):
                if(grid[i][j].active == 1):
                    array[i-1][j-1] = 2
                if(grid[i][j].active == 0):
                    array[i-1][j-1] = 1
    return array


# iterate over the whole grid and create a set of the inactive and a set of the active members
def wholeGridUtility(grid, people, inactives, actives):
    new_utility = 0
    N = len(grid) - 2

    for i in range(1, N+2):
        for j in range(1, N+2):
            if (grid[i][j].populated == True):
                if (grid[i][j].active == 1):
                    new_utility += grid[i][j].utility
                    if (grid[i][j] in inactives):
                        inactives.remove(grid[i][j])
                    actives.add(grid[i][j])
                else:
                    if (grid[i][j] in actives):
                        actives.remove(grid[i][j])
                    inactives.add(grid[i][j])

                people.add(grid[i][j])
    return new_utility




