# Authors: Jurema & Yemi

import pandas as pd
import networkx as nx
from src.mapping import TECHNIQUE_MAP, CUSTOM_DATE_FORMAT, TIME_WINDOW

def analyze_log_data(csv_path):
    """
    Loads, cleans, and builds the NetworkX graph from the audit_logs CSV.
    Returns the graph (G) and the mapped DataFrame (df_mapped).
    """
    print("Step 1: Load and Clean Data")
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: {csv_path} not found.")
        return None

    print(f"Loaded {len(df)} total log entries.")

    try:
        df['@timestamp'] = pd.to_datetime(df['@timestamp'], format=CUSTOM_DATE_FORMAT)
    except Exception as e:
        print(f"Error parsing timestamps: {e}")
        return None
    df = df.sort_values(by='@timestamp').reset_index(drop=True)

    try:
        df['TechniqueID'] = df['process.executable'].apply(lambda x: TECHNIQUE_MAP.get(x))
    except KeyError:
        print("Error: Column 'process.executable' not found.")
        return None

    df_mapped = df.dropna(subset=['TechniqueID']).copy()
    df_mapped = df_mapped.loc[df_mapped['TechniqueID'].shift() != df_mapped['TechniqueID']]
    print(f"Mapped {len(df_mapped)} events to ATT&CK techniques.")

    if len(df_mapped) < 2:
        print("Error: Not enough mapped events to build a graph.")
        return None

    print("\nStep 2: Build Weighted Graph")
    G = nx.DiGraph()
    G.add_nodes_from(df_mapped['TechniqueID'].unique())
    print(f"Building graph with time window: {TIME_WINDOW}")

    for i in range(len(df_mapped)):
        event_A = df_mapped.iloc[i]
        for j in range(i + 1, len(df_mapped)):
            event_B = df_mapped.iloc[j]
            time_diff = event_B['@timestamp'] - event_A['@timestamp']
            
            if time_diff > TIME_WINDOW:
                break
            
            if event_A['TechniqueID'] != event_B['TechniqueID']:
                u, v = event_A['TechniqueID'], event_B['TechniqueID']
                if G.has_edge(u, v):
                    G.edges[u, v]['weight'] += 1
                else:
                    G.add_edge(u, v, weight=1)

    print(f"Graph build complete. Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
    return G, df_mapped
