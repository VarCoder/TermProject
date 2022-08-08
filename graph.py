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
class Node(object):
    def __init__(self,identifier):
        self.ident = identifier
        self.x = None
        self.y = None
    def __repr__(self):
        # return f"Node({self.ident})" #pretty-print
        return f"{self.ident}"
    def __eq__(self,other):
        return isinstance(other,Node) and self.ident==other.ident
    def __hash__(self):
        return hash(self.ident)

class Graph(object):
    def __init__(self,nodeCount):
        self.n = nodeCount
        self.nodes = [Node(i) for i in range(self.n)]
        self.adjList = [set() for tmp in range(self.n)]
    def idToNode(self,id):
        return self.nodes[id]
    def initEdges(self):
        for id in range(0,self.n-1):
            self.adjList[id].add(self.idToNode(id+1))
    def addEdge(self,source,dest):
        if source == dest: return None
        self.adjList[source].add(self.idToNode(dest))
    def getNodeCount(self,maxOutdegree):
        edgeDistSeq = range(maxOutdegree)
        edgeDistWeights =  [0.7]+[0.3/(maxOutdegree-1) for i in range(maxOutdegree-1)]
        return random.choices(edgeDistSeq,weights=edgeDistWeights,k=1)[0]
    def createRandomEdges(self,maxOutdegree):
        for mainNode in self.nodes:
            newNodes = self.getNodeCount(maxOutdegree)
            # print(newNodes)
            # newNodes = random.randrange(0,maxOutdegree)
            while len(self.adjList[mainNode.ident]) <= newNodes:
                otherNode = mainNode.ident + \
                                random.randrange(-mainNode.ident,\
                                self.n - mainNode.ident)

                self.addEdge(mainNode.ident,otherNode)
    # def removeEdge(self,node1,node2):
    #     self.adjList[node1.ident].remove(node2)
    #     self.adjList[node2.ident].remove(node1)
    # def removeNonHamiltonian(self):
    #     for mainNode in self.nodes:
    #         edges = self.adjList[mainNode.ident]
    #         edgeCount = len(edges)
    #         removedEdges = random.randrange(edgeCount-1)
    #         while removedEdges>0:
    #             otherEdge = random.sample(tuple(edges),1)[0]
    #             if otherEdge==mainNode.ident+1:
    #                 break
    #             else:
    #                 self.removeEdge(mainNode,self.nodes[otherEdge])

    def __repr__(self,ind=0):
        res = ""
        for n in range(ind,len(self.adjList)+ind):
            res += f"{n}\n"
        for n in range(ind,len(self.adjList)+ind):
            for item in self.adjList[n]:
                res += f"{n} {item}\n"
        return res

"""Brainstorm:
How should edges be randomly created?
More is better than less
limit the outdegree to be n/2
choose nodes randomly"""

startNode = 0 #fixed because always 0th node

