# -*- coding: utf-8 -*-
"""
Created on Sat May 25 01:09:19 2024

@author: Chris
"""

import networkx as nx
import matplotlib.pyplot as plt 
# TODO add navigation to switch between plots
from matplotlib.widgets import Button

def graph_1():
    G = nx.Graph()  # Creates an empty graph G
    
    # Add nodes
    G.add_node('P')
    G.add_node('E')
    G.add_node('Z')
    
    # Add edges 
    G.add_edges_from([('Q', 'P'), ('Q', 'E'), ('Q', 'Z'), ('Q', 'R')])
    
    print(f"The nodes of graph one are:\n{G.nodes()}")
    nx.draw_networkx(G, with_labels=True)
    plt.title("Graph 1")
    plt.show()

def graph_2(edges, size=(9, 12)):
    OG = nx.Graph()
    plt.figure(figsize=size)
    OG.add_edges_from(edges) 
     
    # Plot original graph
    plt.subplot(211)
    nx.draw_networkx(OG)
    plt.title("Original Graph")
    
    # Create subgraph
    H = OG.subgraph([1, 2, 3, 4, 5, 8])
      
    plt.subplot(212)
    nx.draw_networkx(H)
    plt.title("Subgraph with nodes [1, 2, 3, 4, 5, 8]")
    
    plt.show()

def graph_3():
    """
    PROCEDURE PART 3
    1. MODIFY THE EXISTING CODE BY ADDING TWO NODES AND TWO EDGES TO THE GRAPH 
    ABOVE. THE SPECIFIC NUMBERS USED AND EDGES ARE YOUR CHOICE.
    2. RUN THE PROGRAM.
    """
    G = nx.Graph()
    plt.figure(figsize=(9, 16))

    # Original and modified edges
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (5, 6), (7, 8)])  

    # Plot original undirected graph
    plt.subplot(211)
    nx.draw_networkx(G)
    plt.title("Original Undirected Graph")

    # Convert to directed graph and plot
    H = nx.to_directed(G)
    plt.subplot(212)
    nx.draw_networkx(H)
    plt.title("Directed Graph")

    plt.show()

# Run the functions
graph_1()

edges = [(1, 2), (1, 3), (1, 8), (2, 3), (2, 4), (2, 5), (3, 4),  
         (4, 5), (4, 6), (5, 7), (5, 8), (7, 8)]
graph_2(edges)

graph_3()
