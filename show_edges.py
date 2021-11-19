import argparse
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True);
args = parser.parse_args()

df = pd.read_csv(args.input, index_col=0)
graph = nx.DiGraph()
for edge in df.itertuples():
    graph.add_edge(edge.origin, edge.destination)
nx.draw(graph)
plt.show()
