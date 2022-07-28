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
Pseudocode:

numpoints = n
curPoints = 0
blocks = []
G = [] --> Graph of len(n)

isHamiltonian(G):
    Check if connected by bfs --- cache if it's connected (O(N))

    for u in G
        for v in G
            for w in G
                (O(N^3))
                if nonadjacent(u,v,w): #possibly O(1) but probably O(N)
                    if d(u) + d(v) + d(w) < 1/2(3n-5): (negation of requirement)
                        return False
    return True

constructBlock(maxJumpableDistance):
    \ dont generate blocks (close to) directly above,below,left or right
    \ potentially fix magnitude to make the jumps harder constantly?
    
    c1 = random.randrange(1,80)
    c2 = random.randrange(100,170)
    c3 = random.randrange(190,260)
    c4 = random.randrange(280,350)
    theta = random.choice([c1,c2,c3,c4])
    magnitude = maxJumpableDistance \for right now it will be fixed as the max
    return (theta,magnitude)

inLineOfSight(block1,block2):
    mx + b = construct line between centers
    for point in range(block1.x,block2.x) \centers of blocks
        
notInAnyLineOfSight(mainBlock):
    res = []
    for block in blocks
        if inLineOfSight(block,mainBlock):
            res.append(block)
    return block

while not isHamiltonian(G):



"""