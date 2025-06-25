import os
import pandas as pd
import matplotlib.pyplot as plt

base_path = "dsa_data/data"
person = "p1"
segment = "s01.txt"

# 2 plots per activity (first row across sensors + one sensor column across time)
plt.figure(figsize=(15, 40))
plot_num = 1

for i in range(1, 20):  # a01 to a19
    activity = f"a{i:02d}"
    file_path = os.path.join(base_path, activity, person, segment)

    try:
        df = pd.read_csv(file_path, header=None)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        continue

    # --- Plot 1: First row only (sensor snapshot at t = 0s) ---
    plt.subplot(19, 2, plot_num)
    plt.plot(df.iloc[0, :], marker='o', color='blue')
    plt.title(f"{activity.upper()} - First Row (Sensor Snapshot)")
    plt.xlabel("Sensor Index (0 to 44)")
    plt.ylabel("Value at t = 0s")
    plt.grid(True)
    plot_num += 1

    # --- Plot 2: One column only (sensor value over time) ---
    plt.subplot(19, 2, plot_num)
    sensor_col = 0  # You can change this to any sensor column index 0–44
    plt.plot(df.iloc[:, sensor_col], color='green')
    plt.title(f"{activity.upper()} - Column {sensor_col} (Time Series)")
    plt.xlabel("Time Step (each = 0.04s)")
    plt.ylabel("Sensor Value")
    plt.grid(True)
    plot_num += 1

plt.tight_layout()
plt.suptitle("First Row and Sensor Time Series (s01, p1) — A01 to A19", fontsize=16, y=1.02)
plt.show()
