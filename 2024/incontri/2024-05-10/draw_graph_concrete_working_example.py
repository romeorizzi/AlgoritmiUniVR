#!/usr/bin/python
from sys import stdin, stdout, stderr

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_edges_from([('A', 'B'),('B', 'A'),('C','D'),('G','D')], weight=1)
G.add_edges_from([('D','A'),('D','E'),('B','D')], weight=2)
G.add_edges_from([('B','C'),('E','F')], weight=3)
G.add_edges_from([('C','F')], weight=4)

edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
red_edges = [('C','D'),('D','A')]
edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]

node_labels = {node:node for node in G.nodes()}

pos = {
    'A':(1,3),
    'B':(4,5),
    'C':(6,5),
    'D':(4,3),
    'E':(7,3),
    'F':(9,6),
    'G':(9,3),
}

nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, labels=node_labels)
nx.draw(G,pos, node_color = 'green', node_size=1200,edge_color=edge_colors,edge_cmap=plt.cm.Reds)
plt.show()
