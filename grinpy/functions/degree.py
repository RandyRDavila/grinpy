# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Assorted degree related graph utilities.
"""

from grinpy import degree, nodes, number_of_nodes
from grinpy.functions.neighborhoods import closed_neighborhood, neighborhood

__all__ = ['degree_sequence',
           'min_degree',
           'max_degree',
           'average_degree',
           'number_of_nodes_of_degree_k',
           'number_of_degree_one_nodes',
           'number_of_min_degree_nodes',
           'number_of_max_degree_nodes',
           'neighborhood_degree_list',
           'closed_neighborhood_degree_list'
          ]

def degree_sequence(G):
    """Return the degree sequence of G.

    The degree sequence of a graph is the sequence of degrees of the nodes
    in the graph.

    Parameters
    ----------
    G : graph
        A NetworkX graph.

    Returns
    -------
    degSeq : list
        The degree sequence of the graph.

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.degree_sequence(G)
    [2, 1, 1]
    """
    return [degree(G, v) for v in nodes(G)]

def min_degree(G):
    """Return the minimum degree of G.

    The minimum degree of a graph is the smallest degree of any node in the
    graph.

    Parameters
    ----------
    G : graph
        A NetworkX graph.

    Returns
    -------
    minDegree : int
        The minimum degree of the graph.

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.min_degree(G)
    1
    """
    D = degree_sequence(G)
    D.sort()
    return D[0]

def max_degree(G):
    """Return the maximum degree of G.

    The maximum degree of a graph is the largest degree of any node in the
    graph.

    Parameters
    ----------
    G : graph
        A NetworkX graph.

    Returns
    -------
    maxDegree : int
        The maximum degree of the graph.

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.min_degree(G)
    2
    """
    D = degree_sequence(G)
    D.sort(reverse = True)
    return D[0]

def is_regular(G):
    """ Return boolean value of True if G is regular, and False if G is not regular """
    return min_degree(G) == max_degree(G)

def is_subcubic(G):
    """ Return boolean value of True if G has maximum degree at most 3, and False if G has 
        maximum degree greater than 3"""
    return max_degree(G) <= 3

def is_cubic(G):
    """ Return boolean value of True if G has min_degree(G)=max_degree(G)=3, and false otherwise"""
    return is_regular(G) and max_degree(G) == 3





def average_degree(G):
    """Return the average degree of G.

    The average degree of a graph is the average of the degrees of all nodes
    in the graph.

    Parameters
    ----------
    G : graph
        A NetworkX graph.

    Returns
    -------
    avgDegree : float
        The average degree of the graph.

    Examples
    --------
    >>> G = nx.star_graph(3) # Star on 4 nodes
    >>> nx.average_degree(G)
    1.5
    """
    return sum(degree_sequence(G)) / number_of_nodes(G)

def number_of_nodes_of_degree_k(G, k):
    """Return the number of nodes of the graph with degree equal to k.

    Parameters
    ----------
    G : graph
        A NetworkX graph.

    k : int
        A positive integer.

    Returns
    -------
    numNodes : int
        The number of nodes in the graph with degree equal to k.

    See Also
    --------
    number_of_leaves, number_of_min_degree_nodes, number_of_max_degree_nodes

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.number_of_nodes_of_degree_k(G, 1)
    2
    """
    return sum(1 for v in nodes(G) if degree(G, v) == k)

def number_of_degree_one_nodes(G):
    """Return the number of nodes of the graph with degree equal to 1.

    A vertex with degree equal to 1 is also called a *leaf*.

    Parameters
    ----------
    G : graph
        A NetworkX graph.

    Returns
    -------
    numNodes : int
        The number of nodes in the graph with degree equal to 1.

    See Also
    --------
    number_of_nodes_of_degree_k, number_of_min_degree_nodes,
    number_of_max_degree_nodes

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.number_of_leaves(G)
    2
    """
    return number_of_nodes_of_degree_k(G, 1)

def number_of_min_degree_nodes(G):
    """Return the number of nodes of the graph with degree equal to the minimum
    degree of the graph.

    Parameters
    ----------
    G : graph
        A NetworkX graph.

    Returns
    -------
    numNodes : int
        The number of nodes in the graph with degree equal to the minimum
        degree.

    See Also
    --------
    number_of_nodes_of_degree_k, number_of_leaves, number_of_max_degree_nodes,
    min_degree

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.number_of_min_degree_nodes(G)
    2
    """
    return number_of_nodes_of_degree_k(G, min_degree(G))

def number_of_max_degree_nodes(G):
    """Return the number of nodes of the graph with degree equal to the maximum
    degree of the graph.

    Parameters
    ----------
    G : graph
        A NetworkX graph.

    Returns
    -------
    numNodes : int
        The number of nodes in the graph with degree equal to the maximum
        degree.

    See Also
    --------
    number_of_nodes_of_degree_k, number_of_leaves, number_of_min_degree_nodes,
    max_degree

    Examples
    --------
    >>> G = nx.path_graph(3) # Path on 3 nodes
    >>> nx.number_of_max_degree_nodes(G)
    1
    """
    return number_of_nodes_of_degree_k(G, max_degree(G))

def neighborhood_degree_list(G, nbunch):
    """Return a list of the unique degrees of all neighbors of nodes in nbunch

    Parameters
    ----------
    G : graph
        A NetworkX graph.

    nbunch : a single node or iterable container of nodes

    Returns
    -------
    degreeList : list
        A list of the degrees of all nodes in the neighborhood of the nodes
        in nbunch.

    See Also
    --------
    closed_neighborhood_degree_list, neighborhood

    Examples
    --------
    >>> import grinpy as gp
    >>> G = gp.path_graph(3) # Path on 3 nodes
    >>> gp.neighborhood_degree_list(G, 1)
    [1, 2]
    """
    return list(set(degree(G, u) for u in neighborhood(G, nbunch)))

def closed_neighborhood_degree_list(G, nbunch):
    """Return a list of the unique degrees of all nodes in the closed
    neighborhood of the nodes in nbunch.

    Parameters
    ----------
    G : graph
        A NetworkX graph.

    nbunch : a single node or iterable container of nodes

    Returns
    -------
    degreeList : list
        A list of the degrees of all nodes in the closed neighborhood of the
        nodes in nbunch.

    See Also
    --------
    closed_neighborhood, neighborhood_degree_list

    Examples
    --------
    >>> import grinpy as gp
    >>> G = gp.path_graph(3) # Path on 3 nodes
    >>> gp.closed_neighborhood_degree_list(G, 1)
    [1, 2, 2]
    """
    return list(set(degree(G, u) for u in closed_neighborhood(G, nbunch)))
