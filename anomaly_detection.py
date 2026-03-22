import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\patil\Desktop\log_data.csv")

# convert timestamp
data['timestamp'] = pd.to_datetime(data['timestamp'])

# features for model
X = data[['login_count']]

model = IsolationForest(contamination=0.2, random_state=42)
model.fit(X)

data['anomaly'] = model.predict(X)


anomalies = data[data['anomaly'] == -1]

print("\nSuspicious Activity Detected:\n")
print(anomalies)

# Separate normal and anomaly data
normal = data[data['anomaly'] == 1]
anomalies = data[data['anomaly'] == -1]

plt.figure(figsize=(10,6))

# Plot full login trend
plt.plot(data['timestamp'], data['login_count'], label='Login Count', marker='o')

# Highlight anomalies
plt.scatter(anomalies['timestamp'], anomalies['login_count'],
            color='red', label='Anomaly', s=100)

# Add labels to anomaly points
for i in anomalies.index:
    plt.text(data['timestamp'][i],
             data['login_count'][i] + 0.5,
             f"{data['login_count'][i]}",
             color='red',
             fontsize=9,
             ha='center')

# Labels
plt.xlabel("Timestamp")
plt.ylabel("Login Count")
plt.title("AI-Based Login Anomaly Detection")

# Rotate time labels
plt.xticks(rotation=45)

# Legend + grid
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

anomalies.to_csv("detected_anomalies.csv", index=False)