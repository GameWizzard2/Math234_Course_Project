#Part 3. 
#Name: Your name
#Date: the date
# Convert Undirected Graph to Directed Graph
#filename = mythirdGraph.py
"""
PROCEDURE PART 3
1.	MODIFY THE EXISTING CODE BY ADDING TWO NODES AND TWO EDGES TO THE GRAPH 
ABOVE. THE SPECIFIC NUMBERS USED AND EDGES ARE YOUR CHOICE.
2.	RUN THE PROGRAM.
"""
#FIXME make a smiley face?
import networkx as nx  
import matplotlib.pyplot as plt 
  
G = nx.Graph() 

# Add nodes
G.add_node(117)
G.add_node(343)
G.add_node('RC')
G.add_node(1138)
G.add_node(101)
G.add_node(38)
G.add_node(777)
G.add_node(123)
G.add_node(321)
  
plt.figure(figsize =(9, 16)) 
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4)])
G.add_edges_from([(117, 343),('RC', 1138), (101, 38), (777, 123), (777, 321)])

# Original Undirected Graph created 
  
plt.subplot(211) 
nx.draw_networkx(G) 
  
H = nx.to_directed(G) 
plt.subplot(212) 
nx.draw_networkx(H) 
# -*- coding: utf-8 -*-

