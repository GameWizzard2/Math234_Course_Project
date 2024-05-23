#Math234 Course Project
import networkx as nx

G = nx.Graph( ) # Creates an empty graph G

# Add a node
G.add_nodes_from(['A','B','C','D']) # Adds a list of nodes by passing a list argument

# Add edges 
G.add_edge('A', 'B')
G.add_edge('C', 'D')
print(G.nodes())
nx.draw_networkx(G, with_labels = True)
