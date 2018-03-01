import random
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

"simple agents model"

class Agent:
    def __init__(self):
        # init with a a random 3 element vector between 0 and 255
        self.weights = [ int( random.random() * 255 ) for i in range(3) ]
        self.len = len(self.weights) - 1
        self.dominance = random.random()

    def interact(self, other):
        """
        Check to see if the other has a larger dominance factor
        and if it does replace a random weight with the weight from the other.
        """
        i = random.randint(0, self.len)
        if self.dominance > other.dominance:
            self.weights[i] = other.weights[i]
        else:
            other.weights[i] = self.weights[i]

def get_weights(agents):
    weights = []
    for a in agents:
        weights.append(a.weights)
    return np.asarray( weights, dtype='uint8' )

def run():
    # init the people
    peeps = []
    for i in range(2000):
        peeps.append( Agent() )

    loops = 3000
    snapshots = []
    for i in tqdm( range(loops) ):
        for peep in peeps:
            # pick a random peep
            other = random.choice( peeps )

            # and interact with them
            peep.interact( other )
        snapshots.append( get_weights( peeps ) )
    snapshots = np.asarray(snapshots)

    # use when the number of iterations is greater than the number of agents
    snapshots = np.rot90(snapshots, 1)

    plt.imshow( snapshots )
    plt.show()

if __name__ == '__main__':
    run()