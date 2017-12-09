
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
    # Set parameters
    V = G.nodes()
    n = len(V)
    paths_from_v = []
    
    for w in G.nodes():
        for path in nx.all_simple_paths(G, source = v, target = w):
            paths_from_v.append(path)
    return paths_from_v
    
