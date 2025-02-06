#!/usr/bin/python
from sys import stdin, stdout, stderr, argv
import ruamel.yaml as yaml

import networkx as nx
import matplotlib.pyplot as plt

if len(argv) != 2:
    print(f"\nERROR! I was expecting one argument (the name of the .yaml file with the data of the graph to be drawn). You gave {len(argv)-1} arguments when calling me (with `{argv[0]}`).\n\n", file=stderr)
    exit(0)

with open(argv[1]) as fgraph:
    ygraph = yaml.safe_load(fgraph)

n = int(ygraph['n'])
V = list(range(n))
    
G = nx.DiGraph()

print(f'{ygraph=}\n', file=stderr, flush=True)
print(f'\n{[ (ygraph["node_label"][u], ygraph["node_label"][v]) for u,v in ygraph["edge"] ]=}', file=stderr, flush=True)

G.add_edges_from([ (ygraph["node_label"][u], ygraph["node_label"][v]) for u,v in ygraph["edge"] ], weight=2)

edge_labels={(u,v):"" for u,v,d in G.edges(data=True)}
#edge_labels={(u,v):d['weight'] for u,v,d in G.edges(data=True)}
red_edges = [] # [('C','D'),('D','A')]
edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]

node_labels = {node:node for node in G.nodes()}
pos = { ygraph["node_label"][v]: ygraph["node_pos"][v] for v in V }

nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, labels=node_labels)
nx.draw(G,pos, node_color = 'green', node_size=1200,edge_color=edge_colors,edge_cmap=plt.cm.Reds)
plt.show()
