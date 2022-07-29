"""
Ideas:
https://math.stackexchange.com/questions/963724/actually-playable-games-based-on-graphs

https://www.cs.colostate.edu/~cs200/Fall16/slides/15-graphs3.pdf

https://cs.stackexchange.com/questions/50937/how-to-generate-graphs-with-a-hamiltonian-path


Game Ideas:
https://play.google.com/store/apps/details?id=com.giantllama.maps

Create an undirected successor-ish graph
add (LOTS of) random edges (no self-edges)
label a node as a start node
Place all the nodes onto the screen
shuffle the nodes and draw random paths between all nodes (that dont intersect)
try to expand these paths to actually make a grid

"""
class Graph(object):
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = [{} for node in range(nodes+1)]
    def initEdges(self):
        for i in range(1,nodes+1):
            self.adj_list[i].add(i-1)
        print(self.adj_list)


numNodes = 10
G = Graph(numNodes)
G.initEdges()