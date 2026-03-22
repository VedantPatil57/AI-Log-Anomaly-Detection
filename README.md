# AI-Based Log Anomaly Detection

## Overview
This project detects abnormal login activity using machine learning. It uses login data extracted from Splunk logs to identify suspicious behavior such as brute-force attacks.

## Problem
Traditional detection relies on fixed thresholds. This project uses AI to automatically detect unusual login patterns without predefined rules.

## Approach
- Extracted login data (Event ID 4625) from Splunk
- Aggregated login attempts per minute
- Used Isolation Forest model for anomaly detection
- Identified abnormal login spikes

## Dataset
Sample fields:
- timestamp
- ip
- login_count

## Output
The model flags abnormal login spikes as anomalies.

Example:
- Normal: login_count = 1–5  
- Anomaly: login_count = 19, 21  

## Results
- Successfully detected high-frequency login spikes
- Filtered only suspicious events into output file

## Files
- log_data.csv → input dataset  
- anomaly_detection.py → detection script  
- detected_anomalies.csv → output anomalies  

## Visualization
The graph highlights abnormal login spikes using red markers.

## Conclusion
The model effectively identifies abnormal login behavior and can be used for detecting brute-force attacks.
