import math
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

input_path = 'data/manual_dataset.ods'
input_file = pd.ExcelFile(input_path)
articles_df = pd.read_excel(input_file, 'articles', index_col='index')
citations_df = pd.read_excel(input_file, 'references')

def convert_article_tuple(t):
    return (int(t.Index), {'title': t.title, 'citations': t.citations})

def convert_citation_tuple(t):
    return (t.origin, t.destination)

graph = nx.DiGraph()
graph.add_nodes_from(map(convert_article_tuple, articles_df.itertuples()))
graph.add_edges_from(map(convert_citation_tuple, citations_df.itertuples()))
pos = nx.planar_layout(graph)
sizes = list(nx.get_node_attributes(graph, 'citations').values())
sizes = [s + 300 for s in sizes]
plt.figure(figsize=(10, 10))
nx.draw(graph, pos=pos, with_labels=True, node_size=sizes)
plt.savefig('graph.pdf')

