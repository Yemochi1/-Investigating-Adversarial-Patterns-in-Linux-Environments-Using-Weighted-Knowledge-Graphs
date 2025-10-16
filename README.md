# Graph-Guided Adversarial Technique Detection Across Platforms
# Project Overview
This project is an expansion of research intially published in the 2024 IEEE TrustCom paper "Investigating Patterns of Adversarial Techniques for Cyberattack Forensics". The research detailed a graph-based technique identifying adversarial attack patterns by analyzing co-occurrence patterns found in the MITRE ATT&CK framework. This was specifically designed for Windows event logs and successfully achieved high accuracy in detecting data leakage and unauthorized access attacks.

The proposed extension evaluates the graph-guided approach robustness and performance by incorporating Linux and cloud telemtry, and benchmarking its behavior under streaming SIEM workloads.
# Research Objectives
1. Does the pattern-based detector hold up on Linux and cloud (e.g, CloudTrail/Azure) telemetry without changing the core method?
2. What are the time-to-detection and throughput under streaming SIEM workloads?
# Methodology
1. Baseline Reproduction
Rebuild the the ATT&CK knowledge graph, extract adversarial patterns for data leakage and unathourized access. Run detection on original Windows event logs using Sigma rules and ElasticSearch.
2. Cross-platform Extension
Collect Linux logs (auditd/Sysmon-for-Linux) and cloud logs (AWS CloudTrail). Map events to ATT&CK techniques using Sigma rules/ATT&CK mappings. Evaluate detection accuracy per platform using precision, recall, kill-chain coverage and ATT&CK/Sigma support gaps.
3. Streaming SIEM Benchmark
Replay logs with timestamps, using Beats/Kafka into ElasticSearch. Measure end-to-end latency and throughput. Vary the edge-weight threshold graph extraction and analyze the trade-offs between detection accuracy and latency/throughput.
# Expected Contributions
- Empirical validation of graph-guided detection across Windows, Linux and cloud platforms.
- Benchmark results for latency and throughput under streaming workloads.
- Visualizations: Hit maps, detection timelines, and comparative performance charts.
