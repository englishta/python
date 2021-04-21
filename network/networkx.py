# %%
import networkx as nx
G = nx.Graph()
N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
G.add_nodes_from(N)

E = [(1, 2), (1, 8), (2, 3), (4, 5), (2, 4), (4, 5), (6, 7), (6, 8), (8, 9), (8, 10)]
G.add_edges_from(E)

# %%
nx.draw_networkx(G,with_labels=True, node_color='r')

# %%
import networkx as nx
G = nx.erdos_renyi_graph(100, 0.1)
nx.draw_random(G, node_color = 'blue')
#%%
import matplotlib.pyplot as plt
import networkx as nx
 
G=nx.watts_strogatz_graph(100,4,0.2)
nx.draw(G, node_color = "red")
plt.show()


