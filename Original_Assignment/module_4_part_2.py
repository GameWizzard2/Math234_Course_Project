# -*- coding: utf-8 #Math234 Module 4 Part 2. 
#Name: Your name
 #Date: the date
 # Creating a Graph and a subgraph
 #filename = mysecondGraph.py

import networkx as nx  
import matplotlib.pyplot as plt 
  
OG = nx.Graph() 
  
plt.figure(figsize =(9, 12)) 
OG.add_edges_from([(1, 2), (1, 3), (1, 8), (2, 3), (2, 4), (2, 5), (3, 4),  
                         (4, 5), (4, 6), (5, 7), (5, 8), (7, 8)]) 
 # original Graph created 
plt.subplot(211) 
  
nx.draw_networkx(OG)
H = OG.subgraph([1, 2, 3, 4, 5, 8]) 
# [1, 2, 3, 4] is the subset of  
# the original set of nodes 
  
plt.subplot(212)
nx.draw_networkx(H)


