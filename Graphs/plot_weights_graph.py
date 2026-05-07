import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class PlotWeightsGraph:
    def __init__(self, graph, random_seed=42):
        self.graph = graph

        np.random.seed(random_seed)
        pos = nx.spring_layout(self.graph, k=0.8, iterations=100)

        nx.draw(self.graph, pos, 
                with_labels=True, 
                node_color='lightblue', 
                edge_color='gray')

        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, font_size=7, bbox=dict(facecolor='white', edgecolor='none', alpha=1))
        plt.show()