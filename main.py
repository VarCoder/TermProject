# from cmu_112_graphics import *
from graph import *
from kdtree import *
from randomPoints import *

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import collections as mc
from delaunayTriangulation import *
from dualGraph import *
from bowyerWatson import *
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
    numNodes = 100
    random.seed()
    G = Graph(numNodes)
    G.initEdges()
    G.createRandomEdges(3)

    pointList = genXYCoords((10,100),numNodes,(width,height))
    triangles = BowyerWatson(pointList)
    lines = [list(tri.edges) for tri in triangles]
    lines = [
        list(edgePair)
        for tri in triangles
        for edgePair in tri.edges
    ]
    print(dualDelaunay(triangles))
    lineCol = mc.LineCollection(lines)
    _ , ax = plt.subplots()
    ax.add_collection(lineCol)
    ax.autoscale()
    plt.show()
