#######################################################################

#   Computing the Voronoi Diagram using a divide and conquer method
#   !! https://www.cs.cmu.edu/afs/cs/project/pscico-guyb/294/class-notes/all/13.ps
#       I found this online and converted to a pdf to understand the algorithm
#   Union random cells to gather a better board
#   check for hamiltonian path
#   TODO:
#       ! Convex Hull
#           ! https://cp-algorithms.com/geometry/convex-hull.html#implementation
#       ! geometric intersection
#       ! 
#       ! https://stackoverflow.com/questions/973094/easiest-algorithm-of-voronoi-diagram-to-implement
#       ! https://www.comp.nus.edu.sg/~tantc/ioi_training/CG/l10cs4235.pdf
#       ! 
#
#
#
#######################################################################



def orientation(a,b,c):
    #perform cross-product to find orientation of points
    ax,ay = a
    bx,by = b
    cx,cy = c
    return (bx-ax) * (cy-ay) - (by-ay) * (cx-ax) 

def lowerHull(P_input,removeLast=False,isSorted=True):
    if not isSorted:
        P_input = sorted(set(P_input),key=lambda x: (-x[1],x[0]))
    lo_hull = []
    for p in P_input:
        while len(lo_hull) >= 2 and orientation(lo_hull[-2],lo_hull[-1],p)<=0:
            lo_hull.pop()
        lo_hull.append(p)
    if removeLast:
        return lo_hull[:-1]
    else:
        return lo_hull

def upperHull(P_input,removeLast=False,isSorted=True):
    if not isSorted:
        P_input = sorted(set(P_input),key=lambda x: (-x[1],x[0]))
    up_hull = []    
    for p in reversed(P_input):
        while len(up_hull) >= 2 and orientation(up_hull[-2],up_hull[-1],p)<=0:
            up_hull.pop()
        up_hull.append(p)
    if removeLast:
        return up_hull[:-1]
    else:
        return up_hull

def convexHull(P_input):
    """
    P_input = list of Point objects
    P_input is from the cmu notes
    """
    P_input = sorted(set(P_input),key=lambda x: (-x[1],x[0]))
    n = len(P_input) #number of vertices
    if n <= 1:
        return P_input
    # print(P_input)

    l_hull = lowerHull(P_input,removeLast=True,isSorted=True)
    u_hull = upperHull(P_input,removeLast=True,isSorted=True)
    """
    I return both the lower and upper hull because the 
    cmu divide and conquer algorithm requires the lower hull
    """
    return l_hull+u_hull

def delaunay(pointList,boundary):
    # if len(tmpHull)==1: #if there are less than or equal to 3 points
    #     #this is the base case (e.g use monotone polygon triangulation)
    #     pass
    # else:
        #assume the list is sorted
        # lowerHull,upperHull = hull
    median = pointList[len(pointList)//2]

    #left side loop
    left_inner = []
    left_hull = []
    for pt in pointList:
        if pt in boundary and pt < pointList[median]:
            left_hull.append(pt)
        elif pt < pointList[median]:
            left_inner.append(pt)
    
    right_inner = []
    right_hull = []
    for pt in pointList:
        if pt in boundary and pt > pointList[median]:
            right_hull.append(pt)
        elif pt < pointList[median]:
            right_inner.append(pt)
    
    splitter = lowerHull(right_inner+right_hull)
    new_left_inner = [pt for pt in left_inner if pt not in splitter]
    new_left_hull = [pt for pt in left_hull if pt in splitter]

    new_right_inner = [pt for pt in right_inner if pt not in splitter]
    new_right_hull = [pt for pt in left_hull if pt in splitter]
    left_result = delaunay(new_left_inner,new_left_hull)
    right_result = delaunay(new_right_inner,new_right_hull)
    return left_result, right_result

def triangulation(pointList):
    pointList.sort()
    boundary = convexHull(pointList,boundary)
    return delaunay(pointList,boundary)
