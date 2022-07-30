"""
function kdtree (list of points pointList, int depth)
{
    // Select axis based on depth so that axis cycles through all valid values
    var int axis := depth mod k;

    // Sort point list and choose median as pivot element

    select median by axis from pointList;

    // Create node and construct subtree
    node.location := median;
    node.leftChild := kdtree(points in pointList before median, depth+1);
    node.rightChild := kdtree(points in pointList after median, depth+1);
    return node;
}
"""


# def drawNode(node):

class kdTreeNode(object):
    def __init__(self,loc, lc = None, rc = None):
        self.location = loc
        self.leftChild = lc
        self.rightChild = rc
    def __repr__(self):
        return f"\t{self.location}\n\t{self.leftChild},{self.rightChild}"
def buildkdTree(pointListX,pointListY,depth=0):
    
    if len(pointListX) == 0 or len(pointListY)==0:
        return None
    dim = 2 #our working dimension is fixed
    axis = depth%dim #axis is 0 or 1 (x,y respectively)
    if axis == 0:
        medianIndex = len(pointListX)//2
        median = pointListX[medianIndex]
    else:
        medianIndex = len(pointListY)//2
        median = pointListY[medianIndex]
    
    return kdTreeNode(median,
        buildkdTree(pointListX[:medianIndex],pointListY[:medianIndex],depth+1),
        buildkdTree(pointListX[medianIndex+1:],pointListY[medianIndex+1:],depth+1)
    )

def kdTree(pointList):
    sortedPointListX = sorted(pointList,key=lambda x : x[0])
    sortedPointListY = sorted(pointList,key=lambda x : x[1])
    return buildkdTree(sortedPointListX,sortedPointListY)
    #? pointList is in the form [(x1,y1),(x2,y2)...(x_n,y_n)]

x = kdTree([(1,2),(2,3)])
print(x)