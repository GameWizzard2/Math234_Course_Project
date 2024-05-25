# -*- coding: utf-8 -*-
"""
Created on Sat May 25 01:09:19 2024

@author: Chris
"""

import networkx as nx
import matplotlib.pyplot as plt 

def graph_1():
    G = nx.Graph( ) # Creates an empty graph G
    
    # Add a nodes
    G.add_node('P')
    G.add_node('E')
    G.add_node('Z')
    
    # Add edges 
    G.add_edges_from([('Q', 'P'), ('Q', 'E'), ('Q', 'Z'), (('Q','R'))])
    
    print(f"The nodes of graph one are:\n {G.nodes()}")
    nx.draw_networkx(G, with_labels = True)
    return None
    


def graph_2(edges, size = (9, 12)):
    OG = nx.Graph() 
      
    plt.figure(figsize=size)
    
    OG.add_edges_from(edges) 
     # original Graph created 
    plt.subplot(211) 
      
    nx.draw_networkx(OG)
    """
    ADDING NODES 5 AND 8 TO THE SUBGRAPH.
    """
    H = OG.subgraph([1, 2, 3, 4, 5, 8]) 
    # [1, 2, 3, 4] is the subset of  
    # the original set of nodes 
      
    plt.subplot(212)
    nx.draw_networkx(H)

        
#graph_1()

edges = [(1, 2), (1, 3), (1, 8), (2, 3), (2, 4), (2, 5), (3, 4),  
                         (4, 5), (4, 6), (5, 7), (5, 8), (7, 8)]
graph_2(edges)