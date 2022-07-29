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

class Graph():
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = [set() for node in range(nodes+1)]
    def initEdges(self):
        for i in range(0,self.nodes):
            self.adj_list[i].add(i+1)
    def addEdge(self,source,dest):
        #destructivly modify adj_list so just return None
        if dest==source: return None
        #undirected graph so add both ways
        self.adj_list[source].add(dest)
        self.adj_list[dest].add(source)

numNodes = 10
G = Graph(numNodes)
G.initEdges()

