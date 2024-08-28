import math
import random
from AgentHB import *

def generateGraph(N, max_num_friends, active_inactive_split, t, global_utility):
    # generate a list of agents of N length
    agents = [AgentHB() for _ in range(int(math.pow(N,2)))]

    for i, agent in enumerate(agents):
        agent.index = i

    for agent in agents:
        agent.populated = True
        choose_active = random.random()
        if (choose_active <= active_inactive_split):
            # here, we add an active agent
            agent.active = 1
            #update the agent's utility
            agent.assessActivation(t, global_utility)
        else:
            # otherwise we add an inactive party
            agent.active = 0
        for i in range(max_num_friends):
            potential_friend = random.choice(agents)
            if (len(agent.neighbors) < max_num_friends  and len(potential_friend.neighbors) < max_num_friends and agent.index != potential_friend.index):
                #if the other agent is
                agent.neighbors.append(potential_friend)
                potential_friend.neighbors.append(agent)
    return agents


# iterate over the whole grid and create a set of the inactive members and a set of the active members
def wholeGraphUtility(graph, people, inactives, actives):
    new_utility = 0
    for agent in graph:
        if (agent.active == 1):
            new_utility += agent.utility
            if (agent in inactives):
                inactives.remove(agent)
            actives.add(agent)
        else:
            if (agent in actives):
                actives.remove(agent)
            inactives.add(agent)
        people.add(agent)

    return new_utility
