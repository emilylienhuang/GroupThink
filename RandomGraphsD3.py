from GraphOperations import *
import matplotlib.pyplot as plt


def RandomGraphsD3(N, active_inactive_split, t, max_friends):

    global_utility = 0

    graph = generateGraph(N,max_friends,active_inactive_split, t, global_utility)

    # storage for sets of people
    people = set()
    inactives = set()
    actives = set()

    # populate the sets
    global_utility = wholeGraphUtility(graph, people, inactives, actives)

    # runtime counter in case need to stop based on iteration
    runtime = 0
    # iterate while there is no consensus and less than runtime
    while (inactives and actives and runtime < 2500):
        # increment iteration count
        runtime += 1

        # choose a random person
        person = people.pop()

        # calculate peer pressure
        person.calculateNeighborFractionPlaying1()
        person.assessActivation(t, global_utility)


        # update global utility
        global_utility = wholeGraphUtility(graph, people, inactives, actives)



    return global_utility

# this function returns the average global utility of 10 runs
# of the given input parameters holding n constant at 30 active_inactive_split, t, max_friends)
def averageUtility(active_inactive_split, t, max_friends):

    #store the average utility
    util_ave = 0
    for _ in range(10):
        util_ave += RandomGraphsD3(30,active_inactive_split,t, max_friends)

    return util_ave / 10

#generate the active inactive plot
def generateUtilityActiveInactive():
    utility_ave = []
    x = []
    for i in range(19):
        active_inactive_split = ((i + 1) * 5) / 100
        x.append(active_inactive_split)
        utility_ave.append(averageUtility(active_inactive_split, 0.5, 3))

    plt.scatter(x, utility_ave)
    plt.xlabel("active_inactive_split")
    plt.ylabel("Average Utility")
    plt.title("AverageUtility vs active_inactive_split: N = 30,t=50%, max_friends=3")
    plt.show()

#uncomment the line below to generate plot
generateUtilityActiveInactive()


#generate the t plot
def generateUtilityT():
    utility_ave = []
    x = []
    for i in range(19):
        t = ((i + 1) * 5) / 100
        x.append(t)
        utility_ave.append(averageUtility(0.5, t, 3))

    plt.scatter(x, utility_ave)
    plt.xlabel("threshold for action")
    plt.ylabel("Average Utility")
    plt.title("AverageUtility vs t: N = 30,%active=50, max_friends=3")
    plt.show()

#uncomment the line below to generate plot
generateUtilityT()

#generate the pct_empty plot
def generateUtilityvPctEmpty():
    utility_ave = []
    x = []
    for i in range(20):
        max_friends = i
        x.append(max_friends)
        utility_ave.append(averageUtility(0.5, 0.2, max_friends))


    plt.scatter(x, utility_ave)
    plt.xlabel("max_friends")
    plt.ylabel("Average Utility")
    plt.title("AverageUtility vs max_friends: N = 30,active_split=50%, t=20%")
    plt.show()
#uncomment the line below to generate plot
generateUtilityvPctEmpty()



