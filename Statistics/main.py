import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
"""
# plt.style.use('ggplot')
#pd.set_option('max_columns',200)"""


# Tentukan path lengkap ke file 'titanic.csv'
file_path = 'C:/path/to/your/directory/titanic.csv'

# Baca dataset Titanic dari file 'titanic.csv'
titanic_data = pd.read_csv(file_path)

titanic_data = pd.read_csv('C:/path/to/your/titanic.csv')

# Membaca dataset Titanic
titanic_data = pd.read_csv('titanic.csv')

# Menampilkan beberapa baris pertama dari dataset
print(titanic_data.head())

# Melihat ringkasan statistik deskriptif dari dataset
print(titanic_data.describe())

# Melihat distribusi variabel numerik dengan histogram
titanic_data.hist(figsize=(10,8))
plt.show()

# Membuat Boxplot untuk melihat distribusi dan outlier
plt.figure(figsize=(10,8))
sns.boxplot(data=titanic_data[['Age', 'Fare']])
plt.show()

# Melihat korelasi antar variabel numerik
plt.figure(figsize=(10,8))
sns.heatmap(titanic_data.corr(), annot=True, cmap='coolwarm')
plt.show()

# Membuat diagram batang untuk variabel kategorikal
plt.figure(figsize=(10,8))
sns.countplot(x='Survived', data=titanic_data, hue='Sex')
plt.show()
"""

df = pd.read_csv('https://drive.usercontent.google.com/u/0/uc?id=19cTc2gQO_V0UBgpK1tq9QcnjuLxVqznY&export=download')
df.head()"""