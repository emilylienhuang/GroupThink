from GridOperationsHB import *
import matplotlib.pyplot as plt

def HoardBehaviorD3(N, active_inactive_split, t, pct_empty, alpha=0):

    global_utility = 0

    # create a grid and populate it based on given input values
    grid = initializeGrid(N)
    populateGrid(grid,N,pct_empty,active_inactive_split, t, global_utility)

    # initialize the sets of agents
    people = set()
    inactives = set()
    actives = set()

    # populate the sets of agents
    global_utility = wholeGridUtility(grid, people, inactives, actives)

    # runtime counter in case need to stop based on iteration
    runtime = 0
    # iterate while there is no consensus or less than threshold
    while (inactives and actives and runtime < 2500):
        # increment iteration count
        runtime += 1

        # choose a random agent
        person = people.pop()
        location = (person.row, person.column)

        # choose action of player
        person.calculateNeighborFractionPlaying1()
        person.assessActivation(t, global_utility)
        grid[location[0]][location[1]] = person

        # update global utility
        global_utility = wholeGridUtility(grid, people, inactives, actives)

    return global_utility

# this function returns the average CTF of 10 runs of the given input parameters holding n constant at 30 active_inactive_split, t, pct_empty, tax)
def averageUtility(active_inactive_split, t, pct_empty,alpha=0):

    #store the average ctf
    ctf_ave = 0
    for _ in range(10):
        ctf_ave += HoardBehaviorD3(30,active_inactive_split,t, pct_empty, alpha)

    return ctf_ave / 10


def generateUtilityActiveInactive():
    utility_ave = []
    x = []
    for i in range(19):
        active_inactive_split = ((i + 1) * 5) / 100
        x.append(active_inactive_split)
        utility_ave.append(averageUtility(active_inactive_split, 0.5, 0.3))

    plt.scatter(x, utility_ave)
    plt.xlabel("active_inactive_split")
    plt.ylabel("Average Utility")
    plt.title("AverageUtility vs active_inactive_split: N = 30,t=50%, %empty=30")
    plt.show()

#uncomment the line below to generate plot
generateUtilityActiveInactive()

def generateUtilityT():
    utility_ave = []
    x = []
    for i in range(19):
        t = ((i + 1) * 5) / 100
        x.append(t)
        utility_ave.append(averageUtility(0.5, t, 0.3))

    plt.scatter(x, utility_ave)
    plt.xlabel("threshold for action")
    plt.ylabel("Average Utility")
    plt.title("AverageUtility vs t: N = 30,%active=50, %empty=30")
    plt.show()

#uncomment the line below to generate plot
generateUtilityT()

def generateUtilityvPctEmpty():
    utility_ave = []
    x = []
    for i in range(39):
        pct_empty = ((i + 1) * 2.5) / 100
        x.append(pct_empty)
        utility_ave.append(averageUtility(0.5, 0.5, pct_empty))


    plt.scatter(x, utility_ave)
    plt.xlabel("pct_empty")
    plt.ylabel("Average Utility")
    plt.title("AverageUtility vs pct_empty: N = 30,active_split=50%, t=50%")
    plt.show()
#uncomment the line below to generate plot
generateUtilityvPctEmpty()



