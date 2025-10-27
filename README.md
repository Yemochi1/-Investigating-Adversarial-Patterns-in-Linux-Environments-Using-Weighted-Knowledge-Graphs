# Investigating Adversarial Patterns in Linux Environments Using Weighted Knowledge Graphs
# Project Overview
This project is an expansion of research intially published in the 2024 IEEE TrustCom paper "Investigating Patterns of Adversarial Techniques for Cyberattack Forensics". The research detailed a graph-based technique identifying adversarial attack patterns by analyzing co-occurrence patterns found in the MITRE ATT&CK framework. This was specifically designed for Windows event logs and successfully achieved high accuracy in detecting data leakage and unauthorized access attacks. The proposed extension evaluates the graph-guided approach robustness and performance by incorporating Linux telemetry.

# Research Objectives
1. Can a pattern-based analysis methodology, originally designed for other data, be empirically validated on Linux auditd telemetry?
2. What attack patterns can be identified, modeled, and visualized by applying graph-based analysis to a static dataset of simulated Linux logs?
   
# Methodology
1. Cross-platform Extension: Collect Linux logs (auditd) into an ELK Stack. Simulate a series of known adversary techniques and export the resulting logs to a static .csv file.
2. Technique Mapping: Develop detection logic (Sigma rules, KQL queries) to map raw log events to their corresponding MITRE ATT&CK techniques.
3. Graph-Based Analysis: Build a weighted, directed knowledge graph. The graph's edges represent co-occurring techniques that appear within a defined time window, and the weights represent the frequency of that co-occurrence.

# Expected Contributions
- Empirical validation of graph-guided detection across Linux platform.
- Visualizations: co-occurrence hit maps, detection timelines, and weighted knowledge graph.
