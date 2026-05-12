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

    @staticmethod
    def plot_mst_comparison(original, MST=None, MST_title="Minimum Spanning Tree"):
        """
        Plot the original graph and its Minimum Spanning Tree side by side.

        Args:
            original: A NetworkX graph or NumPy adjacency matrix for the original graph.
            MST: Optional NetworkX graph for the MST. If None, the MST is computed from the original.
        """
        
        if isinstance(original, np.ndarray):
            original = nx.from_numpy_array(original)
        elif not isinstance(original, nx.Graph):
            raise TypeError("plot_mst_comparison expects a NetworkX graph or NumPy array for the original graph")

        if MST is None:
            mst = nx.minimum_spanning_tree(original, weight='weight')
        elif isinstance(MST, np.ndarray):
            mst = nx.from_numpy_array(MST)
        elif isinstance(MST, nx.Graph):
            mst = MST
        else:
            raise TypeError("plot_mst_comparison expects a NetworkX graph or NumPy array for the MST")

        plt.figure(figsize=(14, 6))

        plt.subplot(1, 2, 1)
        pos = nx.spring_layout(original, seed=42, k=1, iterations=100)

        nx.draw(original, pos,
                with_labels=True,
                node_color='lightblue',
                node_size=800,
                edge_color='gray',
                width=2)

        edge_labels = nx.get_edge_attributes(original, 'weight')
        nx.draw_networkx_edge_labels(original, pos, edge_labels=edge_labels, font_size=10)

        plt.title("Original Graph")
        plt.axis('off')

        plt.subplot(1, 2, 2)
        nx.draw(mst, pos,
                with_labels=True,
                node_color='lightgreen',
                node_size=800,
                edge_color='red',
                width=3)

        mst_labels = nx.get_edge_attributes(mst, 'weight')
        nx.draw_networkx_edge_labels(mst, pos, edge_labels=mst_labels, font_size=10)

        plt.title(f"{MST_title}")
        plt.axis('off')

        plt.tight_layout()
        plt.show()

        total_weight = sum(data['weight'] for _, _, data in mst.edges(data=True))
        print(f"\nTotal weight of {MST_title}: {total_weight}")