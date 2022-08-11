from cmu_112_graphics import *
from graph import *
from kdtree import *
from randomPoints import *

from delaunayTriangulation import *
from dualGraph import *
from bowyerWatson import *
from hamiltonianPath import *

def generateLevel(numNodes,width,height):

    #do-while loop doesn't exist in python
    pointList = genXYCoords((30,80),numNodes,(width,height))    
    triangles = BowyerWatson(pointList)
    
    centerLines,ej = precompute(triangles)
    # centerLines = removeOuterSites(centerLines)
    centerLines = [list(line) for line in centerLines]

    triangles = removeOuterEdges(triangles)
    triangles = removeOuterEdges(triangles)

    while not hamiltonianPath(getAdjList(triangles)):
        pointList = genXYCoords((30,80),numNodes,(width,height))
        
        triangles = BowyerWatson(pointList)
        
        centerLines,ej = precompute(triangles)
        centerLines = [list(line) for line in centerLines]

        triangles = removeOuterEdges(triangles)
        triangles = removeOuterEdges(triangles)
    return triangles,centerLines,ej

def appStarted(app):
    app.level, app.cells, app.edgeAdj = generateLevel(33,app.width,app.height)
    app.delVerts = { vert for tri in app.level for vert in tri.vertices }
    app.voronoiVerts = { vert for edge in app.cells for vert in edge }
    app.curpath = []
    app.badRun = False
    app.prevPaths = []
    app.win = 0
    app.gameOver = False
def keyPressed(app,event):
    if event.key == "r":
        appStarted(app)
def mousePressed(app,event):
    if app.gameOver: return
    app.badRun = False
    location = (event.x, event.y)
    def distance(a, b):
        # print('in distance: a =', a)
        (x1, y1), (x2, y2) = a, b
        return (((x2-x1)**2) + ((y2-y1)**2)) ** 0.5
    closestDel = min(
        app.delVerts,
        key=lambda x: distance(x, location),
    )
    closestVoronoi = min(
        app.voronoiVerts,
        key=lambda x: distance(x, closestDel),
    )
    if closestDel not in app.curpath:
        if len(app.curpath) == 0:
            app.curpath.append(closestDel)
        else:
            if any(closestDel in edge and app.curpath[-1] in edge
                for tri in app.level
                for edge in tri.edges):
                app.curpath.append(closestDel) 
    else:
        ind = app.curpath.index(closestDel)
        app.curpath = app.curpath[:ind]
    
    if len(app.curpath) == len(app.delVerts):
        
        if app.curpath not in app.prevPaths:
            app.win += 1
            app.prevPaths.append(app.curpath)
        else:
            app.badRun = True
        app.curpath = []
    # test = app.mouseTree.findNeighbor((event.x,event.y))
    # print(test[0].value)
    # for point in app.edgeAdj:
    #     # print(point)
    #     if almostEqualPoint(test[0].value,point):
    #         print(app.edgeAdj[point])
    #     # else:
    #         # print("...")
def drawCells(app,canvas):
    width = 400
    height = 400
    for cell_ in app.cells:
        cell = [[0,0],[0,0]]
        cell[0][0] = min(max(cell_[0][0],0),app.width)
        cell[0][1] = min(max(cell_[0][1],0),app.height)
        cell[1][0] = min(max(cell_[1][0],0),app.width)
        cell[1][1] = min(max(cell_[1][1],0),app.height)
        canvas.create_line(cell[0][0],cell[0][1],cell[1][0],cell[1][1],fill="black",width=3)
def drawTriangles(app,canvas):
    for triangle in app.level:
        for edge in triangle.edges:
            edge[1][0],edge[1][1]
            canvas.create_oval(edge[0][0]-5,edge[0][1]-5,edge[0][0]+5,edge[0][1]+5,fill="red",width=3)
            canvas.create_oval(edge[1][0]-5,edge[1][1]-5,edge[1][0]+5,edge[1][1]+5,fill="red",width=3)
def drawPath(app,canvas):
    for ind in range(len(app.curpath)):
        point = app.curpath[ind]
        # print(point,point[0])
        canvas.create_text(point[0]+7,point[1]+7,text=str(ind))
def drawWin(app,canvas):
    if app.badRun:
        text = "Make a path you haven't made before"
    else:
        text = f"You have won {app.win} times" if app.win != 1 else f"You have won once"
    canvas.create_text(0,0,anchor="nw",text=text)
def drawGameEnd(app,canvas):
    canvas.create_text(app.width/2,app.height/2,text="Congrats, you have won the game!",font = "Helvetica 11 bold")

def redrawAll(app,canvas):
    if app.win == len(app.delVerts):
        app.gameOver = True
        drawGameEnd(app,canvas)
    drawCells(app,canvas)
    drawTriangles(app,canvas)
    drawPath(app,canvas)
    drawWin(app,canvas)
    
def main():
    runApp(width=450,height=450)
if __name__ == "__main__":
    """Goals:
    perspective camera
    minimap
    background graphics
    potentially moving platforms
    fancy art with platform
    fancy drawing for hamiltonian path
    """
    main()
        
    
    
    # x,y = np.array(convex).T

    # lineCol = mc.LineCollection(centerLines)
    # lineNew = mc.LineCollection(lines,color="red")
    # # points = plt.scatter(x,y)
    # _ , ax = plt.subplots()
    # ax.add_collection(lineCol)
    # ax.add_collection(lineNew)
    # ax.autoscale()
    

    # ax.add_collection(cent)
    # ax.set_xlim(0,400)
    # ax.set_ylim(0,400)
    # plt.show()

        # # print(dualDelaunay(triangles))
    # for tri in triangles:
    #     for edge in tri.edges:
    #         print(dist(tri.circumCenter,edge[1]))
    #         print(edge)
    #         plt.plot(*zip(*edge),color="red")
       
    #     circle = plt.Circle((tri.circumCenter[0],tri.circumCenter[1]),tri.radius)
    #     plt.gca().add_patch(circle)
    #     plt.scatter(tri.circumCenter[0],tri.circumCenter[1],color="red")
    #     plt.show()
    # # plt.xlim(0,400),plt.ylim(0,400)
    # # print(*zip(*centers))
    # # plt.scatter(*zip(*centers))