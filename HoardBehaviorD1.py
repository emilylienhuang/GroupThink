from AgentHB import *
from GridOperationsHB import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
'''
NOTE: function calls to generate deliverables are commented out and must be uncommented to execute code.
This is the visualization implementation used for deliverable 1.
There are four functions:
1. the actual schelling segregation simulation function
2. the animation gif generation function (code courtesy of Dr. Brown)
3. display frames function which displays the first 6 frames of an animation
4. display first and last frames of an animation function.
'''
def HoardBehaviorD1(N, active_inactive_split, t, pct_empty):
    #store the frames of our visualization
    frames = []

    global_utility = 0

    # create a grid and populate it based on given input values
    grid = initializeGrid(N)
    populateGrid(grid,N,pct_empty,active_inactive_split, t, global_utility)
    frames.append(gridToArray(grid))

    # storage for agents
    people = set()
    inactives = set()
    actives = set()


    # populate agent sets
    global_utility = wholeGridUtility(grid, people, inactives, actives)

    # runtime counter in case need to stop based on iteration
    runtime = 0
    # iterate while there is no consensus and runtime less than threshold
    while(inactives and actives and runtime < 1500):
        #increment iteration count
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

        #update the frames for the visualization
        frames.append(gridToArray(grid))

    data = np.stack(frames)
    return data


"""
Created on Thu Feb 17 16:44:09 2022

@author: Philip Brown
"""


def display_animation(data, frame_ms=33, fignum=13, saveFile='animation.gif'):
    '''
    Creates animation

    Parameters
    ----------
    data : numpy array with shape (T,N,N)
        T is number of frames, N is number of pixels on each side of
        square grid.
    frame_ms : int, optional
        Number of milliseconds to draw each frame. The default is 33.
    fignum : int, optional
        The desired pyplot figure to plot in. The default is 13 for luck.

    Returns
    -------
    animation object.
    NOTE: This object must be kept in memory as long as you wish to view the
    animation; otherwise garbage collection will remove it. This means the
    function return needs to be assigned to a variable.

    Example:
    anim = display_animation(load_json_file())

    '''
    fig = plt.figure(fignum)
    #MATSHOW will export the frames, plt.matshow is what to use there
    myplot = plt.matshow(data[0], fignum=fignum)
    num_frames = data.shape[0]

    def update(j):
        myplot.set_data(data[j])
        return [myplot]

    anim = FuncAnimation(fig,
                         update,
                         frames=num_frames,
                         interval=frame_ms,
                         repeat=True,
                         save_count=num_frames)
    if saveFile is not None:
        anim.save(saveFile)
    return anim

import matplotlib.pyplot as plt

'''
Written cross-referencing Dr.Brown's code and ChatGPT
Displays visually the first 6 or all if iteration is less than 6 visualizations of the grid upon iteration.
'''
def display_frames(data, fignum=13, saveFiles=False, savePrefix='frame'):

    num_frames = min(6,data.shape[0])
    frames = []  # List to store frames if needed

    for i in range(num_frames):
        plt.figure(fignum)
        plt.matshow(data[i], fignum=fignum)
        plt.title(f"Frame {i}")

        if saveFiles:
            plt.savefig(f"{savePrefix}_{i}.png")  # save each frame as PNG
        else:
            plt.show()  # display the frame

        plt.close(fignum)  # close the figure to free memory

    # optionally, return the frames list if you need it for further processing
    # return frames

'''
Written cross-referencing Dr.Brown's code and ChatGPT. 
Displays the initial and end configurations of the grid.
'''
def display_first_and_last(data, fignum=13, saveFiles=False, savePrefix='frame'):
    # Ensure there is at least one frame to display
    if data.shape[0] > 0:
        # Indices for the first and last frame
        indices = [0, data.shape[0] - 1] if data.shape[0] > 1 else [0]

        for i in indices:
            plt.figure(fignum)
            plt.matshow(data[i], fignum=fignum)
            plt.title(f"Frame {i}")

            if saveFiles:
                plt.savefig(f"{savePrefix}_{i}.png")  # Save the frame as PNG
            else:
                plt.show()  # Display the frame

            plt.close(fignum)  # Close the figure to free memory


#test driver
def createVisualizations():

    visualization1 = HoardBehaviorD1(10,0.5,0.2,0.3)
    #uncomment if desired:
    display_animation(visualization1)
    #display_frames(visualization1)
    display_first_and_last(visualization1)

createVisualizations()