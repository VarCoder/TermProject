#use recursion/backtracking
#memoization would be VERY helpful here
#generate random mx+b that points in the general vicinity of an edge node
#generate these lines with a fixed length
'''py
Voronoi::draw(){
    // define colors for each point in the diagram;
    // make a structure to hold {pixelCoords,sourcePoint} queue objects
    // initialize a struct of two closest points for each pixel on the map
    // initialize an empty queue;

    // for each point in diagram:
        // for the push object, first set the pixelCoords to pixel coordinates of point;
        // set the sourcePoint of the push object to the current point;
        // push the queue object;

    // while queue is not empty:
        // dequeue a queue object;
        // step through cardinal neighbors n,s,e,w:
            // if the current dequeued source point is closer to the neighboring pixel than either of the two closest:
                // set a boolean doSortAndPush to false;
                // if only one close neighbor is set:
                    // add sourcePoint to closestNeighbors for pixel;
                    // set doSortAndPush to true;
                // elif sourcePoint is closer to pixel than it's current close neighbor points:
                    // replace the furthest neighbor point with sourcePoint;
                    // set doSortAndPush to true;
                // if flag doSortAndPush is true:
                    // re-sort closest neighbors; 
                    // enqueue object made of neighbor pixel coordinates and sourcePoint;

    // for each pixel location:
        // if distance to closest point within a radius for point drawing:
            // color pixel the point color;
        // elif distances to the two closest neighbors are roughly equal:
            // color the pixel to your border color;
        // else 
            // color the pixel the color of the point's region; 

}
'''