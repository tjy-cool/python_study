#!/usr/bin/env python
# Funtion:      
# Filename:

import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

B = nx.Graph()
#添加一个项目101，它有3个参与者：201,202,203
B.add_edge(101,201)
B.add_edge(101, None)
B.add_edge(101,202)
B.add_edge(101,203)
#添加一个项目102，它有2个参与者：203,202,2034
B.add_edge(102,203)
B.add_edge(102,204)


NSet = bipartite.sets(B)   #将二分图中的两类节点分别提取出来
print('NSet', NSet)
Act = nx.project(B,NSet[0])     #向项目节点投影
Actor = nx.project(B,NSet[1])  #向参与者节点投影
print(Act.edges())  #输出 [(101, 102)]
print(Actor.edges() )  #输出 [(201, 202), (201, 203), (202, 203), (203, 204)]

G = nx.make_clique_bipartite(Actor)
print(G.edges())  #输出：[(201, -1), (202, -1), (203, -2), (203, -1), (204, -2)]

nx.draw(G)
plt.show()