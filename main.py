# from cmu_112_graphics import *
import enum
from graph import *
from kdtree import *
from randomPoints import *

import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    """Goals:
    perspective camera
    minimap
    background graphics
    potentially moving platforms
    fancy art with platform
    fancy drawing for hamiltonian path
    """
    width = 400
    height = 400
    numNodes = 10
    G = Graph(numNodes)
    G.initEdges()
    G.createRandomEdges(numNodes//4)
  
    pointList = genXYCoords((100,200),numNodes,(width,height))

    nodeList = list(range(numNodes))
    random.shuffle(nodeList)
    print(pointList,nodeList)
    #pointlist and nodeList are parallel

    data = np.array(pointList)
    x,y = data.T
    plt.scatter(x,y)
    for i,txt in enumerate(nodeList):
        plt.annotate(txt,pointList[i])
    plt.show()

    # printTree(x)
    # runApp()
