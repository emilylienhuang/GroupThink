from AgentHB import *
import matplotlib.pyplot as plt
from GraphOperations import *


def RandomGraphsD2(N, active_inactive_split, t, max_num_friends):
    #store global utility over the run of the model
    utility = []

    global_utility = 0
    graph = generateGraph(N,max_num_friends,active_inactive_split, t, global_utility)

    # storage for empty slots and the discontent neighbors
    people = set()
    inactives = set()
    actives = set()

    # populate the discontent nodes
    global_utility = wholeGraphUtility(graph, people, inactives,actives)

    # runtime counter in case need to stop based on iteration
    runtime = 0
    # iterate while there are discontent agents or runtime is less than threshold
    while (inactives and actives and runtime < 2500):
        # increment iteration count
        runtime += 1

        # pop one of the discontented agents and move them
        person = people.pop()

        # calculate peer pressure
        person.calculateNeighborFractionPlaying1()
        person.assessActivation(t, global_utility)

        # update global utility
        global_utility = wholeGraphUtility(graph, people, inactives, actives)

        utility.append(global_utility)


    return utility


def generatePlots():
    for i in range(10):
        ctf = RandomGraphsD2(30, 0.5, 0.2, 5)

        x = [i for i in range(len(ctf))]
        plt.scatter(x, ctf)
        plt.xlabel("Runtime")
        plt.ylabel("Utility")
        plt.title("Utility Change: N = 30, %active = 0.50, t=0.20, max_friends=5")
    plt.show()

    for i in range(10):
        ctf = RandomGraphsD2(30, 0.7, 0.2, 5)

        x = [i for i in range(len(ctf))]
        plt.scatter(x, ctf)
        plt.xlabel("Runtime")
        plt.ylabel("Utility")
        plt.title("Utility Change: N = 30, %active = 0.70, t=0.20, max_friends=5")
    plt.show()

    for i in range(10):
        ctf = RandomGraphsD2(30, 0.5, 0.2, 1)

        x = [i for i in range(len(ctf))]
        plt.scatter(x, ctf)
        plt.xlabel("Runtime")
        plt.ylabel("Utility")
        plt.title("Utility Change: N = 30, %active = 0.50, t=0.20, max_friends=1")
    plt.show()

    for i in range(10):
        ctf = RandomGraphsD2(30, 0.5, 0.7, 5)

        x = [i for i in range(len(ctf))]
        plt.scatter(x, ctf)
        plt.xlabel("Runtime")
        plt.ylabel("Utility")
        plt.title("Utility Change: N = 30, %active = 0.50, t=0.70, max_friends=5")
    plt.show()

# uncomment to generate plots
generatePlots()