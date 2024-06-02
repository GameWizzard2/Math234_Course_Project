# -*- coding: utf-8 #Math234 Module 4 Part 2. 
#Name: Christopher Barfield
 #Date: 6/2/24
 # Creating a Graph and a subgraph
 #filename = mysecondGraph.py
"""
 PROCEDURE PART 2:
1.	MODIFY THE EXISTING CODE BY ADDING AN EDGE FROM NODE 1 TO NODE 8 IN THE 
ORIGINAL GRAPH AND ADDING NODES 5 AND 8 TO THE SUBGRAPH.
2.	RUN THE PROGRAM.

"""

import networkx as nx  
import matplotlib.pyplot as plt 

OG = nx.Graph() 
  
plt.figure(figsize =(9, 12))
"""
1.	MODIFY THE EXISTING CODE BY ADDING AN EDGE FROM NODE 1 TO NODE 8 IN THE 
ORIGINAL GRAPH.

Answer: Add a tuple to OG.add_edges_from
""" 
OG.add_edges_from([(1, 2), (1, 3), (1, 8), (2, 3), (2, 4), (2, 5), (3, 4),  
                         (4, 5), (4, 6), (5, 7), (5, 8), (7, 8)]) 
 # original Graph created 
plt.subplot(211) 
  
nx.draw_networkx(OG)
"""
ADDING NODES 5 AND 8 TO THE SUBGRAPH.
"""
# Create a subgraph with nodes [1, 2, 3, 4, 5, 8]
H = OG.subgraph([1, 2, 3, 4, 5, 8]) 

  
plt.subplot(212)
nx.draw_networkx(H)

plt.show()
