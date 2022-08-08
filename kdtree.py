"""
https://en.wikipedia.org/wiki/K-d_tree

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

def printTree(node):
    if node != None and node.value != None:
        printTree(node.leftChild)
        print(' ' * 4 * node.depth + '-> ' + str(node))
        printTree(node.rightChild)
    
class kdTreeNode(object):
    def __init__(self,val,depth,lc = None, rc = None):
        self.value = val
        self.leftChild = lc
        self.rightChild = rc
        self.depth = depth
    def __repr__(self):
        return f"{self.value}"
def buildkdTree(pointList,depth=0,dim=2):
    #! largely based off of psuedocode at start of file
    if len(pointList) == 0:
        return kdTreeNode(None,depth)
    axis = depth%dim #axis is 0 or 1 (x,y respectively)

    pointList.sort(key = lambda i : i[axis])
    medianIndex = len(pointList)//2
    median = pointList[medianIndex]
    return kdTreeNode(median,depth,
        buildkdTree(pointList[:medianIndex],depth+1),
        buildkdTree(pointList[medianIndex+1:],depth+1)
    )
def insertNode(tree,point,depth=0):
    #! based off https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/kdtrees.pdf
    # printTree(tree)
    cd = depth%2
    if tree == None:
        tree = kdTreeNode(point,depth)
    elif tree.value == None:
        tree = kdTreeNode(point,tree.depth)
    elif tree.value == point:
        raise Exception("Attempted to insert duplicate node")
    elif point[cd] < tree.value[cd]:
        tree.leftChild = insertNode(tree.leftChild,point,depth+1)
    else:
        tree.rightChild = insertNode(tree.rightChild,point,depth+1)
    return tree
def dist(point1,point2):
    x1 = point1.value[0] 
    x2 = point2.value[0]
    y1 = point1.value[1]
    y2 = point2.value[1]
    return ((x2-x1)**2 + (y2-y1)**2)**0.5



def nearestNeighbor(tree,node):
    res=kdTreeNode(None,0)
    pointDist=0
    def nearestNeighborSearch(tree,node):
        #! info gathered from https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/kdtrees.pdf
        #! https://johnlekberg.com/blog/2020-04-17-kd-tree.html
        nonlocal res,pointDist
        if tree == None or tree.value == None:
            return None
        hypot = dist(tree,node)
        if not pointDist or hypot < pointDist:
            res = kdTreeNode(tree.value,tree.depth)
            pointDist=hypot
            
        axis = tree.depth%2
        closeEnough = (node.value[axis] - tree.value[axis])**2<=pointDist
        if node.value[axis] - tree.value[axis] <= 0:
            nearestNeighborSearch(tree.leftChild,node)
            if closeEnough: nearestNeighborSearch(tree.rightChild,node)
        else:
            nearestNeighborSearch(tree.rightChild,node)
            if closeEnough: nearestNeighborSearch(tree.leftChild,node)
    # res=kdTreeNode(None,0)
    # pointDist=0
    kdnode = kdTreeNode(node,0)
    nearestNeighborSearch(tree,kdnode)
    return res, pointDist

class kdTree(object):
    def __init__(self,pointList):
        self.pointList = pointList
        self.tree = buildkdTree(self.pointList)
    def getTree(self):
        return self.tree
    def findNeighbor(self,node):
        return nearestNeighbor(self.tree,node)
    def insertNode(self,node):
        self.tree = insertNode(self.tree,node)
    def reset(self,pointList):
        self.__init__(pointList)
    #? pointList is in the form [(x1,y1),(x2,y2)...(x_n,y_n)]
