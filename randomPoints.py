"""
generate random (x,y) points
shuffle range of size node count
    (1) overgenerate points and use kdTree to filter
    (2) poisson disc sampling
    (3) generate n*n points and randomly select using .sample
    (4) create a random start node, randomly select coordinates and create new ones if kd_tree says in valid distance
Both (1),(2),(4) use kd-tree
"""
import random
from kdtree import *
# random.seed(1)
def randomPoint(canvasBounds):
    x = random.randrange(0,canvasBounds[0])
    y = random.randrange(0,canvasBounds[1])
    return (x,y)

def genXYCoords(minMaxDist,numPoints,canvasBounds):
    
    startnode = randomPoint(canvasBounds)
    res = [startnode]
    pointTree = kdTree(res)
    counter = 0
    while len(res) < numPoints:
        if counter > 1000:
            res = [startnode]
            pointTree.reset(res) #soft reset
            counter = 0
        candidate = randomPoint(canvasBounds)
        if candidate in res:
            continue
        
        node, dist = pointTree.findNeighbor(candidate)
        # print(dist)
        if minMaxDist[0] <= dist <= minMaxDist[1]:
            res.append(candidate)
            pointTree.insertNode(candidate)
        counter += 1
    # printTree(pointTree.tree)
    return res

