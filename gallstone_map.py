import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("gallstone.csv")

df["Gender"].value_counts().sort_index().plot(kind="bar", title="Gender Distribution")
plt.savefig("gender.png")
plt.close()

glucose = df["Glucose"]
plt.hist(glucose, bins=30)
plt.title("Glucose Distribution")
plt.savefig("glucose.png")
plt.close()

gender_counts = df["Gender"].value_counts()
mean, spread = glucose.mean(), glucose.std()
outliers = glucose[abs((glucose - mean) / spread) > 2]

print("0: ", gender_counts.get(0, 0), "1:", gender_counts.get(1, 0))
print(f"Mean: {mean:.2f}, std={spread:.2f}, normal range [{mean-2*spread:.2f}, {mean+2*spread:.2f}]")
print("Outliers: ", outliers.tolist())