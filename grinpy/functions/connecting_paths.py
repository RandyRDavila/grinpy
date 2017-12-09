
# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for paths between a given vertex and all other vertices"""

def connecting_paths(G, v):
    """Return a list of all paths from vertex v to all other vertices in G.
    Parameters
    ----------
    G : graph
        A NetworkX graph.
    v : a single source node
    Returns
    -------
    neighbors : list
        A list containing all paths from v to all other vertices in the graph
    --------
    
    """
    # Set empty list to store paths
    paths_from_v = []
    
    for w in G.nodes():
        for path in nx.all_simple_paths(G, source = v, target = w):
            paths_from_v.append(path)
    return paths_from_v
    

def is_rainbow_path(P, edge_coloring):
    """ Return a boolean statement True if P is a rainbow path, and False otherwise
    
    Parameters
    ----------
    P : A networkx path (sub)graph
    edge_color_dictionary : dictionary 
        A dictionary with keys corresponding to the edges in P and associated values being their respective edge 'color'
                            
    Returns
    -------
    is_rainbow_path : boolean
        True if P is a rainbow path, and false otherwise.
    """
    
    for edge_1 in P.edges():
        for edge_2 in P.edges():
            if edge_1 != edge_2 and edge_coloring[edge_1] == edge_coloring[edge_2]:
                return False
    return True
    
def is_vertex_rainbow_connected(G,v, edge_coloring):
    #TODO: Add documentation
    for path in connecting_paths(G,v):
        if is_rainbow_path(path, edge_coloring) == True:
            return True
    return False

def is_graph_rainbow_connected(G, edge_coloring):
    #TODO: Addo documentation
    for vertex in G.nodes():
        if is_vertex_rainbow_connected(G,vertex,edge_coloring) == False:
            return False
    return True
