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
    # pointList = {(x,y) for x in range(0,400,10) for y in range(0,400,10)}
    # pointList=list(pointList)
    # print(pointList)
    pointList = genXYCoords((30,80),numNodes,(width,height))
    # pointList.append((0,0))
    # pointList.append((0,400))
    # pointList.append((400,0))
    # pointList.append((400,400))
    triangles = BowyerWatson(pointList)
    
    centerLines = precompute(triangles)
    centerLines = [list(line) for line in centerLines]
    # lines = [list(tri.edges) for tri in tris]
    centers = [tri.circumCenter for tri in triangles]
    vertices = [
        tuple(vertice)
        for tri in triangles
        for vertice in tri.vertices
    ]
    convex = convexHull(vertices)
    triangles = {
        tri for tri in triangles
        if len((tri.vertices).intersection(convex)) == 0
    }
    lines = [
        list(edgePair)
        for tri in triangles
        for edgePair in tri.edges
    ]
    
    # # print(vertices)
    
    
    # x,y = np.array(convex).T

    lineCol = mc.LineCollection(centerLines)
    lineNew = mc.LineCollection(lines,color="red")
    # points = plt.scatter(x,y)
    _ , ax = plt.subplots()
    ax.add_collection(lineCol)
    ax.add_collection(lineNew)
    # ax.autoscale()
    

    # ax.add_collection(cent)
    ax.set_xlim(0,400)
    ax.set_ylim(0,400)
    plt.show()

        # # print(dualDelaunay(triangles))
    # for tri in triangles:
    #     for edge in tri.edges:
    #         print(dist(tri.circumCenter,edge[1]))
    #         print(edge)
    #         plt.plot(*zip(*edge),color="red")
       
    #     circle = plt.Circle((tri.circumCenter[0],tri.circumCenter[1]),tri.radius)
    #     plt.gca().add_patch(circle)
    #     plt.scatter(tri.circumCenter[0],tri.circumCenter[1],color="red")
    #     plt.show()
    # # plt.xlim(0,400),plt.ylim(0,400)
    # # print(*zip(*centers))
    # # plt.scatter(*zip(*centers))