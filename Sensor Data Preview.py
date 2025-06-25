#for person-1
import os
import pandas as pd

base_path = '/content/dsa_data/data'  # Adjust if needed
activities = [f'a{str(i).zfill(2)}' for i in range(1, 20)]
participant = 'p1'

# Loop through each activity
for act in activities:
    file_path = os.path.join(base_path, act, participant, 's01.txt')
    if not os.path.exists(file_path):
        print(f"Missing: {file_path}")
        continue

    # Read without headers
    df = pd.read_csv(file_path, header=None)

    # Display first 5 rows and 15 columns
    preview = df.iloc[:5, :15]
    print(f"\n🔹 Activity: {act} — first 5 rows × 15 cols from s01.txt")
    print(preview)
