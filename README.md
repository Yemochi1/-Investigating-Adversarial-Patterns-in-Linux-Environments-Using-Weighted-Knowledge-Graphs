# Implementing-Digital-Forensic-Techniques-to-Reconstruct-a-Major-Cyberattack-s-Cycle
Digital forensic techniques 
# Research Objectives
1. Does the pattern-based detector hold up on Linux and cloud (e.g, CloudTrail/Azure) telemetry without changing the core method?
2. What are the time-to-detection and throughput under streaming SIEM workloads?
# Methodology
1. Reproduce the baseline: rebuild the ATT&CK knowledge graph, extract adversarial patterns, and run detection on Windows event log datasets (data leakage, unauthorized access).
2. Add cross-platform logs: collect Linux auditd/Sysmon-for-Linux and one cloud dataset (e.g, AWS CloudTrail). Map their events to ATT&CK techniques using Sigma rules or ATT&CK mappings.
3. Evaluate accuracy: measure precision, recall and kill-chain coverage for each platform, compare results and identify where ATT&CK/Sigma support is weak or strong.
4. Setup streaming ingestion, measure performance and tune thresholds: replay logs with real timestamps using Beats/Kafka into ElasticSearch to simulate real-time SIEM pipelines. Record end-to-end latency and throughput. Vary the edge-weight threshold in graph extraction and analyze the trade-offs between detection accuracy and latency/throughput.
