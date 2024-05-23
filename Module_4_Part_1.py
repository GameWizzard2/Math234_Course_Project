#Math234 Module 4 Part 1.
#Purpose: Create an empty graph and add node list, edge list using python
#Name: Your name
#Date: the date
# Creating a Graph
#filename = myfirstGraph.py

"""
PROCEDURE PART 1
1.	MODIFY THE EXISTING CODE BY ADDING TWO NODES TO THE GRAPH: 
    USE TWO LETTERS OF YOUR CHOICE.
2.	ADD EDGES FROM NODE Q TO EACH NEW NODE.
3.	RUN THE PROGRAM.  
4.	COPY THE ENTIRE SPYDER WINDOW INTO THE POWERPOINT DELIVERABLES DOCUMENT.

"""

import networkx as nx
G = nx.Graph( ) # Creates an empty graph G

# Add a node
G.add_node('P')
"""
1.	MODIFY THE EXISTING CODE BY ADDING TWO NODES TO THE GRAPH: USE TWO LETTERS 
OF YOUR CHOICE. 
Answer: In this case I picked E and Z.
""" 
G.add_node('E')
G.add_node('Z')

# Adds a list of nodes by passing a list argument
G.add_nodes_from(['Q','R']) 


G.add_nodes_from(['Q','E']) 
G.add_nodes_from(['Q','Z']) 


# Add edges 
#G.add_edge('P', 'Q')
"""
2.	ADD EDGES FROM NODE Q TO EACH NEW NODE. 
Answer: Instead of using fucntion G.add_edge('P', 'Q'), the function 
G.add_edges_from() is used instead to add a list of edges combining multiple 
nodes.
"""
G.add_edges_from([('P', 'Q'), ('Q', 'E'), ('Q', 'Z')])


e = ('Q','R')
G.add_edge(*e) # * unpacks the tuple
#G.add_edges_from([('P','Q'), ('P','R')]) # Adds edges from a list
print(G.nodes())
nx.draw_networkx(G, with_labels = True)


