# from cmu_112_graphics import *
from graph import *
from kdtree import *
from randomPoints import *

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import collections as mc
from delaunayTriangulation import *
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
    print(list(triangles)[0].edges)
    lines = [list(tri.edges) for tri in triangles]
    lines = [
        list(edgePair)
        for tri in triangles
        for edgePair in tri.edges
    ]
    lineCol = mc.LineCollection(lines)
    _ , ax = plt.subplots()
    ax.add_collection(lineCol)
    ax.autoscale()
    plt.show()
    # for triangle in triangles:
    #     tri = list(triangle.edges)
        
    #     e1 = tri[0]
    #     e2 = tri[1]
    #     e3 = tri[2]
    #     print(e1,e2,e3)
    #     plt.plot(e1[0],e1[1],color="blue")
    #     plt.plot(e2[0],e2[1],color="blue")
    #     plt.plot(e3[0],e3[1],color="blue")
    
    # nodeList = list(range(numNodes))
    # print(pointList)
    # # maybe use a monte carlo algorithm to get the best permutation of nodes for the game
    # #pointlist and nodeList are parallel

    # hull = np.array(convexHull(pointList))
    # print(hull)
    # for point in pointList:
    #     if point in hull:
    #         plt.plot(point[0],point[1],marker="s",color="red")
    #     else:
    #         plt.plot(point[0],point[1],marker="o",color="blue")
    # plt.show()
    

    # for i,txt in enumerate(nodeList):
    #     for edge in G.adjList[i]:
    #         x1,y1 = pointList[i]
    #         x2,y2 = pointList[edge.ident]
    #         plt.plot((x1+200,x2+200),(y1+200,y2+200),marker="o")

    #     plt.annotate(txt,[200 + pointList[i][j] for j in range(2)])
    
    # plt.show()

    
    # runApp()
