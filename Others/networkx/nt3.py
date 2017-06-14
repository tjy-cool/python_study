#!/usr/bin/env python
# Funtion:      
# Filename:

import networkx as nx
print(nx)
import matplotlib.pyplot as plt
g = nx.read_edgelist('one.txt', create_using=nx.Graph(), nodetype=int)

print(nx.info(g))
print(g.nodes())    #输出全部的节点
print(g.edges())    #输出全部的边

nx.draw(g)
plt.show()