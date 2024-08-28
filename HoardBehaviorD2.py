from AgentHB import *
from GridOperationsHB import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def HoardBehaviorD2(N, active_inactive_split, t, pct_empty, alpha=0):
    #store the frames of our visualization
    utility = []

    global_utility = 0

    # create a grid and populate it based on given input values
    grid = initializeGrid(N)
    populateGrid(grid,N,pct_empty,active_inactive_split, t, global_utility)

    # storage for empty slots and the discontent neighbors
    people = set()
    inactives = set()
    actives = set()

    # populate the discontent nodes
    global_utility = wholeGridUtility(grid, people, inactives,actives)

    # runtime counter in case need to stop based on iteration
    runtime = 0
    # iterate while there are discontent agents or runtime is less than threshold
    while (inactives and actives and runtime < 2500):
        # increment iteration count
        runtime += 1

        # choose a random person
        person = people.pop()
        location = (person.row, person.column)

        # calculate peer pressure
        person.calculateNeighborFractionPlaying1()
        person.assessActivation(t, global_utility)
        grid[location[0]][location[1]] = person

        # update global utility
        global_utility = wholeGridUtility(grid, people, inactives, actives)

        utility.append(global_utility)


    return utility


def generatePlots():


    for i in range(10):
        ctf = HoardBehaviorD2(30, 0.5, 0.2, 0.3)

        x = [i for i in range(len(ctf))]
        plt.scatter(x, ctf)
        plt.xlabel("Runtime")
        plt.ylabel("Utility")
        plt.title("Utility Change: N = 30, %active = 0.50, t=0.20, %empty=0.30")
    plt.show()

    for i in range(10):
        ctf = HoardBehaviorD2(30, 0.7, 0.2, 0.3)

        x = [i for i in range(len(ctf))]
        plt.scatter(x, ctf)
        plt.xlabel("Runtime")
        plt.ylabel("Utility")
        plt.title("Utility Change: N = 30, %active = 0.70, t=0.20, %empty=0.30")
    plt.show()

    for i in range(10):
        ctf = HoardBehaviorD2(30, 0.5, 0.2, 0.1)

        x = [i for i in range(len(ctf))]
        plt.scatter(x, ctf)
        plt.xlabel("Runtime")
        plt.ylabel("Utility")
        plt.title("Utility Change: N = 30, %active = 0.50, t=0.20, %empty=0.10")
    plt.show()



    for i in range(10):
        ctf = HoardBehaviorD2(30, 0.5, 0.7, 0.3)

        x = [i for i in range(len(ctf))]
        plt.scatter(x, ctf)
        plt.xlabel("Runtime")
        plt.ylabel("Utility")
        plt.title("Utility Change: N = 30, %active = 0.50, t=0.7, %empty=0.30")
    plt.show()


# uncomment to generate plots
generatePlots()