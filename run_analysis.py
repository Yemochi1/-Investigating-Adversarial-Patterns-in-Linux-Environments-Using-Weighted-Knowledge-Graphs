# Authors: Jurema & Yemi

import os
from src.graph_builder import analyze_log_data
from src.visualizer import create_graph_visualization, create_heatmap, create_timeline

# Define file paths
DATA_FILE = os.path.join("Data", "audit_logs.csv")
RESULTS_DIR = "Results"
HEATMAP_DIR = os.path.join(RESULTS_DIR, "Hitmaps")

# Ensure output directories exist
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(HEATMAP_DIR, exist_ok=True)

# Define output file paths
OUTPUT_GRAPH = os.path.join(RESULTS_DIR, "attack_graph.png")
OUTPUT_HEATMAP = os.path.join(HEATMAP_DIR, "attack_heatmap.png")
OUTPUT_TIMELINE = os.path.join(RESULTS_DIR, "attack_timeline.png")

if __name__ == "__main__":
    print("Starting attack graph analysis...")
    
    if not os.path.exists(DATA_FILE):
        print(f"Error: Data file not found at {DATA_FILE}")
        print("Please place your 'audit_logs.csv' in the 'Data' folder.")
    else:
        analysis_results = analyze_log_data(csv_path=DATA_FILE)
        
        if analysis_results:
            G, df_mapped = analysis_results
            print("\n--- Analysis Complete. Generating visualizations... ---")

            create_graph_visualization(G, OUTPUT_GRAPH)
            create_heatmap(G, OUTPUT_HEATMAP)
            create_timeline(df_mapped, OUTPUT_TIMELINE)
            
            print(f"\nAll visualizations saved to {RESULTS_DIR}/")
        else:
            print("Analysis failed. No results to visualize.")
    
    print("Analysis finished.")
