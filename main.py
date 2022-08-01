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
    G.createRandomEdges(4)
  
    pointList = genXYCoords((100,200),numNodes,(width,height))
    # pointList.sort(key=lambda x : x[1])
    nodeList = list(range(numNodes))
    # random.shuffle(nodeList)
    # maybe use a monte carlo algorithm to get the best permutation of nodes for the game
    print(pointList,nodeList)
    #pointlist and nodeList are parallel

    data = np.array(pointList)
    x,y = data.T
    plt.scatter(x,y)
    for i,txt in enumerate(nodeList):
        # x1 = pointList[i]
        # for edge in G.adjList[i]:
        for edge in G.adjList[i]:
            x1 = pointList[i]
            x2 = pointList[edge.ident]
            # print(x1,x2)
            plt.axline(x1,x2,marker="o")
        # print(pointList[i])
        # plt.plot()
        plt.annotate(txt,pointList[i])
        plt.xlim(0,400), plt.ylim(0,400)
    plt.show()

    # printTree(x)
    # runApp()
