import math
import textwrap
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
titles = nx.get_node_attributes(graph, 'title')
titles = {k: f'{k}\n' + textwrap.shorten(t, width=50) for k, t in titles.items()}
plt.figure(figsize=(30, 30))
nx.draw(graph, pos=pos, labels=titles, node_size=sizes, edge_color='#00000060', node_color="#0000FF60")
plt.savefig('graph.pdf')

