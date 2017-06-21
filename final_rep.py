# -*- coding:utf-8 -*-
import pandas   as pd
import numpy    as np
import seaborn  as sns
import networkx as nx
import os
import matplotlib.pyplot  as plt

citations = pd.read_csv('citations.csv', encoding='utf-8', index_col=0)
citations = citations[citations.isin(citations.index)]
citations = citations.dropna(axis=0,how='all')

print(citations)

Graph = nx.DiGraph()
Graph.add_nodes_from(list(citations.index))
for i in list(citations.index):
    x = list(citations.ix[str(i),:])
    x = [j for j in x if str(j) != 'nan']
    edgelist = [(str(i),k) for k in x]
    Graph.add_edges_from(edgelist)

pos = nx.spring_layout(Graph)
nx.draw_networkx(Graph, pos, fontsize=0, nodesize=50, with_labels=True)
plt.show()