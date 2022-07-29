"""
Ideas:
https://math.stackexchange.com/questions/963724/actually-playable-games-based-on-graphs

https://www.cs.colostate.edu/~cs200/Fall16/slides/15-graphs3.pdf

https://cs.stackexchange.com/questions/50937/how-to-generate-graphs-with-a-hamiltonian-path


Game Ideas:
https://play.google.com/store/apps/details?id=com.giantllama.maps

Create an undirected successor-ish graph \this is our hamiltonian path
add (LOTS of) random edges (no self-edges)
label a node as a start node
Place all the nodes onto the screen
shuffle the nodes and draw random paths between all nodes (that dont intersect)
try to expand these paths to actually make a grid

"""
import random
# class Node(object):
#     idToInstance = dict() #id -> 
#     def __init__(self,id):
#         self.id= id
#         if id not in Node.idToInstance:
#             self.x = None
#             self.y = None
#             Node.idToInstance[id] = self
#         else:
#             raise Exception("Node with id {id} already exists")
        
#     def assignXY(self,x_val,y_val):
#         self.x = x_val
#         self.y = y_val
#     def __repr__(self):
#         return str(self.num)
#     def __hash__(self):
#         return hash(self.num)
#     def __eq__(self,other):
#         return self.num == other.num

# class Graph(object):
#     def __init__(self, nodes):
#         self.nodeCount = len(nodes)
#         self.adjList = { n: set() for n in nodes }
#     def initEdges(self):
#         for key, value in self.adjList:
#             value.add(Node(key.displayId + 1))
#     def addEdge(self,source,dest):
#         #destructivly modify adj_list so just return None
#         if dest==source: return None
#         #undirected graph so add both ways
#         self.adjList[source].add(dest)
#         self.adjList[dest].add(source)
#     def getNodeAdjList(self,node):
#         return self.adjList[node]
#     def getAdjList(self):
#         return self.adjList
class Node(object):
    def __init__(self,identifier):
        self.ident = identifier
        self.x = None
        self.y = None
    def __repr__(self):
        return f"Node({self.ident})"
    def __eq__(self,other):
        return isinstance(other,Node) and self.ident==other.ident
    def __hash__(self):
        return hash(self.ident)

class Graph(object):
    def __init__(self,nodeCount):
        self.n = nodeCount
        self.nodes = [Node(i) for i in range(self.n)]
        self.adjList = [set() for tmp in range(self.n)]
#sdasdadasd
    def idToNode(self,id):
        return self.nodes[id]
    def initEdges(self):
        for id in range(0,self.n-1):
            self.adjList[id].add(self.idToNode(id+1))
    def addEdge(self,source,dest):
        if source == dest: return None
        self.adjList[self.idToNode(source)].add(self.idToNode(dest))

numNodes = 10
G = Graph(numNodes)
G.initEdges()
print(G.adjList)
"""Brainstorm:
How should edges be randomly created?
More is better than less
limit the outdegree to be n/2
choose nodes randomly"""
# def createRandomEdges(maxOutdegree):
#     #choose gap greater than 1
#     for node in range(numNodes):
#         newNodes = random.randrange(1,maxOutdegree)
#         while len(G.getNodeAdjList(node)) <= newNodes:
#             shift = random.randrange(-node,numNodes-node+1)
#             G.addEdge(node,shift+node)
startNode = 0 #fixed because always 0th node

