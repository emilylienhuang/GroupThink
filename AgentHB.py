'''
Class representing the agents in the simulation.
The agents must be able to calculate the fraction of their current neighbors playing 1 as well as whether or not they
choose to continue to act.
'''

#need to add some sort of functionality to move slot, set equal to ""
class AgentHB:
    # create an init that defines default values
    def __init__(self):
        # if a node is active, inactive, or the grid slot in unpopulated
        self.active = 0
        self.populated = False
        # location of the agent on the grid
        self.row = 0
        self.column = 0
        # a collection of the current neighbors
        self.neighbors = []
        # count of utility and the node degree
        self.utility = 0
        self.fraction_playing_1 = 0
        self.index = 0
        self.first_run = True

    # activate the agent
    def activate(self, t, global_utility):

        if (len(self.neighbors) > 0):
            f = 1 / len(self.neighbors)
            active_neighbor_benefit = 0
            for neighbor in self.neighbors:
                if neighbor.active == 1:
                    active_neighbor_benefit += 1

            self.utility = f * active_neighbor_benefit - t
            self.active = 1

    # activate the agent
    def assessActivation(self, t, global_utility):

        if (len(self.neighbors)> 0):
            f = (1 / len(self.neighbors))
            active_neighbor_benefit = 0
            for neighbor in self.neighbors:
                if neighbor.active == 1:
                        active_neighbor_benefit += 1

            #if it's not the first iteration check if the agent still wants to act.
            if not self.first_run:
                self.utility = f * active_neighbor_benefit - t
                if (self.utility > 0):
                    self.active = 1
                else:
                    self.utility = 0
                    self.active = 0
            else :
                self.first_run = False



    #calculate the threshold for action that the current agent is at
    def calculateNeighborFractionPlaying1(self):
        for neighbor in self.neighbors:
            if neighbor.active == 1:
                    self.fraction_playing_1 += 1

        if (len(self.neighbors) > 0):
            self.fraction_playing_1 /= len(self.neighbors)
        else:
            self.fraction_playing_1 = 0







