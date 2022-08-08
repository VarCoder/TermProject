```py
1st Idea: generate random set of points
    \ done with kdTree
2nd: generate voronoi diagram
    \ https://en.wikipedia.org/wiki/Fortune%27s_algorithm
        \ https://jacquesheunis.com/post/fortunes-algorithm/
    \ https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm
        \ https://github.com/jmespadero/pyDelaunay2D
3rd: connect random cells in the voronoi diagram
    \ Make sure it's in the style of the game and not entirely random
4th: generate dual graph (adj list for faces on the diagram to other faces) (not really but almost delaunay triangulation)
    \ floodfill by iterating through geometric version of voronoi diagram?
5th: search for hamiltonian path
    \ https://codeforces.com/blog/entry/337#:~:text=4.%20Check%20for%20existence%20of%20Hamiltonian%20walk
    if path exists
        draw and let user play game
    else
        restart from 3rd again
```
