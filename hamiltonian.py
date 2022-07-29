#create a starting node at some coordinate (let's say (0,0))
#create a list of transformations in (theta,magnitude) to this starting coord to make new points

import math

"""
https://math.stackexchange.com/a/130528
https://www.angelfire.com/space2/m_kaykobad/publications/Ham_path.pdf
    Let G = (V, E) be a connected graph with n vertices.
    If for all pairwise nonadjacent vertex-triples u, v, and w it holds that 
    d(u) + d(v) + d(w) >= 1/2(3n-5)        | d(x) denotes the degree of a node x
    then G has a Hamiltonian path.

    If G is a simple graph (no repeated edges or self-edges) on n vertices and d(u)+d(v)≥n-1 
    whenever u and v are not adjacent, then G has a Hamilton path. 
Pseudocode:

numpoints = n
curPoints = 0
blocks = [] \make the blocks a class
G = [] --> Graph with n vertices \make the graphs a class
block class:
    possess x and y coords
    know block it was derived from
    know the theta and mag of the transformation

isHamiltonian(G):
    Brute force and dfs from every node to see if its hamiltonian O(N*(M+N))

    for u in G
        for v in G
            (O(N^2))
            if nonadjacent(u,v): #possibly O(1) but probably O(N)
                if d(u) + d(v) < n-1: (negation of requirement)
                        return False
    return True

constructBlock(maxJumpableDistance):
    \ dont generate blocks (close to) directly above,below,left or right
    \ potentially fix magnitude to make the jumps harder constantly?
    \ possibly pass an edge through make a block
    c1 = random.randrange(10,80)
    c2 = random.randrange(100,170)
    c3 = random.randrange(190,260)
    c4 = random.randrange(280,350)
    theta = random.choice([c1,c2,c3,c4])
    magnitude = maxJumpableDistance \for right now it will be fixed as the max
    return (theta,magnitude)

blockIsIn(blocks,checkedBlock):
    for block in blocks
        if checkedBlock shares points from 
            (block.cx-platformWidth/2,block.cy-platformHeight/2,
            block.cx+platformWidth/2,block.cy+platformHeight/2)
                return True
    return False


maxJumpDist = ...

while not isHamiltonian(G):
    curBlock = random.choice(blocks) \find a non-naive implementation to choose a block
    newBlock = constructBlock(maxJumpDist)
    if newBlockNode not in G[curBlockNode] and isJumpable(curBlock,newBlock):
        block.append(newBlock)
        G[curBlockNode].add(newBlockNode)

\possible no exit condition
\maybe cache possible graph if it takes too long 

"""