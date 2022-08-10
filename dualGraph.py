############################################
# Generate Voronoi Diagram
#   Find the adjancency list of the triangles
#   dfs and connect circumcenters
#   
#       
############################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)
def almostEqualPoint(point,point2):
    return almostEqual(point[0],point2[0]) and almostEqual(point[1],point2[1])

def precompute(triangles):
    # dict : key = frozen set of edge, value = set of circumcenters
    res = dict()
    for tri in triangles:
        for edge in tri.edges:
            key = frozenset(edge)
            res[key] = (res.get(key,set())).union([tri.circumCenter])
            
    newEdgeList = set()
    edgeAdj = dict()
    for _, centers in res.items():
        for center1 in centers:
            for center2 in centers:
                if center1 == center2: continue
                if not (0<=center1[0]<=400 and 0<=center2[0]<=400) or not (0<=center1[1]<=400 and 0<=center2[1]<=400):
                    # print([edge for tri in triangles for edge in tri.edges])
                    rev = lambda x : (x[1],x[0])
                    triangles = {
                        tri
                        for tri in triangles
                        for edge in tri.edges
                        if center1 not in edge and rev(center1) not in edge and center2 not in edge and rev(center2) not in edge
                    }
                    # continue 

                newEdgeList.add(frozenset([center1,center2]))
                edgeAdj[center1] = (edgeAdj.get(center1,set())).union(center2)
    
    return newEdgeList

def searchID(visited,targetVert):
    for vertex,assocID in visited:
        if almostEqualPoint(vertex,targetVert):
            return assocID
    return None


def getAdjList(triangles):
    visited = []
    cnt = 0
    adjList = []
    for tri in triangles:
        for edge in tri.edges:
            newEdgeIds = []
            for vertex in edge:
                foundID = searchID(visited,vertex)
                if foundID == None:
                    visited.append((vertex,cnt))
                    adjList.append(set())
                    foundID = cnt
                    cnt+=1
                newEdgeIds.append(foundID)
            [src,dst] = newEdgeIds
            adjList[src].add(dst)
            adjList[dst].add(src)
    return adjList