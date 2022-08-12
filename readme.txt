Project Description:
    A fun puzzle game designed using graph theory and computational geometry 
    to challenege the user to find a path in a complex system.  
Structural Plan:
    The game will have a title screen stage, a loading bar potentially to generate a valid game board, the game screen, 
    and if the user beats the level there will be a section asking if they want to increase the difficulty.
Algorithmic Plan:
    Delaunay Triangulation via Bowyer-Watson (create centers of cells)
	Voronoi Diagram Generation via a Flipping algorithm (create cells)
	Convex Hull to filter out "bad points" (minimize mistakes)
	Hamiltonian Path existence check via a Dynamic Programming graph method (ensure game is possible)
		This was done to guarantee it's possible to make a possible path
		I used a graph theory proof to create the win condition via this algorithm
	Random point generation using KD-trees to be nearly equidistant (maximize cells sizes for improved UI)
Timeline Plan:
    Finish geometry by end of week and spend 1-2 days doing the graph theory part of the problem
Version Control Plan:
    I'm using GitHub to host and keep track of any changes of my project.
TP2 Update:
    I have graphics now, and I'm working on making the game show which path the user constructed
TP3 Update:
	I added graphics, a reasonably designed UI, a information screen, and buckets of difficulty.