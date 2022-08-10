############################################
# Generate Voronoi Diagram
#   Find the adjancency list of the triangles
#   dfs and connect circumcenters
#   
#       
############################################

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
    
    return newEdgeList#,triangles
