import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
iris = sns.load_dataset('iris')

# Display the first few rows of the dataset
print(iris.head())

# Bar chart
plt.figure(figsize=(10, 6))
sns.countplot(x='species', data=iris)
plt.title('Count of each Iris species')
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=iris)
plt.title('Sepal Length vs Sepal Width')
plt.show()

# Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(iris.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
