#!/usr/bin/env python
# Funtion:      
# Filename:

import networkx as nx
import matplotlib.pyplot as plt
g = nx.Graph()

g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,1)

nx.write_edgelist(g,"edgelist.txt")

nx.draw((g))

plt.show()