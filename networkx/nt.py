# #!/usr/bin/env python
# # Funtion:
# # Filename:
#
# import networkx as nx
# import matplotlib.pyplot as plt
#
# g = nx.Graph()      # 建立一个空的无向图G
# # 添加有向图的方式： G = nx.DiGraph()
# # 需要主要的是：再添加边3-2与边2-3，则被认为是两条不同的边
# # 有向图和无向图是可以相互转化的，分别用到Graph.to_undirected() 和 Graph.to_directed()两个方法。
#
#
# g.add_node(2)       # 添加一个节点
# g.add_node(5)
# g.add_edge(2,5)     # 添加一条边（隐含着添加了两个节点）
# g.add_edge(4,1)
# g.add_edges_from([[2,5], (1,3)])
#
# print(nx.info(g))
# print(g.nodes())    #输出全部的节点
# print(g.edges())    #输出全部的边
# print(g.number_of_edges())   #输出边的数量
# print(g.number_of_nodes())   #输出边的数量
# nx.draw((g))
# plt.show()

import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

B = nx.Graph()
B.add_nodes_from([1,2,3,4], bipartite=0) # Add the node attribute "bipartite"
B.add_nodes_from(['a','b','c'], bipartite=1)
B.add_edges_from([(1,'a'), (1,'b'), (2,'b'), (2,'c'), (3,'c'), (4,'a')])

print(nx.is_connected(B))
bottom_nodes, top_nodes = bipartite.sets(B)
print(bottom_nodes, top_nodes)      # {1, 2, 3, 4} {'b', 'a', 'c'}

B.remove_edge(2,'c')
print(nx.is_connected(B))
print(bipartite.is_bipartite(B))
bottom_nodes, top_nodes = bipartite.sets(B)
print(bottom_nodes, top_nodes)      # {'a', 'b', 3} {1, 2, 4, 'c'}


top_nodes = set(n for n,d in B.nodes(data=True) if d['bipartite']==0)
bottom_nodes = set(B) - top_nodes
print(bottom_nodes, top_nodes)      # {1, 2, 3, 4} {'b', 'a', 'c'}

# print(round(bipartite.density(B, bottom_nodes),2))
# G = bipartite.projected_graph(B, top_nodes)
# print(G.edges())

nx.draw(B)
plt.show()

