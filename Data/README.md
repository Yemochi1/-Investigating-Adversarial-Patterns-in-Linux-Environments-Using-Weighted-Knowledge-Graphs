# Data Directory
This directory is the designated location for the raw data files required by the analysis script.
# Required File
* `audit_logs.csv`
The `audit_logs.csv` file is **intentionally excluded** from this repository using the `.gitignore` file.

# How to Run the Project

1.  Export  `auditd` log data from  ELK Stack.
2.  Name the exported file `audit_logs.csv`.
3.  **Place the `audit_logs.csv` file directly into this `Data/` folder.**
4.  Run the main `run_analysis.py` script from the root of the project

# Data Format Requirements
The analysis script (`src/mapping.py`) is configured to expect a specific data format.
* **`@timestamp` column:** Must be in the exact format: `Oct 26, 2025 @ 00:01:11.784` (Format string: `%b %d, %Y @ %H:%M:%S.%f`).
* **`process.executable` column:** Must contain the full file path of the executed process (e.g., `/usr/bin/whoami`).
