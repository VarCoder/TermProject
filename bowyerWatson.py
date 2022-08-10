from itertools import permutations
# from dualGraph import *
import math
import sys


def orientation(a, b, c):
    # perform cross-product to find orientation of points
    ax, ay = a
    bx, by = b
    cx, cy = c
    return (bx-ax) * (cy-ay) - (by-ay) * (cx-ax)


def dist(point1, point2):
    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]
    return ((x2-x1)**2 + (y2-y1)**2)**0.5


def midpoint(point1, point2):
    return (((point1[0]+point2[0])/2), ((point1[1]+point2[1])/2))


def slope(point1, point2):
    y_diff = (point2[1]-point1[1])
    x_diff = (point2[0]-point1[0]+sys.float_info.epsilon)
    return int(y_diff/x_diff)


class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.edges = [
            (a, b),
            (b, c),
            (a, c)
        ]
        self.vertices = frozenset([self.a, self.b, self.c])

        self.circumCenter = self.getcircumCenter()
        self.radius = self.circumRadius()
    def getcircumCenter(self):
        #! https://en.wikipedia.org/wiki/Circumscribed_circle#Cartesian_coordinates_2
        D = 2 * (self.a[0]*(self.b[1]-self.c[1]) + self.b[0]*(self.c[1]-self.a[1]) + self.c[0]*(self.a[1]-self.b[1]))
        aComponent = (self.a[0]**2 + self.a[1]**2)
        bComponent = (self.b[0]**2 + self.b[1]**2)
        cComponent = (self.c[0]**2 + self.c[1]**2)
        centerX = (aComponent*(self.b[1]-self.c[1]) + bComponent*(self.c[1]-self.a[1]) + cComponent*(self.a[1]-self.b[1]))
        centerX *= 1/(D+sys.float_info.epsilon)

        centerY = (aComponent*(self.c[0]-self.b[0]) + bComponent*(self.a[0]-self.c[0]) + cComponent*(self.b[0]-self.a[0]))
        centerY *= 1/(D+sys.float_info.epsilon)
        return (centerX,centerY)

    def circumRadius(self):
        return dist(self.a,self.circumCenter)
    def inCircumcircle(self,point):
        return dist(point,self.circumCenter) <= self.radius

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.vertices == other.vertices

    def __hash__(self):
        return hash(self.vertices)

    def __iter__(self):
        yield from self.edges

    # def inCircumcircle(self, point):
    #     #! https://stackoverflow.com/questions/39984709/how-can-i-check-wether-a-point-is-inside-the-circumcircle-of-3-points
    #     for i in permutations([self.a, self.b, self.c]):
    #         # test out variations to see if points are in ccw order
    #         if orientation(i[0], i[1], i[2]) > 0:
    #             ax = i[0][0]-point[0]
    #             ay = i[0][1]-point[1]
    #             bx = i[1][0]-point[0]
    #             by = i[1][1]-point[1]
    #             cx = i[2][0]-point[0]
    #             cy = i[2][1]-point[1]
    #             res = (ax**2 + ay**2) * (bx*cy - cx*by) - \
    #                   (bx**2 + by**2) * (ax*cy - cx*ay) + \
    #                   (cx**2 + cy**2) * (ax*by - bx*ay)
    #             ans = res >= 0
    #             # assert(self.inCirCumCircle2(point)==ans)
    #             return ans
        # return False


def BowyerWatson(pointList):
    #! implemented from https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm
    #! https://stackoverflow.com/questions/58116412/a-bowyer-watson-delaunay-triangulation-i-implemented-doesnt-remove-the-triangle
    #! https://github.com/bl4ckb0ne/delaunay-triangulation/blob/master/dt/delaunay.cpp
    triangulation = set()  # list of triangle objects

    minX = min(x[0] for x in pointList)
    maxX = max(x[0] for x in pointList)
    minY = min(x[1] for x in pointList)
    maxY = max(x[1] for x in pointList)

    dx = maxX-minX
    dy = maxY-minY
    maxDiff = max(dx, dy)
    avgX = (minX+maxX)/2
    avgY = (minY+maxY)/2

    superTriangle = Triangle(
        (avgX - 20 * maxDiff, avgY-maxDiff),
        (avgX, avgY + 20 * maxDiff),
        (avgX + 20 * maxDiff, avgY - maxDiff)
    )

    triangulation.add(superTriangle)
    for point in pointList:
        badTriangles = set()
        for tri in triangulation:
            if tri.inCircumcircle(point):
                badTriangles.add(tri)
        polygon = set()
        for tri in badTriangles:
            for edge in tri:
                if not any((edge in tri_ and tri != tri_) for tri_ in badTriangles):
                    polygon.add(edge)
        # print(polygon,badTriangles)
        for tri in badTriangles:
            triangulation.remove(tri)
        for edge in polygon:
            newTri = Triangle(edge[0], edge[1], point)
            triangulation.add(newTri)

    return {
        tri for tri in triangulation
        if not any(vertex in superTriangle.vertices for vertex in tri.vertices)
    }
