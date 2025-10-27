# Authors: Jurema & Yemi

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

def create_graph_visualization(G, output_image_path):
    print(f"--- [Visualizing: Knowledge Graph] -> {output_image_path} ---")
    if G.number_of_nodes() == 0:
        print("Cannot visualize an empty graph.")
        return

    plt.figure(figsize=(14, 10))
    pos = nx.spring_layout(G, k=1.5, iterations=30)
    edge_weights = [G.edges[u, v]['weight'] for u, v in G.edges()]
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightblue', alpha=0.9, edgecolors='black', linewidths=1)
    nx.draw_networkx_edges(G, pos, width=[max(1, w / 2) for w in edge_weights], alpha=0.6, edge_color='gray', arrows=True, arrowsize=20, connectionstyle='arc3,rad=0.1')
    nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='firebrick', font_size=10, rotate=False)
    
    plt.title("Adversarial Technique Knowledge Graph", size=20)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_image_path, format="PNG")
    plt.close()

def create_heatmap(G, output_image_path):
    print(f"--- [Visualizing: Hitmap] -> {output_image_path} ---")
    nodes = sorted(list(G.nodes()))
    df_heatmap = pd.DataFrame(0, index=nodes, columns=nodes)
    
    for u, v, data in G.edges(data=True):
        if u in df_heatmap.index and v in df_heatmap.columns:
            df_heatmap.loc[u, v] = data['weight']
        
    if df_heatmap.empty:
        print("Cannot generate heatmap for an empty graph.")
        return

    plt.figure(figsize=(12, 10))
    sns.heatmap(df_heatmap, annot=True, fmt=".0f", cmap="viridis_r", linewidths=.5)
    plt.title("Technique Co-occurrence Hitmap", size=18)
    plt.xlabel("Destination Technique (Follows)")
    plt.ylabel("Source Technique (Precedes)")
    plt.tight_layout()
    plt.savefig(output_image_path, format="PNG")
    plt.close()

def create_timeline(df_mapped, output_image_path):
    print(f"--- [Visualizing: Detection Timeline] -> {output_image_path} ---")
    techniques = sorted(df_mapped['TechniqueID'].unique())
    technique_times = [df_mapped[df_mapped['TechniqueID'] == t]['@timestamp'] for t in techniques]

    plt.figure(figsize=(14, 6))
    plt.eventplot(technique_times, orientation='horizontal', colors='blue', lineoffsets=range(len(techniques)))
    plt.yticks(range(len(techniques)), techniques)
    plt.xlabel("Time of Event")
    plt.ylabel("ATT&CK Technique")
    plt.title("Detection Timeline")
    plt.tight_layout()
    plt.savefig(output_image_path, format="PNG")
    plt.close()
