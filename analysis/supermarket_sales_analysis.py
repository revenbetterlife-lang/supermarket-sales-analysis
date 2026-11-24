# ==============================
# Supermarket Sales Analysis
# ==============================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("supermarket_sales.csv")

# Display First 5 Rows
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Statistical Description
print("\nStatistical Summary:")
print(df.describe())

# ==============================
# Statistical Calculations
# ==============================

# Mean
mean_value = df["Total"].mean()
print("\nMean =", mean_value)

# Median
median_value = df["Total"].median()
print("Median =", median_value)

# Mode
mode_value = df["Total"].mode()[0]
print("Mode =", mode_value)

# Range
range_value = df["Total"].max() - df["Total"].min()
print("Range =", range_value)

# Variance
variance_value = df["Total"].var()
print("Variance =", variance_value)

# Standard Deviation
std_value = df["Total"].std()
print("Standard Deviation =", std_value)

# ==============================
# Data Visualization
# ==============================

# Bar Plot
plt.figure(figsize=(6,4))
sns.countplot(x="Branch", data=df)
plt.title("Branch Sales Count")
plt.show()

# Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df["Rating"], df["Total"])
plt.xlabel("Rating")
plt.ylabel("Total")
plt.title("Rating vs Total")
plt.show()

# Histogram
plt.figure(figsize=(6,4))
plt.hist(df["Total"], bins=10)
plt.title("Total Distribution")
plt.xlabel("Total")
plt.ylabel("Frequency")
plt.show()

# Box Plot
plt.figure(figsize=(6,4))
sns.boxplot(y=df["Total"])
plt.title("Box Plot of Total")
plt.show()

# Pie Chart
payment_counts = df["Payment"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(payment_counts,
        labels=payment_counts.index,
        autopct='%1.1f%%')

plt.title("Payment Methods")
plt.show()

# ==============================
# Additional Analysis
# ==============================

# Most Selling Product Line
print("\nMost Selling Product Line:")
print(df["Product line"].value_counts())

# Most Used Payment Method
print("\nMost Used Payment Method:")
print(df["Payment"].value_counts())

# Highest Selling Branch
print("\nHighest Selling Branch:")
print(df["Branch"].value_counts())

# ==============================
# End of Project
# ==============================

print("\nProject Finished Successfully")