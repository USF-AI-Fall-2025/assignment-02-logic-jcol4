import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#load gallstone dataset
df = pd.read_csv("gallstone.csv")

#first sort the values of gender and then create a bar chart showing the distribution
df["Gender"].value_counts().sort_index().plot(kind="bar", title="Gender Distribution")
plt.savefig("gender.png")
plt.close()

#get the glucose data
#make a histograph to show the distribution of the glucose levels
glucose = df["Glucose"]
plt.hist(glucose, bins=30)
plt.title("Glucose Distribution")
plt.savefig("glucose.png")
plt.close()
#both figures are saved and close plt

#get the gender counts from data set
gender_counts = df["Gender"].value_counts()
#access the mean and standard deviation from the dataset
mean, standard_dev = glucose.mean(), glucose.std()
#find all the outliers - all values more than two standard deviations away from the mean
outliers = glucose[abs((glucose - mean) / standard_dev) > 2]

#print all the appropriate data
print("0: ", gender_counts.get(0, 0), "1:", gender_counts.get(1, 0))
print(f"Mean: {mean:.2f}, std={standard_dev:.2f}, normal range [{mean-2*standard_dev:.2f}, {mean+2*standard_dev:.2f}]")
print("Outliers: ", outliers.tolist())