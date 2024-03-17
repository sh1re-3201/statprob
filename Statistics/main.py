import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset Iris
iris_data = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')

# Menampilkan beberapa baris pertama dari dataset
print(iris_data.head())

# Melihat ringkasan statistik deskriptif dari dataset
print(iris_data.describe())

# Melihat distribusi variabel numerik dengan histogram
iris_data.hist(figsize=(10,8))
plt.show()

# Membuat Pairplot untuk melihat hubungan antar variabel
sns.pairplot(iris_data, hue='species')
plt.show()

# Membuat Boxplot untuk melihat distribusi dan outlier
plt.figure(figsize=(10,8))
sns.boxplot(data=iris_data.drop(columns='species'))
plt.show()

# Melihat korelasi antar variabel numerik
plt.figure(figsize=(10,8))
sns.heatmap(iris_data.corr(), annot=True, cmap='coolwarm')
plt.show()