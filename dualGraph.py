############################################
# Generate Voronoi Diagram
#   Find perpendicular bisectors
#       Store by slope and (x,y) from the midpoint
#   
#       
############################################
def voronoiVertices(triangles):
    res = dict()
    for tri in triangles:
        for vert in tri.vertices:
            # print(vert)
            edgeSet = res.get(vert,set())
            
            res[vert] = edgeSet.union({
                edge for edge in tri.edges
                if vert in edge
            })
    return res
def dualDelaunay(triangles):
    return voronoiVertices(triangles)
