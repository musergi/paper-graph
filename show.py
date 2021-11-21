import argparse
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--input_edges', required=True)
parser.add_argument('--input_nodes', required=True)
args = parser.parse_args()

df_nodes = pd.read_csv(args.input_nodes, index_col=0)
df_edges = pd.read_csv(args.input_edges, index_col=0)

graph = nx.DiGraph()
for node in df_nodes.itertuples():
    graph.add_node(node.id, title=node.title, year=node.year)
for edge in df_edges.itertuples():
    graph.add_edge(edge.origin, edge.destination)
nx.draw(graph, labels=nx.get_node_attributes(graph, 'title'))
plt.show()
