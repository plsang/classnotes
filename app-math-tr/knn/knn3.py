from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import pprint
import numpy as np
import time
import dist

__rmin__ = 2

# node: [pivot, radius, points, [child1,child2]]
def new_node(): return  [None,None,None,[None,None]]

def zero_if_neg(x):
    if x < 0: return 0
    else: return x

def form_tree(points,node):    
    pivot = points[0]; print "pivot",pivot; print "points",points
    radius = np.max(dist.dist(points,pivot)); print "radius",radius
    node[0] = pivot
    node[1] = radius
    if len(points) <= __rmin__:
        node[2] = points
        return
    print "node",node
    idx = np.argmax(dist.dist(points,pivot))
    furthest = points[idx,:]; print "new pivot 1", furthest
    idx = np.argmax(dist.dist(points,furthest))
    furthest2 = points[idx,:]; print "new pivot 2", furthest2
    dist1=dist.dist(points,furthest)
    dist2=dist.dist(points,furthest2)
    diffs = dist1-dist2; print diffs    
    p1 = points[diffs <= 0]; print "points 1", p1
    p2 = points[diffs > 0]; print "points 2", p2        
    node[3][0] = new_node() # left child
    node[3][1] = new_node() # right child
    form_tree(p1,node[3][0])
    form_tree(p2,node[3][1])

# knn: [min_so_far, [points]]
def search_tree(new_point, knn_matches, node, k):
    pivot = node[0]
    radius = node[1]
    children = node[3]
    print "c",pivot
    print "r",radius
    print "np", new_point

    # calculate min distance between new point and pivot
    # it is direct distance minus the radius
    min_dist_new_pt_node = dist.norm(pivot,new_point) - radius
    
    # if the new pt is inside the circle, its potential minimum
    # distance to a random point inside is zero (hence
    # zero_if_neg). we can only say so much without looking at all
    # points (and if we did, that would defeat the purpose of this
    # algorithm)
    min_dist_new_pt_node = zero_if_neg(min_dist_new_pt_node)

    knn_matches_out = []
    
    # min is greater than so far
    if min_dist_new_pt_node >= knn_matches[0]:
        # nothing to do
        return knn_matches
    elif children[0] == None and children[1] == None: # if node is a leaf
        knn_matches_out = knn_matches[:] # copy it
        for p in node[2]: # linear scan
            if dist.norm(new_point,p) < radius:
                knn_matches_out.append(p)
                if len(knn_matches_out[1]) == k+1:
                    tmp = [dist.norm(new_point-x) for x in knn_matches_out[1]]
                    print "knn_matches_out[1]",knn_matches_out[1]
                    del knn_matches_out[1][tmp.argmin()]
                    print "knn_matches_out[1]",knn_matches_out[1]
                    knn_matches_out[0] = np.min(tmp)

    else:
        dist_child_1 = dist.norm(children[0][0],new_point)
        dist_child_2 = dist.norm(children[1][0],new_point)
        node1 = None; node2 = None
        if dist_child_1 < dist_child_2:
            node1 = children[0]
            node2 = children[1]
        else:
            node1 = children[1]
            node2 = children[0]

        knn_tmp = search_tree(new_point, knn_matches, node1, k)
        knn_matches_out = search_tree(new_point, knn_tmp, node2, k)
            
    return knn_matches_out
                   
if __name__ == "__main__": 
    points = np.array([[3.,4.],[5.,5.],[9.,2.],[3.2,5.],[7.,5.],
                     [8.,9.],[7.,6.],[8,4],[6,2]])
    tree = new_node()
    form_tree(points,tree)
    #pp = pprint.PrettyPrinter(indent=4)
    #print "\ntree"
    #pp.pprint(tree)
    print "found", search_tree(np.array([5.,5.]),[np.Inf, []], tree, k=3)
    
