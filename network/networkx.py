#%%
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

# %%
import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()
g.add_node((0, 0))
g.add_node((0, 1))
g.add_edge((0, 0), (0, 1))

nx.draw_networkx(g, node_color='w')
# %%
nw = nx.grid_2d_graph(3, 3)

# 各ノードの描画位置を指定する辞書 { ノードのキー : (x座標, y座標) }
pos = {n: (n[0], -n[1]) for n in nw.nodes()}
pos
#%%
nx.draw_networkx(nw, pos=pos, node_color='w')
plt.gca().xaxis.set_visible(False)
plt.gca().yaxis.set_visible(False)
plt.show()
