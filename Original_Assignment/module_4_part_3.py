#Part 3. 
#Name: Christopher Barfield
#Date: 6/2/24
# Convert Undirected Graph to Directed Graph
#filename = mythirdGraph.py
"""
PROCEDURE PART 3
1.	MODIFY THE EXISTING CODE BY ADDING TWO NODES AND TWO EDGES TO THE GRAPH 
ABOVE. THE SPECIFIC NUMBERS USED AND EDGES ARE YOUR CHOICE.
2.	RUN THE PROGRAM.
"""
import networkx as nx  
import matplotlib.pyplot as plt 
  
G = nx.Graph() 
  
plt.figure(figsize =(9, 16)) 
# Og Code G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4)]) 
# Modified Code, # Added nodes 5, 6, 7, 8 and edges (5, 6), (7, 8):
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (5, 6), (7, 8)])  

# Original Undirected Graph created 
  
plt.subplot(211) 
nx.draw_networkx(G) 
  
H = nx.to_directed(G) 
plt.subplot(212) 
nx.draw_networkx(H) 
